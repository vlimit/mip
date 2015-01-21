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

def getSpeed():
    speedString = speedEntry.get()
    speed = int(speedString)
    return speed

def forwardCallBack():
    distance = getDistance()
    mip.distanceDrive(distance=distance)

def backwardCallBack():
    distance = getDistance()
    mip.distanceDrive(distance=-distance)

def forwardRadarCallBack():
    speed = getSpeed()
    mip.continuousDriveForwardUntilRadar(speed=speed)

def leftCallBack():
    angle = getAngle()
    mip.turnByAngle(angle=-angle)

def rightCallBack():
    angle = getAngle()
    mip.turnByAngle(angle=angle)

def getVolume():
    volumeString = volumeEntry.get()
    volume = int(volumeString)
    return volume

def setVolume():
    volume = getVolume()
    mip.setVolume(volume)

def soundCallBack(soundNumber):
    mip.playSound(soundNumber)

def startSoundDialog():
    """
    Manage a sound control window
    """
    soundWindow = Toplevel(root)
    soundWindow.title("Sound Window")
    soundWindow.geometry("600x600")
    soundMenubar = Menu(soundWindow)
    soundFileMenu = Menu(soundMenubar, tearoff=0)
    soundFileMenu.add_command(label="Exit", command=soundWindow.destroy)
    soundMenubar.add_cascade(label="File", menu=soundFileMenu)
    soundWindow.config(menu=soundMenubar)
    soundFrame = Frame(soundWindow)
    soundFrame.pack()
    # Volume control
    volumeFrame = Frame(soundFrame)
    volumeFrame.pack()
    volumeButton = Button(volumeFrame, text = "Volume(0..7):", command = setVolume)
    volumeButton.grid(column=0,row=0)
    volumeStringVar = StringVar()
    volumeEntry = Entry(volumeFrame, textvariable = volumeStringVar)
    volumeEntry.insert(0,"1")
    volumeEntry.grid(column=1,row=0)
    # Add sounds
    soundsFrame1 = Frame(soundFrame)
    soundsFrame1.pack()
    button1 = Button(soundsFrame1, text ="Beep", command = lambda: soundCallBack(1))
    button1.pack(side = LEFT)
    button2 = Button(soundsFrame1, text ="Burp", command = lambda: soundCallBack(2))
    button2.pack(side = LEFT)
    button5 = Button(soundsFrame1, text ="Raspberry", command = lambda: soundCallBack(5))
    button5.pack(side = LEFT)
    button14 = Button(soundsFrame1, text ="Ah! (interested)", command = lambda: soundCallBack(14))
    button14.pack(side = LEFT)
    button15 = Button(soundsFrame1, text ="Ah! (disappointed)", command = lambda: soundCallBack(15))
    button15.pack(side = LEFT)
    button16 = Button(soundsFrame1, text ="Oh Yeah!", command = lambda: soundCallBack(16))
    button16.pack(side = LEFT)
    button17 = Button(soundsFrame1, text ="Meh", command = lambda: soundCallBack(17))
    button17.pack(side = LEFT)
    soundsFrame2 = Frame(soundFrame)
    soundsFrame2.pack()
    button19 = Button(soundsFrame2, text ="See yah", command = lambda: soundCallBack(19))
    button19.pack(side = LEFT)
    button20 = Button(soundsFrame2, text ="MiP chatter", command = lambda: soundCallBack(20))
    button20.pack(side = LEFT)
    button22 = Button(soundsFrame2, text ="Stop", command = lambda: soundCallBack(22))
    button22.pack(side = LEFT)
    button23 = Button(soundsFrame2, text ="Goodnight", command = lambda: soundCallBack(23))
    button23.pack(side = LEFT)
    button26 = Button(soundsFrame2, text ="Hi Yah!", command = lambda: soundCallBack(26))
    button26.pack(side = LEFT)
    button29 = Button(soundsFrame2, text ="Lets Go!", command = lambda: soundCallBack(29))
    button29.pack(side = LEFT)
    soundsFrame3 = Frame(soundFrame)
    soundsFrame3.pack()
    button32 = Button(soundsFrame3, text ="Eigh (something horrible)", command = lambda: soundCallBack(32))
    button32.pack(side = LEFT)
    button35 = Button(soundsFrame3, text ="Hellllooo", command = lambda: soundCallBack(35))
    button35.pack(side = LEFT)
    button36 = Button(soundsFrame3, text ="Bah?", command = lambda: soundCallBack(36))
    button36.pack(side = LEFT)
    button37 = Button(soundsFrame3, text ="Ohaye", command = lambda: soundCallBack(37))
    button37.pack(side = LEFT)
    button38 = Button(soundsFrame3, text ="Huh?", command = lambda: soundCallBack(38))
    button38.pack(side = LEFT)
    soundsFrame4 = Frame(soundFrame)
    soundsFrame4.pack()
    button39 = Button(soundsFrame4, text ="Mip Humming", command = lambda: soundCallBack(39))
    button39.pack(side = LEFT)
    button40 = Button(soundsFrame4, text ="Mip Humming", command = lambda: soundCallBack(40))
    button40.pack(side = LEFT)
    button41 = Button(soundsFrame4, text ="Mip Laughing", command = lambda: soundCallBack(41))
    button41.pack(side = LEFT)
    button42 = Button(soundsFrame4, text ="Heaaahhh", command = lambda: soundCallBack(42))
    button42.pack(side = LEFT)
    button43 = Button(soundsFrame4, text ="Harp sound", command = lambda: soundCallBack(43))
    button43.pack(side = LEFT)
    button44 = Button(soundsFrame4, text ="Lets MiP", command = lambda: soundCallBack(44))
    button44.pack(side = LEFT)
    soundsFrame5 = Frame(soundFrame)
    soundsFrame5.pack()
    button45 = Button(soundsFrame5, text ="MiP chatter", command = lambda: soundCallBack(45))
    button45.pack(side = LEFT)
    button46 = Button(soundsFrame5, text ="'kay", command = lambda: soundCallBack(46))
    button46.pack(side = LEFT)
    button47 = Button(soundsFrame5, text ="Music (verse 1)", command = lambda: soundCallBack(47))
    button47.pack(side = LEFT)
    button48 = Button(soundsFrame5, text ="Music (verse 2)", command = lambda: soundCallBack(48))
    button48.pack(side = LEFT)
    button49 = Button(soundsFrame5, text ="Out of power", command = lambda: soundCallBack(49))
    button49.pack(side = LEFT)
    button50 = Button(soundsFrame5, text ="Happy", command = lambda: soundCallBack(50))
    button50.pack(side = LEFT)

def startTelemetryDialog():
    """
    Manage a telemetry window
    """
# distance
# orientation
# battery level
# special quit/manage routine that sets flag queried in updateLoop to regularily update values

def startModeDialog():
    """
    Manage a mode changing window
    """
# move MiP in and out of computer control, allow selection of roam and music modes

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
    menubar.add_cascade(label="File", menu=fileMenu)
    windowMenu = Menu(menubar, tearoff=0)
    windowMenu.add_command(label="Sound", command=startSoundDialog)
    windowMenu.add_command(label="Telemetry", command=startTelemetryDialog)
    windowMenu.add_command(label="Mode", command=startModeDialog)
    menubar.add_cascade(label="Window", menu=windowMenu)
    root.config(menu=menubar)

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

    labels = Label(configFrame, text = "Speed(1-32):")
    labels.grid(column=0,row=2)

    speedStringVar = StringVar()
    speedEntry = Entry(configFrame, textvariable = speedStringVar )
    speedEntry.insert(0,"10")
    speedEntry.grid(column=1,row=2)

    controlFrame = Frame(fixedDriveFrame)
    controlFrame.grid(column=0,row=1)

    buttonf = Button(controlFrame, text="F", command=forwardCallBack)
    buttonf.grid(column=1,row=0)

    buttonf = Button(controlFrame, text="FR", command=forwardRadarCallBack)
    buttonf.grid(column=1,row=1)

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
