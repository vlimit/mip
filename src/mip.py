
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

    def charWriteCmd(self, handle, value):
        cmd = 'char-write-cmd 0x%4.4x %6.6x' % (handle, value)
        self.child.sendline(cmd)

class Mip:
    def __init__(self, gt):
        self.gt = gt
        self.gt.connect()   
        time.sleep(2)
 
    def forward(self, dist):
        self.gt.charWriteCmd(0x13, 0x70 << 16 | 00 << 8 | int(round(dist * 50)))
        t = dist * 5
        time.sleep(t)

    def reverse(self, dist):
        self.gt.charWriteCmd(0x13, 0x70 << 16 | 01 << 8 | int(round(dist * 50)))
        t = dist * 5
        time.sleep(t)

    def left(self, angle, speed=15):
        self.gt.charWriteCmd(0x13, 0x73 << 16 | int(round(angle / 4.0)) << 8 | speed)
        t = angle / 360.0 * 0.9
        time.sleep(t)

    def right(self, angle, speed=15):
        self.gt.charWriteCmd(0x13, 0x74 << 16 | int(round(angle / 4.0)) << 8 | speed)
        t = angle / 360.0 * 0.9
        time.sleep(t)

    def sound(self, id):
        self.gt.charWriteCmd(0x13, 0x06 << 16 | id << 8 | 0)
        
if __name__ == '__main__':

    gt = GattTool('hci0', 'D0:39:72:B8:C5:84')
    mip = Mip(gt)

    mip.sound(0x4d)

    if 0:
        mip.forward(0.4)
        mip.right(90)
        mip.forward(0.4)
        mip.right(90)
        mip.forward(0.4)
        mip.right(90)
        mip.forward(0.4)
        mip.right(90)

    if 1:
        for i in range(10):
            mip.left(720)
            mip.right(720)

