#!/usr/bin/env python

"""
MiP Sound tester.
To Use:
mip_test_sound.py -i hci0 -b D0:39:72:C4:7A:01 -s <n>
1 = beep
2 = burp
3 = ewwp - ah
4 = la la la la (lower)
5 = small raspberry?
6 = rerrr
7 = punching sound
8 = punching sound
9 = harder punching sound
10 = lep

60 = play
61 = lets fish?
62 = fire?
63 = click click
64 = rar
65 = la la la la la (derogatory sound)
66 = ah-choo (sneeze?)
67 = snoring
68 = feck?
69 = whish (sound made when recognising a gesture)
70 = whish (sound made when recognising a gesture)
71 = X?
72 = lets trick
73 = duh duh duh duh duh duh (cage escape sound)
74 = waaaah
75 = wakey wakey?
76 = yay
0xfd = 77 = roam whistle

"""

import mippy
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Test MiP Sounds.')
    mippy.add_arguments(parser)
    parser.add_argument(
        '-s',
        '--sound',
        default=0x4d,
        help='Specify sound number (1-106). 105 is no sound', type=int)
    args = parser.parse_args()

    gt = mippy.GattTool(args.adaptor, args.device)

    mip = mippy.Mip(gt)
# roam whistle
    mip.playSound(args.sound)
