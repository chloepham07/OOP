from week3.point import Point
import copy

class LineSegment:
    def __init__(self, *args):

        if len(args) == 0:
            self.__d1 = Point(8, 5)
            self.__d2 = Point(1, 0)

        elif len(args) == 2 and isinstance(args[0], Point) and isinstance(args[1], Point):
            self.__d1 = args[0]
            self.__d2 = args[1]

        elif len(args) == 4:
            self.__d1 = Point(args[0], args[1])
            self.__d2 = Point(args[2], args[3])

        elif len(args) == 1 and isinstance(args[0], LineSegment):
            S = args[0]
            self.__d1 = copy.deepcopy(S.__d1)
            self.__d2 = copy.deepcopy(S.__d2)

        else:
            raise ValueError("Invalid arguments")