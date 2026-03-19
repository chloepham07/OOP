import math
from point import Point

class Circle:
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

    def __str__(self):
        return f"Circle(center=({self.center.x},{self.center.y}), radius={self.radius})"

def point_in_circle(circle: Circle, point: Point) -> bool:
    distance = math.sqrt((point.x - circle.center.x)**2 + (point.y - circle.center.y)**2)   
    return distance <= circle.radius

class Rect:
    def __init__(self, corner: Point, width: float, height: float):
        self.corner = corner
        self.width = width
        self.height = height

        self.bottom_left = Point(corner.x, corner.y)
        self.bottom_right = Point(corner.x + width, corner.y)
        self.top_left = Point(corner.x, corner.y + height)
        self.top_right = Point(corner.x + width, corner.y + height)

def rect_in_circle(circle: Circle, rect: Rect) -> bool:
    return (
        point_in_circle(circle, rect.bottom_left) and
        point_in_circle(circle, rect.bottom_right) and
        point_in_circle(circle, rect.top_left) and
        point_in_circle(circle, rect.top_right)
    )

def rect_circle_overlap(circle: Circle, rect: Rect) -> bool:
    closest_x = max(rect.bottom_left.x, min(circle.center.x, rect.top_right.x))
    closest_y = max(rect.bottom_left.y, min(circle.center.y, rect.top_right.y))
        
    closest_point = Point(closest_x,closest_y)
    return point_in_circle(circle,closest_point)
if __name__ == '__main__':
    center = Point(150, 100)
    my_circle = Circle(center, 75)

    point = Point(150, 150)

    corner = Point(80, 70)
    my_rect = Rect(corner, 75, 90)
    print(my_circle)
    print("Point in circle:", point_in_circle(my_circle, point))
    print("Rect in circle:", rect_in_circle(my_circle, my_rect))
    print("Rect overlaps circle:", rect_circle_overlap(my_circle, my_rect))