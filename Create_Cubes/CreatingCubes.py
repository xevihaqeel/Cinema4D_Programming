import c4d
import math
import random
#cubes = [20,0]


for i in doc.GetObjects():
    if(i.GetName() == "Objects"):
        cubes = i.GetChildren()
def makeMaterial():
    mat = c4d.BaseMaterial(5703)
    mat[c4d.ID_BASELIST_NAME] = "Material"
    doc.InsertMaterial(mat)

    mat[c4d.MATERIAL_COLOR_COLOR] = c4d.Vector(1,1,1)
    tag = cube.MakeTag(c4d.Ttexture)
    tag[c4d.TEXTURETAG_MATERIAL] = mat 
    
def makeCube():
    global cube
    global mat
    randomX = int(random.uniform(-200,200))
    randomY = int(random.uniform(-200,200))
    randomZ = int(random.uniform(-200,200))

    rotX = int(random.uniform(-45,45))
    rotY = int(random.uniform(-45,45))
    rotZ = int(random.uniform(-45,45))
    cube = c4d.BaseObject(5166)


    cube.InsertUnder(doc.SearchObject("Objects"))
    cube.SetAbsPos(c4d.Vector(randomX,randomY,randomZ))
    cube.SetAbsRot(c4d.Vector(rotX,rotY,rotZ))
    
    
def moveThings():
    things = doc.SearchObject("Figure")
    thingsPos = things.GetRelPos()
    change = math.sin(frame/10.0)*10
    thingsPos.y += change
    things.SetRelPos(c4d.Vector(thingsPos.x,thingsPos.y,thingsPos.z))

def main():
    global cubes
    global frame
    global randomX,randomY
    while(len(cubes) < 40):
        cubes.extend([makeCube()])
        c4d.EventAdd
    frame = doc.GetTime().GetFrame(doc.GetFps())
    for x in range(len(cubes)):

        #rotating the shits
        rot = cubes[x].GetAbsRot()
        change = math.sin(0.03)
        rot.y += change
        cubes[x].SetAbsRot(c4d.Vector(rot.x,rot.y,rot.z))
        for y in range(len(cubes)):
            #moving the shits
            pos = cubes[y].GetRelPos()
            change = math.sin(frame/10) * 2
            change2 = math.cos(frame/10) * 2 
            pos.x += change 
            pos.y += change2
            pos.z += math.sin(20)
            #cubes[x].SetRelPos(c4d.Vector(0,pos.y,0))