#!/usr/bin/env python

"""
MiP Volume control
To Use:
mip_set_volume.py -i hci0 -b D0:39:72:C4:7A:01 -v <n>
volume should be between 0 and 7
"""

import mippy
import argparse
import time

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='MiP Volume control.')
    mippy.add_arguments(parser)
    parser.add_argument(
        '-v',
        '--volume',
        default=0x1,
        help='Specify volume (0..7)', type=int)
    args = parser.parse_args()

    gt = mippy.GattTool(args.adaptor, args.device)

    mip = mippy.Mip(gt)
    mip.setVolume(args.volume)
    time.sleep(1)
    # play roam sound at new volume level
    mip.playSound(0xfd)
