#!/usr/bin/env python

"""
This GUI is designed for general eploration using MiP.
./mip_explorer_gui.py -i hci0 -b D0:39:72:C4:7A:01
"""
from Tkinter import *
#import Tkinter
from movement_canvas import MovementCanvas
import logging
import mippy
import argparse

def getDistance():
    distanceString = distanceEntry.get()
    distance = float(distanceString)
    # distance = 3.0 causes MiP to spin instead - number overflow?
    if distance > 2.5:
        distance = 2.5
    return distance

def getAngle():
    angleString = angleEntry.get()
    angle = int(angleString)
    return angle

def forwardCallBack():
    distance = getDistance()
    mip.distanceDrive(distance=distance)

def backwardCallBack():
    distance = getDistance()
    mip.distanceDrive(distance=-distance)

def leftCallBack():
    angle = getAngle()
    mip.turnByAngle(angle=-angle)

def rightCallBack():
    angle = getAngle()
    mip.turnByAngle(angle=angle)

def startSoundDialog():
    """
    Manage a sound dialog
    """


def updateLoop():
    """
    Top-level update loop.
    Called by Tk every 50ms
    Currenly just calls updateMovement to drive MiP in continuous drive mode,
    if applicable
    """
    updateMovement()
    root.after(50,updateLoop)

def updateMovement():
    """
    Called to read current pointer position from the movement canvas
    and drive MiP in continuous drive mode based on it's potision.
    If the magnitude of movement is small, leave MiP and do not drive him
    """
    # movementCanvas.positionX,movementCanvas.positionY, (-50 - 50)
    # movementCanvas.positionAngle,movementCanvas.positionMagnitude
    if movementCanvas.positionMagnitude > 10:
        forwardSpeed = int((-movementCanvas.positionY * 0x20)/50)
        turnSpeed = int((movementCanvas.positionX * 0x20)/50)
        logging.debug('updateMovement : forwardSpeed %d : turnSpeed %d' % (forwardSpeed,turnSpeed))
        mip.continuousDrive(forwardSpeed,turnSpeed)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='MiP Exploration GUI.')
    mippy.add_arguments(parser)
    args = parser.parse_args()
    logging.basicConfig(level=logging.DEBUG)
    gt = mippy.GattTool(args.adaptor, args.device)
    mip = mippy.Mip(gt)
    # start gui
    root = Tk()
    root.title("MiP Explorer GUI")
    root.geometry("600x300")
    logging.debug('main:1')

    menubar = Menu(root)
    fileMenu = Menu(menubar, tearoff=0)
    fileMenu.add_command(label="Exit", command=root.quit)
    windowMenu = Menu(menubar, tearoff=0)
    windowMenu.add_command(label="Sound", command=startSoundDialog)

    logging.debug('main:2')
    rootFrame = Frame(root)
    rootFrame.grid(column=0,row=1)
    
    logging.debug('main:3')
    # Fixed drive GUI
    fixedDriveFrame = Frame(rootFrame)
    fixedDriveFrame.grid(column=0,row=0)
    configFrame = Frame(fixedDriveFrame)
    configFrame.grid(column=0,row=0)

    logging.debug('main:4')
    labeld = Label(configFrame, text = "Distance(m):")
    labeld.grid(column=0,row=0)

    distanceStringVar = StringVar()
    distanceEntry = Entry(configFrame, textvariable = distanceStringVar)
    distanceEntry.insert(0,"0.1")
    distanceEntry.grid(column=1,row=0)

    labela = Label(configFrame, text = "Angle(deg):")
    labela.grid(column=0,row=1)

    angleStringVar = StringVar()
    angleEntry = Entry(configFrame, textvariable = angleStringVar )
    angleEntry.insert(0,"90")
    angleEntry.grid(column=1,row=1)

    controlFrame = Frame(fixedDriveFrame)
    controlFrame.grid(column=0,row=1)

    buttonf = Button(controlFrame, text="F", command=forwardCallBack)
    buttonf.grid(column=1,row=0)

    buttonb = Button(controlFrame, text="B", command=backwardCallBack)
    buttonb.grid(column=1,row=2)

    buttonl = Button(controlFrame, text="L", command=leftCallBack)
    buttonl.grid(column=0,row=1)

    buttonr = Button(controlFrame, text="R", command=rightCallBack)
    buttonr.grid(column=2,row=1)

    quitButton = Button(controlFrame, text='Quit', command=root.destroy)
    quitButton.grid(column=1,row=3)

    logging.debug('main:5')
    # movement canvas (continuous drive mode)
    movementCanvas = MovementCanvas(rootFrame,300,300)
    movementCanvas.canvas.grid(column=1,row=0)
    movementCanvas.setBindings()
#    movementCanvas.pack()


    logging.debug('main:6')
    root.after(50,updateLoop)
    logging.debug('main:7')
    root.mainloop()
