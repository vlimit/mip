#!/usr/bin/env python

"""
MiP Sound tester.
To Use:
mip_test_sound.py -i hci0 -b D0:39:72:C4:7A:01 -s <n>
<n> 1 - 106
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
11 = lep
12 = lep
13 = lep
14 = ahhh! (interested)
15 = arhhh! (disapointed)
16 = oh yeah
17 = meh (derogatory?)
18 = beh
19 =  see yah?
20 = bad a bad a bad a (MiP talking to himself?)
21 = bad a bad a bad a (MiP talking to himself?)
22 = stop?
23 = goodnight?
24 = bang of drum
25 = bang of drum (different)
26 = Hi Yah!
27 = some word.. gay?
28 = Ha Ha Ha lep
29 = lets go!
30 = bah bah bah (low)
31 = her (low)
32 = eigh (something horrible)
33 = narrrh
34 = lets go it?
35 = hellllooo (sexy)
36 = bah? (questioning)
37 = ohaye
38 = huh?
39 = dur dur dur dur dooo (humming to himself)
40 = la la la la laaa (humming to himself)
41 = hah ha hah, hah hah hahaha...
42 = heaaahhh
43 = harp sound plus he says something
44 = lets MiP?
45 = talks to himself
46 = 'kay (as when in training mode)
47 = Music (part one)
48 = Music (part two)
49 = Out of power sound
50 = Happy!
51 = yeuh (collision warning sound in roam mode)
52 = Yah ha ha ha
53 = Music (MiP says music not plays it)
54 = oh ah (collision warning sound in roam mode)
55 = Oh Oh (something bad) (part of power down noise?)
56 = Oh yeah!
57 = high pitch 'Happy!'
58 = howell (sound when MiP sees a wall in cage mode?)
59 = howell (higher pitch)
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
78 = waaaaahhhh
79 = wuuuy (higher pitch)
80 = yeuh
81 = Yeah!
82 = You (low pitch)
83 = happy/snappy? (low pitch)
84 = oooee (low pitch)
85 = aaeeeh (higher pitch)
86 = ribit
87 = Boring
88 = errr (low pich)
89 = lets go
90 = yipppee! (higher pitch)
91 = ho ho ho ho ho
92 = crafteee?
93 = crafty
94 = ha ha
95 = this is mip (low pitch)
96 = sigharhhh
97 = MiP crying (lost the cage game?)
98 = nuh (low pitch)
99 = snifty?
100 = Aaahhhh (large sigh)
101 = funny little beeping sound
102 = drum
103 = laser beam
104 = swanny whistle sound
105 = No sound - stop sound playing
106 = mip
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
