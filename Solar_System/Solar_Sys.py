import c4d
import math
import random

#Welcome to the world of Python
suns = []
orbits = []
planets = []
clones = []

for i in doc.GetObjects():
    if(i.GetName() == "Sun"):
        suns = i
    if(i.GetName() == "Orbit"):
        orbits = i
    if(i.GetName()== "Planet"):
        planets = i
    if(i.GetName() == "Cloned"):
        clones = i

def Sun():
    global sun
    sun = c4d.BaseObject(5160)
    sun.SetAbsPos(c4d.Vector(0,0,0))
    #sun.SetAbsScale(c4d.Vector(200,200,200))
    sun.SetName("Sun")
    doc.InsertObject(sun)
    return sun

def Orbit ():
    global orbit
    rotX = int(random.uniform(-45,45))
    rotY = int(random.uniform(-45,45))
    rotZ = int(random.uniform(-45,45))
    orbit = c4d.BaseObject(5140)
    orbit.SetAbsPos(c4d.Vector(0,0,0))
    orbit.SetAbsRot(c4d.Vector(rotX,rotY,rotZ))
    orbit.SetName("Orbit")
    orbit.InsertUnder(doc.SearchObject("Sun"))
    return orbit


def Planet():
    global planet
    #getting position of the orbit to which it is parented
    orbPos = orbit.GetAbsPos()
    #random ints for position addition
    rand1 = int(random.uniform(-1000,1000))
    rand2 = int(random.uniform(-1000,1000))
    #variables using orbit position
    x = orbPos.x
    y = orbPos.y
    z = orbPos.z
    #random rotations for initial planet orientation
    rotX = int(random.uniform(-45,45))
    rotY = int(random.uniform(-45,45))
    rotZ = int(random.uniform(-45,45))
    #randoms for scale

    planet = c4d.BaseObject(5161)
    planet.SetAbsPos(c4d.Vector(x+rand1,y,z +rand2))
    planet.SetAbsRot(c4d.Vector(rotX, rotY, rotZ))

    planet.InsertUnder(doc.SearchObject("Orbit"))

    return planet

def Clone():
    rotX = int(random.uniform(-45,45))
    rotY = int(random.uniform(-45,45))
    rotZ = int(random.uniform(-45,45))
    sun = doc.SearchObject("Sun")
    orbit = doc.SearchObject("Orbit")
    clone = orbit.GetClone()
    clone.SetAbsPos(c4d.Vector(0,0,0))
    clone.SetAbsRot(c4d.Vector(rotX,rotY,rotZ))
    clone.SetName("Cloned")
    clone.InsertUnder(sun)
    
    return clone
def main():
    frame = doc.GetTime().GetFrame(doc.GetFps())
#making initial objects
    while(len(suns) < 1):
        suns.extend([Sun()])
        c4d.EventAdd
    while(len(orbits) < 1):
        orbits.extend([Orbit()])
        c4d.EventAdd
    while(len(planets) < 1):
        planets.extend([Planet()])
        c4d.EventAdd

#making clones
    while(len(clones) < 8):
        clones.extend([Clone()])
        c4d.EventAdd


#Rotating Orbits
    for x in range(len(orbits)):
        rot = orbits[x].GetRelRot()
        change = math.sin(0.03)
        rot.x += change
    orbits[x].SetRelRot(c4d.Vector(rot.x,0,0))
#Rotating Clones
    for x in range(len(clones)):
        rot1 = clones[x].GetRelRot()
        change1 = math.sin(0.03)
        rot1.x += change1
    clones[x].SetRelRot(c4d.Vector(rot1.x,0,0))