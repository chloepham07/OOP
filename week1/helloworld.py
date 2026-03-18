import math
class Point :
    """represent a point in 2D space """
    x= int
    y= int
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return('(%d,%d)%(self.x,self,y)')
    
    def read(self):
        self.x = int(input('nhap x: '))
        self.y = int(input('nhap y: '))

    def distance(self, point):
        d= math.sqrt ((self.x - point.x)**2+ (self.y-point.y)**2)
        return d
    
diemA = Point(3,4)
print(diemA)




