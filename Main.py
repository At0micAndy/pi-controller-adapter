#for reading from xbox controller
from evdev import InputDevice
from ButtonCodes import x360

#for reading from app
import blynklib

#used in main
import _thread
import os.path
from os import path

#for outputing signals
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

#for holding button values
from RetroControllers import MdPad
mdPad1 = MdPad()

def read_ctrl_input():
    
    xboxPad1 = InputDevice('/dev/input/event2')
        
    global mdPad1

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

    ###########BUTTONS###############
        #x -> a button, 01 is pressed, 00 is released
        if event.code == x360.x:
            if event.value:
                mdPad1.a = True
            else:
                mdPad1.a = False

        #a -> b button, 01 is pressed, 00 is released
        if event.code == x360.a:
            if event.value:
                mdPad1.b = True
            else:
                mdPad1.b = False

        #b -> c button, 01 is pressed, 00 is released
        if event.code == x360.b:
            if event.value:
                mdPad1.c = True
            else:
                mdPad1.c = False

        #start -> c button, 01 is pressed, 00 is released
        if event.code == x360.start:
            if event.value:
                mdPad1.start = True
            else:
                mdPad1.start = False
                
BLYNK_AUTH = 'edY5cMITGVUTFU8xOpZEznjcsGxHiiwd'

blynk = blynklib.Blynk(BLYNK_AUTH)

WRITE_EVENT_PRINT_MSG = "[WRITE_VIRTUAL_PIN_EVENT] Pin: V{} Value: '{}'"

def run_blink():
    while True:
        blynk.run()

@blynk.handle_event('write V7')
def write_virtual_pin_handler(pin, value):
    if value == ['1']:
        mdPad1.start = True
    else:
        mdPad1.start = False

@blynk.handle_event('write V5')
def write_virtual_pin_handler(pin, value):
    if value == ['1']:
        mdPad1.b = True
    else:
        mdPad1.b = False
        
@blynk.handle_event('write V3')
def write_virtual_pin_handler(pin, value):
    if value == ['-1']:
        mdPad1.right = True
        mdPad1.left = False
    elif value == ['1']:
        mdPad1.left = True
        mdPad1.right = False
    else:
        mdPad1.left = False
        mdPad1.right = False
        
@blynk.handle_event('write V1')
def write_virtual_pin_handler(pin, value):
    if value == ['-1']:
        mdPad1.down = True
        mdPad1.up = False
    elif value == ['1']:
        mdPad1.up = True
        mdPad1.down = False
    else:
        mdPad1.up = False
        mdPad1.down = False
            
def write_ctrl_output():
    
    #input_list = [7,11,12,13,15,18]
    #for pin in range(0,6):
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #select pin is only input
    
    while True:
    
        if mdPad1.up:
            GPIO.output(7, GPIO.LOW)
            print("up out")
        else:
            GPIO.output(7, GPIO.HIGH)
        
        if mdPad1.down:
            GPIO.output(11, GPIO.LOW)
            print("down out")
        else:
            GPIO.output(11, GPIO.HIGH)
        
        if mdPad1.left:
            GPIO.output(12, GPIO.LOW)
            print("left out")
        else:
            GPIO.output(12, GPIO.HIGH)
        
        if mdPad1.right:
            GPIO.output(13, GPIO.LOW)
            print("right out")
        else:
            GPIO.output(13, GPIO.HIGH)
        
        if mdPad1.b:
            GPIO.output(15, GPIO.LOW)
            print("b out")
        else:
            GPIO.output(15, GPIO.HIGH)

########MAIN#########
if path.exists('/dev/input/event2'):
    _thread.start_new_thread(read_ctrl_input, ())
else:
    _thread.start_new_thread(run_blink, ())
    
write_ctrl_output()