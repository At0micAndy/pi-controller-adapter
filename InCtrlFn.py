#from evdev import InputDevice

def readDirBtn(event,btn,dirA,dirB):
    if event.code == btn:
        if event.value == -1:
            print(dirA)#debug
            dirA = True
            dirB = False
        elif event.value == 1:
            print(dirB)#debug
            dirA = False
            dirB = True
        elif event.value == 00:
            print("center")#debug
            dirA = False
            dirB = False
        else:
            print("Unrecognized D-pad value:",event.value)
        #print(mdPad1)#debug
        
def readPushBtn(event,inBtn,outBtn):
    if event.code == inBtn:
        if event.value == True:
            print(outBtn)#debug
            outBtn = True
        else:
            outBtn = False
        #print(mdPad1)#debug