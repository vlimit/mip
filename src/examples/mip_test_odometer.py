#!/usr/bin/env python

"""
MiP Test program to test problems getting odometer readings
To Use:
mip_test_odometer.py -i hci0 -b D0:39:72:C4:7A:01 -d <m>

"""

import logging
import mippy
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Test MiPs odometer.')
    mippy.add_arguments(parser)
    parser.add_argument(
        '-d',
        '--distance',
        default=0.1,
        help='Distance to move in metres', type=float)
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG)
    gt = mippy.GattTool(args.adaptor, args.device)

    mip = mippy.Mip(gt)
    mip.resetOdomemeter()
    distance = mip.getOdometer()
    print 'Distane (cm): %f' % (distance)
    mip.distanceDrive(args.distance)
    distance = mip.getOdometer()
    print 'Distane (cm): %f' % (distance)
# 0.1m = 1485 = 30cm @ 48.5/cm
# 0.2m = 2128 = 43cm @ 48.5/cm
# 0.3m = 2089 = 43cm @ 48.5/cm
# 0.5m = 3400 = 70cm @ 48.5/cmm
# 1.0m = 6253 = 129cm @ 48.5/cm
