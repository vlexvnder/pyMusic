import os
currdir = os.path.dirname(os.path.realpath(__file__))

def getDict(mypath = currdir):
    #mypath = "C:\\Users\\Andrew\\Documents\\code"
    onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))] #get a list of files in the folder


    notedict = {}

    for i in onlyfiles:                             #create a dict with key of note name and value of path
        notedict[i.split('.')[0]] = mypath + i
    return notedict
