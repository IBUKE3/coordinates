from structures import *


A = Point(1, 2, 1)
B = Point(3, 3, 3)
AB = generate_vector(A, B)
BA = generate_vector(B, A)
C = A + B
print(C)
D = Point(0, 0, 1)
OD = D.radius_vector()
a = Vector(-5, -5, 0)
b = Vector(-1, 0, 0)
c = Vector(0, 0, 10)
print(cross_vectors(a, b))
print(mixed_vectors(a, b, c))
print(volume_of_pyramid(a, b, c))
