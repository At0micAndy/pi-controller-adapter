def write_ctrl_output():
    # input_list = [7,11,12,13,15,18]
    # for pin in range(0,6):
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # select pin is only input

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