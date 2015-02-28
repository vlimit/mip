#!/usr/bin/env python

"""
MiP Eye control test program
To Use:
mip_test_eyes.py -i hci0 -b D0:39:72:C4:7A:01 -e1 <n> -e2 <n> -e3<n> -e4 <n>
Each e<n> parameter controls one half of one of MiPs eyes: 
eye1 left hand side left eye
eye2 right hand side left eye
eye3 left hand side right eye
eye4 right hand side right eye
<n> 
0 = off
1 = on
2 = blink slow
3 = blink fast
"""

import mippy
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Test MiP Sounds.')
    mippy.add_arguments(parser)
    parser.add_argument('-e1','--eye1',default=0x1,
           help='Eye 1 control. 0 = off, 1 = on, 2 = blink slow, 3 = blink fast', type=int)
    parser.add_argument('-e2','--eye2',default=0x1,
           help='Eye 2 control. 0 = off, 1 = on, 2 = blink slow, 3 = blink fast', type=int)
    parser.add_argument('-e3','--eye3',default=0x1,
           help='Eye 3 control. 0 = off, 1 = on, 2 = blink slow, 3 = blink fast', type=int)
    parser.add_argument('-e4','--eye4',default=0x1,
           help='Eye 4 control. 0 = off, 1 = on, 2 = blink slow, 3 = blink fast', type=int)
    args = parser.parse_args()

    gt = mippy.GattTool(args.adaptor, args.device)

    mip = mippy.Mip(gt)
    mip.setHeadLed(args.eye1,args.eye2,args.eye3,args.eye4)
    # sleep a bit to display results
    time.sleep(10.0)
