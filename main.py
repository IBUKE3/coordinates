from structures import *


A = Point(1, 2, 1)
B = Point(3, 3, 3)
AB = generate_vector(A, B)
BA = generate_vector(B, A)
C = A + B
D = Point(0, 0, 1)
OD = D.radius_vector()
a = Vector(-5, -5, 0)
b = Vector(-1, 0, 0)
c = Vector(0, 0, 10)


alpha = Plane(1, 2, 3, 9)

A = Point(0, 0, 1)
B = Point(0, 1, 0)
C = Point(0, 0, 0)
beta = generate_plane_via_points(A, B, C)
print(beta.normal())
D = Point(3, 2, 1)
E = Point(2, 2, 2)
F = Point(0, 0, 0)
gamma = generate_plane_via_points(D, E, F)
print(beta)
print(gamma)
print(dist_point_plane(D, alpha))
