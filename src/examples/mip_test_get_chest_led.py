#!/usr/bin/env python

"""
MiP Test program to get the chest LED colour
To Use:
mip_test_get_chest_led.py -i hci0 -b D0:39:72:C4:7A:01 

"""

import logging
import mippy
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Get MiPs chest LED colour.')
    mippy.add_arguments(parser)
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG)
    gt = mippy.GattTool(args.adaptor, args.device)

    mip = mippy.Mip(gt)
# get Chest LE colour
    colourVals = []
    colourVals = mip.getChestLed()
    print 'Red: %d' % (colourVals[0])
    print 'Green: %d' % (colourVals[1])
    print 'Blue: %d' % (colourVals[2])
