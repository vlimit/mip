import argparse
import logging
import pexpect
import sys
import time


class GattTool:

    PROMPT = '.*\[LE\]>'

    def __init__(self, interface, address):
        cmd = 'gatttool -i %s -b %s -I' % (interface, address)
        self.child = pexpect.spawn(cmd)
        self.child.logfile = sys.stdout
        self.child.expect(self.PROMPT, timeout=1)

    def connect(self):
        self.child.sendline('connect')
        self.child.expect(self.PROMPT, timeout=1)

    def disconnect(self):
        self.child.sendline('disconnect')
        self.child.expect(self.PROMPT, timeout=1)

    def charWriteCmd(self, handle, byte_vals):

        if not iter(byte_vals):
            byte_vals = [byte_vals]

        val = ''
        for byte_val in byte_vals:
            val += '%2.2x' % (byte_val)

        cmd = 'char-write-cmd 0x%4.4x ' % (handle) + val
        logging.debug('gatttool cmd: %s' % (cmd))
        self.child.sendline(cmd)


class Mip:
    def __init__(self, gt):
        self.gt = gt
        self.gt.connect()   
        time.sleep(2)
 
    def playSound(self, id):
        self.gt.charWriteCmd(0x13, [0x06, id, 0])
        
    def setMipPosition(self, position):
        self.gt.charWriteCmd(0x13, [0x08, position])

    def distanceDrive(self, distance, angle=0):
        """
            distance (+/-m)
            angle    (+/-deg)
        """

        if distance > 0:
            direction = 0
        else:
            direction = 1
        distance = abs(distance)

        if angle > 0:
            rotation = 0
        else:
            rotation = 1
        angle = abs(angle)
        self.gt.charWriteCmd(
            0x13, [
                0x70, 
                direction, 
                int(round(distance * 100)), 
                rotation, angle >> 8, 
                angle & 0xff])

        t = distance * 5
        time.sleep(t)

    def driveWithTime(self, speed, time_):
        """
            speed (-30...+30)
            time  (s)
        """

        t = int(round(time_/0.05))

        speed_mag = abs(speed)
        speed_sign = speed/speed_mag

        if speed_sign > 0:
            # Forward
            self.gt.charWriteCmd(0x13, [0x71, speed_mag, t/0.07])
        else:
            # Reverse
            self.gt.charWriteCmd(0x13, [0x72, speed_mag, t/0.07])

    def turnByAngle(self, angle, speed=15):
        """
            angle (deg)
            speed (0-24)
        """

        angle_mag = abs(angle)
        angle_sign = angle / angle_mag

        if angle_sign > 0:
            self.gt.charWriteCmd(0x13, [0x74, int(round(angle_mag / 5.0)), speed])
        else:
            self.gt.charWriteCmd(0x13, [0x73, int(round(angle_mag / 5.0)), speed])

        t = angle_mag / 360.0 * 0.9
        time.sleep(t)

    # Add continuous drive
    # Add set game mode

    def setChestLed(self, r, g, b):

        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)

        self.gt.charWriteCmd(0x13, [0x84, r, g, b])


class Turtle:
    def __init__(self, mip):
        self.mip = mip

    def left(self, angle):
        self.mip.turnByAngle(-angle)

    def right(self, angle):
        self.mip.turnByAngle(angle)

    def forward(self, distance):
        self.mip.distanceDrive(distance)

    def reverse(self, distance):
        self.mip.distanceDrive(-distance)


def add_arguments(parser):

    """Add gatttool-style arguments to an optparse parser."""

    parser.add_argument(
        '-i',
        '--adaptor',
        default='hci0',
        help='Specify local adaptor interface')

    parser.add_argument(
        '-b',
        '--device',
        default='D0:39:72:B8:C5:84',
        help='Specify remote bluetooth address')


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Quick test program.')

    parser.add_argument(
        '-i', 
        '--adaptor', 
        default='hci0', 
        help='Specify local adaptor interface')

    parser.add_argument(
        '-b', 
        '--device',  
        default='D0:39:72:B8:C5:84', 
        help='Specify remote bluetooth address')

    args = parser.parse_args()

    gt = GattTool(args.adaptor, args.device)

    mip = Mip(gt)

    mip.playSound(0x4d)
