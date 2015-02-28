#!/usr/bin/env python

"""
Setup a movement GUI.
Move Mip based on the GUI
mip_test_continuous_drive_gui.py -i hci0 -b D0:39:72:C4:7A:01
"""

#from Tkinter import *
import Tkinter
from movement_canvas import MovementCanvas
import logging
import mippy
import argparse

def updateMovement():
    # movementCanvas.positionX,movementCanvas.positionY, (-50 - 50)
    # movementCanvas.positionAngle,movementCanvas.positionMagnitude
    if movementCanvas.positionMagnitude < 20:
        logging.debug('updateMovement : stopping')
        mip.continuousDriveForward(0x0)
    elif movementCanvas.positionY < 0 and movementCanvas.positionAngle > 45 and movementCanvas.positionAngle < 135:
        speed = int(movementCanvas.positionMagnitude / 3)
        logging.debug('updateMovement : forward : speed %d ' % speed)
        mip.continuousDriveForward(int(speed))
    elif movementCanvas.positionY > 0 and movementCanvas.positionAngle > 225 and movementCanvas.positionAngle < 315:
        speed = int(movementCanvas.positionMagnitude / 3)
        logging.debug('updateMovement : backward : speed %d ' % speed)
        mip.continuousDriveBackward(speed)
# forwards turns
    elif movementCanvas.positionAngle >= 0 and movementCanvas.positionAngle <= 45:
        forwardSpeed = int(movementCanvas.positionY * (0x20/50))
        turnSpeed = int(movementCanvas.positionX * (0x20/50))
        logging.debug('updateMovement : forward right : forward speed %d : turn speed %d' % (forwardSpeed,turnSpeed))
        mip.continuousTurnForwardRight(forwardSpeed,turnSpeed)
    elif movementCanvas.positionAngle >= 135 and movementCanvas.positionAngle <= 180:
        forwardSpeed = int(movementCanvas.positionY * (0x20/50))
        turnSpeed = int(movementCanvas.positionX * (0x20/50))
        turnSpeed = -turnSpeed
        logging.debug('updateMovement : forward left : forward speed %d : turn speed %d' % (forwardSpeed,turnSpeed))
        mip.continuousTurnForwardLeft(forwardSpeed,turnSpeed)
# backwards turns
    elif movementCanvas.positionAngle >= 315 and movementCanvas.positionAngle <= 360:
        forwardSpeed = int(movementCanvas.positionY * (0x20/50))
        forwardSpeed = -forwardSpeed
        turnSpeed = int(movementCanvas.positionX * (0x20/50))
        logging.debug('updateMovement : backward right : forward speed %d : turn speed %d' % (forwardSpeed,turnSpeed))
        mip.continuousTurnBackwardRight(forwardSpeed,turnSpeed)
    elif movementCanvas.positionAngle >= 180 and movementCanvas.positionAngle <= 225:
        forwardSpeed = int(movementCanvas.positionY * (0x20/50))
        forwardSpeed = -forwardSpeed
        turnSpeed = int(movementCanvas.positionX * (0x20/50))
        turnSpeed = -turnSpeed
        logging.debug('updateMovement : backward left : forward speed %d : turn speed %d' % (forwardSpeed,turnSpeed))
        mip.continuousTurnBackwardLeft(forwardSpeed,turnSpeed)

    top.after(50,updateMovement)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Continuous Drive GUI.')
    mippy.add_arguments(parser)
    args = parser.parse_args()

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
