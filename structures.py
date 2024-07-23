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


class Plane:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self) -> str:
        return str(self.a) +'*x + ' + str(self.b) + '*y + ' + str(self.c) + '*z + ' + str(self.d)

    def normal(self) -> Vector:
        return Vector(self.a, self.b, self.c)


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

def generate_plane_via_points(A: Point, B: Point, C: Point) -> Plane:
    v1 = generate_vector(A, B)
    v2 = generate_vector(A, C)
    n_alpha = cross_vectors(v1, v2)
    d = -(n_alpha.x * A.x + n_alpha.y * A.y + n_alpha.z * A.z)
    if d > 0:
        n_alpha = -n_alpha
        d = -d
    return Plane(n_alpha.x, n_alpha.y, n_alpha.z, d)


def angle_between_vector_and_plane(alpha: Plane, v: Vector) -> float:
    n = alpha.normal()
    return abs(90 - angle_between_vectors(n, v))

def angle_between_planes(alpha: Plane, beta: Plane) -> float:
    n1 = alpha.normal()
    n2 = beta.normal()
    return angle_between_vectors(n1, n2)

def dist_point_plane(A: Point, alpha: Plane) -> float:
    return abs(alpha.a * A.x + alpha.b * A.y + alpha.c * A.z + alpha.d)/(alpha.normal().length())