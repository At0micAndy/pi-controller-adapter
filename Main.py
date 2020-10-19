from evdev import InputDevice
from ButtonCodes import x360
from RetroControllers import MdPad

xboxPad1 = InputDevice('/dev/input/event2')
    
mdPad1 = MdPad()

#################D-PAD###########################
for event in xboxPad1.read_loop():
    #left/right d-pad, -1 means left, 1 means right
    if event.code == x360.leftRight:
        if event.value == -1:
            print("left")#debug
            mdPad1.left = True
            mdPad1.right = False
        elif event.value == 1:
            print("right")#debug
            mdPad1.left = False
            mdPad1.right = True
        elif event.value == 00:
            print("center")#debug
            mdPad1.left = False
            mdPad1.right = False
        else:
            print("Unrecognized L/R D-pad value:",event.value)
        print(mdPad1)

    #up/down d-pad, -1 means up, 1 means down
    if event.code == x360.upDown:
        if event.value == -1:
            print("up")#debug
            mdPad1.up = True
            mdPad1.down = False
        elif event.value == 1:
            print("down")#debug
            mdPad1.up = False
            mdPad1.down = True
        elif event.value == 00:
            print("level")#debug
            mdPad1.up = False
            mdPad1.down = False
        else:
            print("Unrecognized D/U D-pad value:",event.value)
        print(mdPad1)
    
###########BUTTONS###############
    #x -> a button, 01 is pressed, 00 is released
    if event.code == x360.x:
        if event.value == True:
            print("a")#debug
            mdPad1.a = True
        else:
            mdPad1.a = False
        print(mdPad1)
        
    #a -> b button, 01 is pressed, 00 is released
    if event.code == x360.a:
        if event.value == True:
            print("b")#debug
            mdPad1.b = True
        else:
            mdPad1.b = False
        print(mdPad1)
        
    #b -> c button, 01 is pressed, 00 is released
    if event.code == x360.b:
        if event.value == True:
            print("c")#debug
            mdPad1.c = True
        else:
            mdPad1.c = False
        print(mdPad1)

    #start -> c button, 01 is pressed, 00 is released
    if event.code == x360.start:
        if event.value == True:
            print("c")#debug
            mdPad1.start = True
        else:
            mdPad1.start = False
        print(mdPad1)
