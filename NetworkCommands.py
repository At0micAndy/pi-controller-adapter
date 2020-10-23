import blynklib
import RPi.GPIO as GPIO

up = 7
down = 11
left = 12
right = 13
b = 15
start = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(up, GPIO.OUT)
GPIO.setup(down, GPIO.OUT)
GPIO.setup(left, GPIO.OUT)
GPIO.setup(right, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)
GPIO.setup(start, GPIO.OUT)

BLYNK_AUTH = 'edY5cMITGVUTFU8xOpZEznjcsGxHiiwd'

blynk = blynklib.Blynk(BLYNK_AUTH)

WRITE_EVENT_PRINT_MSG = "[WRITE_VIRTUAL_PIN_EVENT] Pin: V{} Value: '{}'"

@blynk.handle_event('write V7')
def write_virtual_pin_handler(pin, value):
    if value == ['1']:
        GPIO.output(start, GPIO.LOW)
    else:
        GPIO.output(start, GPIO.HIGH)

@blynk.handle_event('write V5')
def write_virtual_pin_handler(pin, value):
    if value == ['1']:
        GPIO.output(b, GPIO.LOW)
    else:
        GPIO.output(b, GPIO.HIGH)
        
@blynk.handle_event('write V3')
def write_virtual_pin_handler(pin, value):
    if value == ['1']:
        GPIO.output(up, GPIO.LOW)
    elif value == ['-1']:
        GPIO.output(down, GPIO.LOW)
    else:
        GPIO.output(up, GPIO.HIGH)
        GPIO.output(down, GPIO.HIGH)
        
@blynk.handle_event('write V1')
def write_virtual_pin_handler(pin, value):
    if value == ['1']:
        GPIO.output(right, GPIO.LOW)
    elif value == ['-1']:
        GPIO.output(left, GPIO.LOW)
    else:
        GPIO.output(right, GPIO.HIGH)
        GPIO.output(left, GPIO.HIGH)
      
while True:
    blynk.run()