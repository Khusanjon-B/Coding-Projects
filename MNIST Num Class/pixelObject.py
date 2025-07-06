class pixelObject():
    
    def __init__(self, width, height, x, y, value = 0):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.value = value
    
    def center(self):
        return [self.x + self.width / 2, self.y + self.height / 2]
    
    def getValue(self):
        return self.value
    
    def getRectangle(self):
        return (self.x, self.y, self.width, self.height)
    
    def hover(self, x, y):
        
        if (self.x <= x <= self.x + self.width) and (self.y <= y <= self.y + self.height):
            self.value = 1
        # elif (abs(self.center()[0] - x) <= self.width) and (abs(self.center()[1] - y) <= self.height) and self.value != 1:
            # self.value = 0.2
