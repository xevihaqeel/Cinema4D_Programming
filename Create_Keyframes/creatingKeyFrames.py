import c4d
#Welcome to the world of Python


def main():
    pass  #put in your code here
    
    #Get userdata for object: record
    onOff = op[c4d.ID_USERDATA, 1]
    print "onOff: ", onOff
    #Get time/frame
    curTime = doc.GetTime()
    curFrame = curTime.GetFrame(24)
    print"curFrame: ", curFrame
    
    #Set frame
    
    #get object for which to set keyframe
    if onOff:
        obj = doc.GetActiveObject()
        print "obj: ", obj
        
        trck = obj.FindCTrack(c4d.PRIM_CONE_BRAD)
        if not trck: 
            trck = c4d.CTrack (obj, c4d.PRIM_CONE_BRAD)
            obj.InsertTrackSorted (trck)
        curve = trck.GetCurve()
        keyDict = curve.AddKey(c4d.BaseTime(curFrame, 24))
        
        
        #actually adds the ky
        trck.FillKey(doc,obj, keyDict["key"])
        c4d.EventAdd()
        #actually adds the key
        c4d.CallCommand(12147) #command for updating screen
        op[c4d.ID_USERDATA,1] = False