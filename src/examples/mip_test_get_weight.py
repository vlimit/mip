#!/usr/bin/env python

"""
MiP Test program to get an angle representing the amount of weight MiP is carrying
To Use:
mip_test_get_weight.py -i hci0 -b D0:39:72:C4:7A:01 

"""

import logging
import mippy
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Get MiPs weight angle.')
    mippy.add_arguments(parser)
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG)
    gt = mippy.GattTool(args.adaptor, args.device)

    mip = mippy.Mip(gt)
    weightAngle = mip.getWeight()
    orientationString = ['on back' , 'face down' , 'upright' , 'picked up',
                         'hand stand' , 'face down on tray' , 
                         'on back with kickstand' ]
    print 'Weight Angle (+ve = weight on back): %f' % (weightAngle)
