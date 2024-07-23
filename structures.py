from math import acos, degrees


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if not isinstance(other, Point):
            raise ArithmeticError('The second object is not a Point')
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def display(self):
        print(self.x, self.y, self.z)

    def radius_vector(self):
        return Vector(self.x, self.y, self.z)


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return str([self.x, self.y, self.z])

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise ArithmeticError('The second object is not a Vector')
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise ArithmeticError('The second object is not a Vector')
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other, self.z * other)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Vector):
            raise ArithmeticError('The second object is not a Vector')
        return self.x == other.x and self.y == other.y and self.z == other.z

    def display(self) -> None:
        print(self.x, self.y, self.z)
        return None

    def length(self) -> float:
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5


def generate_vector(A: Point, B: Point) -> Vector:
    v = Vector(B.x-A.x, B.y-A.y, B.z-A.z)
    return v


def scalar(a: Vector, b: Vector) -> float:
    return a.x * b.x + a.y * b.y + a.z * b.z


def cos_between_vectors(a: Vector, b: Vector) -> float:
    return scalar(a, b) / (a.length() * b.length())


def angle_between_vectors(a: Vector, b: Vector) -> float:
    return degrees(acos(cos_between_vectors(a, b)))


def cross_vectors(a: Vector, b: Vector) -> Vector:
    x = a.y * b.z - a.z * b.y
    y = a.z * b.x - a.x * b.z
    z = a.z * b.y - a.y * b.x
    return Vector(x, y, z)


def mixed_vectors(a: Vector, b: Vector, c: Vector) -> float:
    return scalar(a, cross_vectors(b, c))


def volume_of_parallelepiped(a: Vector, b: Vector, c: Vector) -> float:
    return abs(mixed_vectors(a, b, c))


def volume_of_pyramid(a: Vector, b: Vector, c: Vector) -> float:
    return volume_of_parallelepiped(a, b, c) / 6
