import math


class Point:
    def __init__(self, x, y=None, polar=False):
        if isinstance(x, Point):
            self.x = x.x
            self.y = x.y
        else:
            if polar is False:
                self.x = x
                self.y = y
            else:
                self.x = x * math.cos(y)
                self.y = x * math.sin(y)

    def __str__(self):
        return str((self.x, self.y))

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def dist(self, x=None, y=None):
        if y:
            other_x = x
            other_y = y
        elif x:
            other_x = x.x
            other_y = x.y
        else:
            other_x = 0
            other_y = 0
        return math.hypot(other_x - self.x, other_y - self.y)


class Vector(Point):

    def __init__(self, a, b=None, c=None, d=None):
        if b is None:
            if isinstance(a, Point):
                self.x = a.x
                self.y = a.y
            elif isinstance(a, tuple):
                self.x = a[0]
                self.y = a[1]
            elif isinstance(a, Vector):
                self.x = a.x
                self.y = a.y
        elif c is None:
            if isinstance(a, tuple):
                self.x = b[0] - a[0]
                self.y = b[1] - a[1]
            elif isinstance(a, Point):
                self.x = b.x - a.x
                self.y = b.y - a.y
            else:
                self.x = a
                self.y = b
        else:
            self.x = c - a
            self.y = d - b

    def lenght(self):
        return math.hypot(self.x, self.y)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y

    def __mul__(self, other):
        return self.dot_product(other)

    def cross_product(self, other):
        return self.x * other.y - self.y * other.x

    def __xor__(self, other):
        return self.cross_product(other)

    def mul(self, other):
        self.x *= other
        self.y *= other

    def __rmul__(self, other):
        return Vector(self.x * other, self.y * other)

    def angle(self, other):
        return math.degrees(math.acos(self.dot_product(other)/other.lenght()/self.lenght()))


class Circle:
    def __init__(self, radius, pointx, pointy=None):
        self.r = radius
        if pointy is None:
            self.x = pointx.x
            self.y = pointx.y
        else:
            self.x = pointx
            self.y = pointy

    def len_full(self):
        return 2 * self.r * math.pi

    def len_part(self, x1, y1, x2, y2):
        if self.r == 0:
            return 0
        else:
            v1 = Vector(self.x, self.y, x1, y1)
            v2 = Vector(self.x, self.y, x2, y2)
            angle = math.degrees(math.acos(v1.dot_product(v2) / v1.lenght() / v2.lenght()))
            return angle / 360 * self.len_full()