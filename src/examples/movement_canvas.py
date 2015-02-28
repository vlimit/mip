#!/usr/bin/env python
"""
MovementCanvas.
Presents a small canvas with a couple of circles in it. By pressing down the left hand button/clicking in the canvas
a representation of a direction/speed to move in can be returned.
Based on:
http://www.tutorialspoint.com/python/tk_canvas.htm
"""
import math
import Tkinter



class MovementCanvas:
    """
    MovementCanvas.
    Presents a small canvas with a couple of circles in it. By pressing down the left hand button/clicking
    in the canvas a representation of a direction/speed to move in can be returned.
    """
    buttonPressed = 0
    width = 0
    height = 0
    innerRadius = 10
    centreX = 0
    centreY = 0
    positionX = 0
    positionY = 0
    positionAngle = 0
    positionMagnitude = 0
    callbackList = []
    
    def __init__(self, parent,width=300,height=300):
        """
        Constructs canvas attached inside parent of specified width and height
        """
        self.canvas = Tkinter.Canvas(parent, bg="grey", height=height, width=width)
        self.width = width
        self.height = height
        self.innerRadius = 10
        self.centreX = (width/2)
        self.centreY = (height/2)
        self.outerOval = self.canvas.create_oval(10,10,width-10,height-10,fill="white")
        self.centreOval = self.canvas.create_oval(self.centreX-self.innerRadius,self.centreY-self.innerRadius,
                                                 self.centreX+self.innerRadius,self.centreY+self.innerRadius,
                                                                                fill="black")
        self.innerOval = self.canvas.create_oval(self.centreX-self.innerRadius,self.centreY-self.innerRadius,
                                                 self.centreX+self.innerRadius,self.centreY+self.innerRadius,
                                                                                fill="red")
        self.buttonPressed = 0
 
    def setBindings(self):
        """
        Add internal movement bindings to the canvas.
        """
        self.canvas.bind('<Button-1>',self.buttonPress)
        self.canvas.bind('<ButtonRelease-1>',self.buttonRelease)
        self.canvas.bind('<Motion>',self.motion)

    def pack(self):
        self.canvas.pack()
        
    def addUpdateCallback(self,callback):
        """
        Add a callback to the lsit of callbacks to be called on a movement
        Callbacks of the form:
        callback(positionX,positionY,positionAngle,positionMagnitude)
        Where:
        positionX and positionY are -50-50 based around the centre position.
        positionMagnitude is 0-50 based from the centre
        positionAngle is the angle in degrees, from the horizontal X axies increasing anti-clockwise.       
        """
        self.callbackList.append(callback)
    
    def motion(self,event):
        #print("Mouse position: (%s %s) : buttonPressed : %d " % (event.x, event.y,self.buttonPressed))
        if self.buttonPressed == 1:
            #print("Mouse position: (%s %s) Button is pressed" % (event.x, event.y))
            self.canvas.coords(self.innerOval,event.x-self.innerRadius,event.y-self.innerRadius,
                               event.x+self.innerRadius,event.y+self.innerRadius)
            self.updatePosition(event.x,event.y)
            return

    def updatePosition(self,eventX,eventY):
        """
        Update positionX/positionY/positionAngle/positionMagnitude variables based on event position
        (eventX,eventY)
        positionX and positionY are -50-50 based around the centre position.
        positionMagnitude is 0-50 based from the centre
        positionAngle is the angle in degrees, from the horizontal X axies increasing anti-clockwise.
        """
        # calculate position offset from centre, scaled to -50..50 based on with/height of widget
        self.positionX = ((eventX-self.centreX)*100)/self.width
        self.positionY = ((eventY-self.centreY)*100)/self.height
        # Distance from centre point (0-50)
        self.positionMagnitude = math.sqrt((self.positionX*self.positionX)+((self.positionY*self.positionY)))
        # Only calculate angle if we are away from the centre, otherwise angle is zero (division by zero)
        if self.positionMagnitude > 0.0:
            self.positionAngle = (math.acos(self.positionX/self.positionMagnitude)*180.0)/math.pi
            # If y position is positive(below centre in Y) make angle consistent
            if self.positionY > 0:
                self.positionAngle = 360.0 - self.positionAngle
        else:
            self.positionAngle = 0.0
        # call callbacks
        for fn in self.callbackList:
            fn(self.positionX,self.positionY,self.positionAngle,self.positionMagnitude)
        return

    def buttonPress(self,event):
        self.buttonPressed = 1
        print("Button Press at position: (%s %s) : buttonPressed : %d " % (event.x, event.y,self.buttonPressed))
        self.canvas.coords(self.innerOval,event.x-self.innerRadius,event.y-self.innerRadius,
                           event.x+self.innerRadius,event.y+self.innerRadius)
        self.updatePosition(event.x,event.y)
        return

    def buttonRelease(self,event):
        self.buttonPressed = 0
        print("Button Release : buttonPressed : %d " % (self.buttonPressed))
        return


def movement(x=0,y=0,angle=0.0,magnitude=0.0):
    print("Movement Callback: x = %d, y = %d, angle = %f, magnitude = %f " % (x,y,angle,magnitude))

def getLatest():
    print("After callback: x = %d, y = %d, angle = %f, magnitude = %f " % (movementCanvas.positionX,movementCanvas.positionY,movementCanvas.positionAngle,movementCanvas.positionMagnitude))
    top.after(50,getLatest)
    
if __name__ == '__main__':
    top = Tkinter.Tk()
    movementCanvas = MovementCanvas(top,300,300)
    movementCanvas.setBindings()
    movementCanvas.addUpdateCallback(movement)
    movementCanvas.pack()
    top.after(50,getLatest)
    top.mainloop()

