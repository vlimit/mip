#!/usr/bin/env python

"""
MiP Test program to drive forwards in continuous drive mode 
To Use:
mip_test_continuous_drive.py -i hci0 -b D0:39:72:C4:7A:01 -s <speed>
Fw:0x01(slow)~-0x20(fast)	Buffer = 0
OR Bw:0x21(slow)~0x40(fast)	This command is for single drive or turn
right spin:0x41(slow)~0x60(fast)	Note:Sending per 50ms if held
OR Left spin:0x61(slow)~0x80(fast)	
Carzy Fw:0x81(slow)~-0xA0(fast)	
OR Carzy Bw:0x81(slow)~0xC0(fast)	
Carzy right spin:0xC1(slow)~0xE0(fast)	
OR Carzy Left spin:0xE1(slow)~0xFF(fast)
"""

import logging
import mippy
import argparse
import time
import pexpect

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Test MiPs radar.')
    mippy.add_arguments(parser)
    def auto_int(x):
        return int(x,0)

    parser.add_argument(
        '-s',
        '--speed',
        default=0x1,
        help='Specify speed (0..32)', type=auto_int)
    parser.add_argument(
        '-t',
        '--turnspeed',
        default=0x0,
        help='Specify number (0..32)', type=auto_int)
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG)

    # low level gattool test
    gt = mippy.GattTool(args.adaptor, args.device)
    gt.connect()
    time.sleep(2)
    # turn radar mode on
    logging.debug('Writing MiP Set Gesture Radar Mode  ON: 0x0c 0x04 .')
    gt.charWriteCmd(0x13, [0x0c, 0x04])
    done = 0
    while done == 0:
        #gt.charWriteCmd(0x13, [0x78, args.speed])
        gt.charWriteCmd(0x13, [0x78, args.speed, args.turnspeed])
        try:
            returnVals = gt.charReadReply(0x13, -1 ,timeout=0.02)
            if returnVals[0] == 0x0c:   # radar response
                radarResponse = returnVals[1]
            elif returnVals[0] == 0x79: # MiPStatus response
                # returnVals[1] is battery level
                orientation = returnVals[2]
        except pexpect.TIMEOUT:
            radarResponse = 0
            orientation = 2
        # radarResponse value 0 - no radar response
        # radarResponse value 1 - no object
        # radarResponse value 2 - object between 10cm-30cm
        # radarResponse value 3 - object less than 10cm
        #  orientation 0 on back
        #  orientation 2 upright
        # Stop if we detect an object or we are not upright
        done = (radarResponse > 1) or (orientation != 2)

