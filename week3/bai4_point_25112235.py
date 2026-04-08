import math
class Point:
    """represent a point in 2D space """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def symmetric(self):
        return Point(-self.x, -self.y)
    
    
if __name__ == "__main__":
    pointA = Point(3,4)
    print(f'Point A {pointA}')

    print('Enter coordinates for point B')
    pointB = Point( int(input('x: ')), int(input('y: ')))
    print(f'Point B {pointB}')

    pointC = pointB.symmetric()
    print(f'point C {pointC} ')

    pointO = Point(0,0)

    AB = pointA.distance_to(pointB)
    OB = pointO.distance_to(pointB)

    print(f'distance from B to O is {OB} ')
    print(f'distance from A to B is {AB} ')
