NEWTUPLE = ("apple", "pear", "apple")

# print(id(NEWTUPLE))
# print(type(NEWTUPLE))
# print(dir(NEWTUPLE))

# print(NEWTUPLE.count("apple"))
# print(NEWTUPLE.index("pear"))

NEWTUPLE = list(NEWTUPLE)
print(type(NEWTUPLE))
print(NEWTUPLE)

NEWTUPLE.append("cherry")
print(NEWTUPLE)

NEWTUPLE = tuple(NEWTUPLE)
print(type(NEWTUPLE))
print(NEWTUPLE)