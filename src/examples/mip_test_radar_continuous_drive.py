#!/usr/bin/env python

"""
MiP Test program to drive forwards in continuous drive mode until the radar says stop
To Use:
mip_test_radar_continuous_drive.py -i hci0 -b D0:39:72:C4:7A:01 -s <speed>

"""

import logging
import mippy
import argparse
import time

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Test MiPs radar.')
    mippy.add_arguments(parser)
    parser.add_argument(
        '-s',
        '--speed',
        default=0x1,
        help='Specify speed (0..32)', type=int)
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG)

    gt = mippy.GattTool(args.adaptor, args.device)
    mip = mippy.Mip(gt)
    mip.continuousDriveForwardUntilRadar(args.speed)
