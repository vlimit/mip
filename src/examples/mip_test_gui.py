#!/usr/bin/env python

"""
MiP Basic Test GUI.
To Use:
mip_test_gui.py -i hci0 -b D0:39:72:C4:7A:01
"""

from Tkinter import *
import mippy
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Basic MiP GUI.')
    mippy.add_arguments(parser)
    args = parser.parse_args()

    gt = mippy.GattTool(args.adaptor, args.device)

    mip = mippy.Mip(gt)
# roam whistle
#    mip.playSound(0x4d)

#    x=0
#    y=0
# https://www.youtube.com/watch?v=Qr60hWFyKHc
# https://www.youtube.com/watch?v=_1tTS638xUQ
# Create window
    root = Tk()
    root.title("MiP Control Panel")
    root.geometry("200x200")

    rootFrame = Frame(root)
    rootFrame.grid(column=0,row=0)

    configFrame = Frame(rootFrame)
    configFrame.grid(column=0,row=0)

    labeld = Label(configFrame, text = "Distance(m):")
    labeld.grid(column=0,row=0)

    distanceStringVar = StringVar()
    #distanceStringVar = "0.1"
    distanceEntry = Entry(configFrame, textvariable = distanceStringVar)
    distanceEntry.insert(0,"0.1")
    distanceEntry.grid(column=1,row=0)
    #distanceEntry.configure(text="1.0")
    #distanceEntry["text"] = "2.0"

    labela = Label(configFrame, text = "Angle(deg):")
    labela.grid(column=0,row=1)

    angleStringVar = StringVar()
    #angleStringVar = "90.0"
    angleEntry = Entry(configFrame, textvariable = angleStringVar )
    angleEntry.insert(0,"90")
    angleEntry.grid(column=1,row=1)
    #angleEntry.configure(text="1.0")
    #angleEntry["text"] = "2.0"

    controlFrame = Frame(rootFrame)
    controlFrame.grid(column=0,row=1)

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

    buttonf = Button(controlFrame, text="F", command=forwardCallBack)
    buttonf.grid(column=1,row=0)

    def backwardCallBack():
        distance = getDistance()
        mip.distanceDrive(distance=-distance)

    buttonb = Button(controlFrame, text="B", command=backwardCallBack)
    buttonb.grid(column=1,row=2)

    def leftCallBack():
        angle = getAngle()
        mip.turnByAngle(angle=-angle)

    buttonl = Button(controlFrame, text="L", command=leftCallBack)
    buttonl.grid(column=0,row=1)

    def rightCallBack():
        angle = getAngle()
        mip.turnByAngle(angle=angle)

    button9 = Button(controlFrame, text="R", command=rightCallBack)
    button9.grid(column=2,row=1)

    quitButton = Button(controlFrame, text='Quit', command=root.destroy)
    quitButton.grid(column=1,row=3)

# kick off GUI event loop
    root.mainloop()

