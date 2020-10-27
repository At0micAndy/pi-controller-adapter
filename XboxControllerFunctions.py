def read_ctrl_input():
    try:
        xboxPad1 = InputDevice('/dev/input/event2')
    except:
        print("No controller")
        return

    global mdPad1

    #################D-PAD###########################
    for event in xboxPad1.read_loop():
        # left/right d-pad, -1 means left, 1 means right
        if event.code == x360.leftRight:
            if event.value == -1:
                print("left")  # debug
                mdPad1.left = True
                mdPad1.right = False
            elif event.value == 1:
                print("right")  # debug
                mdPad1.left = False
                mdPad1.right = True
            elif event.value == 00:
                print("center")  # debug
                mdPad1.left = False
                mdPad1.right = False
            else:
                print("Unrecognized L/R D-pad value:", event.value)

        # up/down d-pad, -1 means up, 1 means down
        if event.code == x360.upDown:
            if event.value == -1:
                print("up")  # debug
                mdPad1.up = True
                mdPad1.down = False
            elif event.value == 1:
                print("down")  # debug
                mdPad1.up = False
                mdPad1.down = True
            elif event.value == 00:
                print("level")  # debug
                mdPad1.up = False
                mdPad1.down = False
            else:
                print("Unrecognized D/U D-pad value:", event.value)

        ###########BUTTONS###############
        # x -> a button, 01 is pressed, 00 is released
        if event.code == x360.x:
            if event.value:
                print("a")  # debug
                mdPad1.a = True
            else:
                mdPad1.a = False

        # a -> b button, 01 is pressed, 00 is released
        if event.code == x360.a:
            if event.value:
                print("b")  # debug
                mdPad1.b = True
            else:
                mdPad1.b = False

        # b -> c button, 01 is pressed, 00 is released
        if event.code == x360.b:
            if event.value:
                print("c")  # debug
                mdPad1.c = True
            else:
                mdPad1.c = False

        # start -> c button, 01 is pressed, 00 is released
        if event.code == x360.start:
            if event.value:
                print("start")  # debug
                mdPad1.start = True
            else:
                mdPad1.start = False