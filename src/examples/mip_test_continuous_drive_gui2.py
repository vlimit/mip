#!/usr/bin/env python

"""
Setup a movement GUI.
Move Mip based on the GUI
mip_test_continuous_drive_gui2.py -i hci0 -b D0:39:72:C4:7A:01 [-c|--carzy}
"""

#from Tkinter import *
import Tkinter
from movement_canvas import MovementCanvas
import logging
import mippy
import argparse

carzy = 0

def updateMovement():
    # movementCanvas.positionX,movementCanvas.positionY, (-50 - 50)
    # movementCanvas.positionAngle,movementCanvas.positionMagnitude
    if movementCanvas.positionMagnitude < 10:
        logging.debug('updateMovement : stopping')
        mip.continuousDriveForward(0x0)
    else:
        forwardSpeed = int((-movementCanvas.positionY * 0x20)/50)
        turnSpeed = int((movementCanvas.positionX * 0x20)/50)
        logging.debug('updateMovement : forwardSpeed %d : turnSpeed %d' % (forwardSpeed,turnSpeed))
        if carzy > 0:
            mip.continuousCarzyDrive(forwardSpeed,turnSpeed)
        else:
            mip.continuousDrive(forwardSpeed,turnSpeed)
    top.after(50,updateMovement)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Continuous Drive GUI.')
    mippy.add_arguments(parser)
    parser.add_argument(
        '-c',
        '--carzy',
        default=0x0,action='count',
        help='Carzy mode')
    args = parser.parse_args()

    if args.carzy > 0:
        carzy = 1
    else:
        carzy = 0
    print ("Carzy Mode = %d " % (carzy))

    logging.basicConfig(level=logging.DEBUG)
    gt = mippy.GattTool(args.adaptor, args.device)
    mip = mippy.Mip(gt)
    # start gui
    top = Tkinter.Tk()
    movementCanvas = MovementCanvas(top,300,300)
    movementCanvas.setBindings()
    #movementCanvas.addUpdateCallback(movement)
    movementCanvas.pack()
    top.after(50,updateMovement)
    top.mainloop()
