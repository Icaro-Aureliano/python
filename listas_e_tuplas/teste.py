r2 = r3 = [1,2]#lista
r3.append(3)
print(id(r2))
print(id(r3))

r2 = r3 = 2#int
r3 = 3
print(r2)

print(".............................")


r2 = r3 = "123"#str
r3 = "222"
print(id(r2))
print(id(r3))

