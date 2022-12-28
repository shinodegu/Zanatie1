a1 = (1,2,3,4)
a2 = (1,2,3,4)
a3 = (1,2,3,4)

print(type(a1), id(a1))
print(type(a2), id(a2))
print(type(a3), id(a3))

z1 = [1,2,3,4]
z2 = [1,2,3,4]

print(type(z1), id(z1))
print(type(z2), id(z2))

a1 = list(a1)
a2 = list(a2)
a3 = list(a3)

print(type(a1), id(a1))
print(type(a2), id(a2))
print(type(a3), id(a3))


z1 = bool(z1)
z2 = bool(z2)
z1 == z2
True
z1 is z2
True

print(type(z1), id(z1))
print(type(z2), id(z2))

