from evdev import InputDevice
from ButtonCodes import x360
from RetroControllers import MdPad

xboxPad1 = InputDevice('/dev/input/event2')    
mdPad1 = MdPad()

def readDirBtn(btn,dirA,dirB):
    #left/right d-pad, -1 means left, 1 means right
    if event.code == btn:
        if event.value == -1:
            print(dirA)#debug
            mdPad1.dirA = True
            mdPad1.dirB = False
        elif event.value == 1:
            print(dirB)#debug
            mdPad1.dirA = False
            mdPad1.dirB = True
        elif event.value == 00:
            print("center")#debug
            mdPad1.dirA = False
            mdPad1.dirB = False
        else:
            print("Unrecognized D-pad value:",event.value)
        print(mdPad1)
        
def readPushBtn(inBtn,outBtn):
    if event.code == inBtn:
        if event.value == True:
            print(outBtn)#debug
            mdPad1.outBtn = True
        else:
            mdPad1.outBtn = False
        print(mdPad1)#debug

#################MAIN###########################
for event in xboxPad1.read_loop():
    
    #read D-pad
    readDirBtn(x360.leftRight,"left","right")
    readDirBtn(x360.upDown,"up","down")
    
    #read Buttons
    readPushBtn(x360.x,'a')
    readPushBtn(x360.a,'b')
    readPushBtn(x360.b,'c')
    readPushBtn(x360.lb, 'x')
    readPushBtn(x360.rb, 'y')
    readPushBtn(x360.y, 'z')
    readPushBtn(x360.start, 'start')

