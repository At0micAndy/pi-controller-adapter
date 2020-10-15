from ButtonCodes import x360
from evdev import InputDevice

xboxPad1 = InputDevice('/dev/input/event2')

#debug
print(xboxPad1)

class MdPad:
    def __init__(self):
        self.a = self.b = self.c = False
        self.x = self.y = self.z = False
        self.up = self.down = self.left = self.right = False
        self.start = False
        
    def __str__(self):
        return  "Button states: a:% s b:% s c:% s x:% s y:% s z:% "\
                "s start:% s up:% s down:% s left:% s right:% s " %\
                (self.a, self.b, self.c, self.x, self.y, self.z, \
                 self.start, self.up, self.down, self.left, self.right)
    
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
    if event.code == x360.xBtn:
        if event.value == True:
            print("a")#debug
            mdPad1.a = True
        else:
            mdPad1.a = False
        print(mdPad1)
        
    #a -> b button, 01 is pressed, 00 is released
    if event.code == x360.aBtn:
        if event.value == True:
            print("b")#debug
            mdPad1.b = True
        else:
            mdPad1.b = False
        print(mdPad1)
        
    #b -> c button, 01 is pressed, 00 is released
    if event.code == x360.bBtn:
        if event.value == True:
            print("c")#debug
            mdPad1.c = True
        else:
            mdPad1.c = False
        print(mdPad1)
