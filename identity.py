i = "asdf"
j = "asdf"

print(id(i))
print(id(i) == id(j))
print(i == j)

i = 257
j = 257

print(id(i))
print("The variables i and j have the same identity: %s" % (id(i) == id(j)))

print('Now we will try a different way.')
print(f"The variables i and j have the same identity: {id(i) == id(j)}")
