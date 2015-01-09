#!/usr/bin/env python

"""
MiP Test program to get an angle representing the amount of weight MiP is carrying
To Use:
mip_test_get_odometer.py -i hci0 -b D0:39:72:C4:7A:01 

"""

import logging
import mippy
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Get MiPs odometer.')
    mippy.add_arguments(parser)
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG)
    gt = mippy.GattTool(args.adaptor, args.device)

    mip = mippy.Mip(gt)
    distance = mip.getOdometer()
    print 'Distane (cm): %f' % (distance)
