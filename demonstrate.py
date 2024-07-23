from structures import *


A = Point(1, 1, 1)
B = Point(2, 1, 1)
C = Point(2, 2, 2)

print('\n------------------------')
print('   VECTOR OPERATIONS      ')
print('------------------------\n')

v = Vector(3, 1, 1)
AB = generate_vector(A, B)

print('C radius vector')
print(C.radius_vector())

print('AB vector: ' + str(AB))
print('v vector: ' + str(v))

print('Sum')
print(AB + v)

print('Division')
print(AB - v)

print('Vector-number multiplication')
print(AB * 5)

print('Negative vector')
print(-AB)

print('Vector v length')
print(v.length())

print('Scalar multiplication')
print(scalar(AB, v))

print('Cos between two vectors')
print(cos_between_vectors(AB, v))

print('Angle between two vectors')
print(angle_between_vectors(AB, v))

print('Vectornoe (cross) multiplication')
print(cross_vectors(AB, v))

cv = Vector(3, 2, 0)
print('cv vector: ' + str(cv))

print('Smeshannoe (mixed) multiplication')
print(mixed_vectors(AB, v, cv))

print('Volume of parallelepiped on 3 vectors')
print(volume_of_parallelepiped(AB, v, cv))

print('Volume of pyramid on 3 vectors')
print(volume_of_pyramid(AB, v, cv))


