#!/usr/bin/env python

"""
Logo-style turtle example.
"""

import argparse
import os.path
import sys
import time

sys.path.append(os.path.join(os.path.split(__file__)[0], '..'))

import mippy

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Turtle example.')
    mippy.add_arguments(parser)
    args = parser.parse_args()

    gt = mippy.GattTool(args.adaptor, args.device)

    mip = mippy.Mip(gt)
    mip.playSound(0x4d)

    turtle = mippy.Turtle(mip)

    for i in range(4):
        turtle.forward(0.4)
        turtle.right(90)

    for i in range(2):
        turtle.right(720)
        turtle.left(720)

    mip.setChestLed(0.5, 0.0, 0.0)

    time.sleep(2)

