import c4d
import random

#creates list of cooridnates
#x and y
last = [0,0]
lastRot = [0,0,0]

def createNewLink(head):
    posX = head.GetAbsPos().x
    posY = head.GetAbsPos().y
    link = c4d.BaseObject(5159)
    link.SetAbsPos(c4d.Vector(posX,posY,0))
    link[c4d.PRIM_CUBE_LEN] = c4d.Vector(10,10,10) * 10

    link.InsertUnder(doc.SearchObject("SnakeChild"))
    return link


#checks all the objects above the one holding this script.
#Then gets the children of the object with the chosen name
for i in doc.GetObjects():
    if(i.GetName() == "snake"):
        #returns a list
        snake = i.GetChildren()



def main():
    #VARIABLES ACCESSIBLE TO EVERYTHING#
    global last
    global snake
    global snakeX,snakeY
    global snakeRotX, snakeRotY,snakeRotZ
    global bait


    #creates bait if there aren't any'

    #VARIABLES ACCESSIBLE TO EVERYTHING#

    #sets the initial position of the controller
    inputObj = doc.SearchObject("Input")
    coordInput = inputObj.GetAbsPos()
    inputObj.SetAbsPos(c4d.Vector(0,0,0))
    #for rotation
    inputObj.SetAbsRot(c4d.Vector(0,0,0))
    snakeX = snake[0].GetAbsPos().x + last[0]
    snakeY = snake[0].GetAbsPos().y + last[1]
    snakeRotX = snake[0].GetAbsRot().x + lastRot[0]
    snakeRotY = snake[0].GetAbsRot().y + lastRot[1]
    snakeRotZ = snake[0].GetAbsRot().y = lastRot[2]

    #checks whether or not the arrow keys have been used
    if(coordInput.x != 0 or coordInput.y != 0):
        if(coordInput.x != 0):
            last[0] = (coordInput.x / abs(coordInput.x)) * 10
            last[1] = 0
            if(len(snake) < 10):
                snake.extend([createNewLink(snake[0])])
                c4d.EventAdd
            #print "moved along x"
            #keeps the positive and negative values stored
            #this avoids drifting and other problems related to movement values

            #does the same with rotation as the above
            lastRot[0] = (coordInput.x / abs(coordInput.x)) / 10
            lastRot[1] = 0
            lastRot[2] = (coordInput.x / abs(coordInput.x)) / 5
        elif(coordInput.y != 0):
            #print "moved along y"
            #keeps the positive and negative values stored
            #this avoids drifting and other problems related to movement values
            last[1] = (coordInput.y / abs(coordInput.y)) * 10
            last[0] = 0




    #variables for the initial position/rotation of the snake object


    #initializing position/rotation of the snake object
    #runs every frame allowing for constant movement
    snake[0].SetAbsPos(c4d.Vector(snakeX,snakeY,0))
    snake[0].SetAbsRot(c4d.Vector(snakeRotX,snakeRotY,snakeRotZ))
    #snake[0].SetAbsPos(c4d.Vector(snake[0].GetAbsPos().x + last[0], snake[0].GetAbsPos().y + last[1], 0))
    #for i in xrange(len(snake)):
        #if(i == len(snake)-1):
            #snake[0].SetAbsPos(c4d.Vector(snakeX,snakeY,0))
        #else:
            #inv = len(snake)-1-i
            #snake[inv].SetAbsPos(snake[inv-1]. GetAbsPos())