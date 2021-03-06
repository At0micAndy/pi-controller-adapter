class MdPad:
    upZ = 7
    downY = 11
    leftX = 12
    rightMode = 13
    bA = 15
    select = 16
    cStart = 18
    
    def __init__(self):
        self.a = self.b = self.c = False
        self.x = self.y = self.z = False
        self.up = self.down = self.left = self.right = False
        self.start = self.mode = False
        
    def __str__(self):
        return  "Button states: a:% s b:% s c:% s x:% s y:% s z:% "\
                "s start:% s up:% s down:% s left:% s right:% s " %\
                (self.a, self.b, self.c, self.x, self.y, self.z, \
                 self.start, self.up, self.down, self.left, self.right)