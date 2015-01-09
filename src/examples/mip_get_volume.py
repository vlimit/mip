#!/usr/bin/env python

"""
MiP Sound tester.
To Use:
mip_get_volume.py -i hci0 -b D0:39:72:C4:7A:01 
Prints current volume level : should be between 0 and 7
"""

import mippy
import argparse
import time

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Get MiP Volume.')
    mippy.add_arguments(parser)
    args = parser.parse_args()

    gt = mippy.GattTool(args.adaptor, args.device)

    mip = mippy.Mip(gt)
    volume = mip.getVolume()
    time.sleep(1)
    # play roam sound
    mip.playSound(0xfd)
    print 'Volume (0..7): %d' % (volume)
