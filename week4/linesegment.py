from point import Point
import copy
class LineSegment:
    def __init__(self, *args):
        pass

        if len(args) == 0:
            self.__d1 = Point(8, 5)
            self.__d2 = Point(1, 0)

        elif len(args) == 2 and isinstance(args[0], Point) and isinstance(args[1], Point): 
            if isinstance(args[0], Point):
                self.__d1 = args[0]
                self.__d2 = args[1]

        elif len(args) == 4:
            self.__d1 = Point(args[0],args[1])
            self.__d2 = Point(args[2],args[3])

        elif len(args) == 1 and isinstance(args[0], LineSegment):
            S = args[0]
            self.d1 = Point(S.d1.x, S.d1.y)  
            self.d2 = Point(S.d2.x, S.d2.y)

        else:
            raise ValueError("Invalid arguments")