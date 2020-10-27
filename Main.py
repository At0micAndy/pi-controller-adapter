from evdev import InputDevice
from ButtonCodes import x360
from RetroControllers import MdPad
import _thread

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()
    
mdPad1 = MdPad()

########MAIN#########
_thread.start_new_thread(read_ctrl_input, ())
write_ctrl_output()
