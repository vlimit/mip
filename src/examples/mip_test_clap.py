#!/usr/bin/env python

"""
MiP Test program to test clap recognition software
To Use:
./mip_test_clap.py -i hci0 -b D0:39:72:C4:7A:01

"""
import logging
import mippy
import argparse
import time

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Test MiPs clap recognition.')
    mippy.add_arguments(parser)
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG)

    gt = mippy.GattTool(args.adaptor, args.device)
    mip = mippy.Mip(gt)
    # enable clap recognition
    logging.debug('Enable clap')
    mip.clapEnable(0x1)
    clapStatus = mip.requestClapStatus()
    logging.debug('Clap status %x.' % (clapStatus))
    logging.debug('Entering loop requesting clap status: Ctrl-C to exit.')
    done = 0
    while done == 0:
        logging.debug('Requesting clap times.')
        retval = mip.getClapTimes()
        if retval > 0:
            logging.debug('Clap detected')
        else:
            logging.debug('NO Clap detected')
