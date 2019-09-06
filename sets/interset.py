x = {"Red","Green","Blue"}
y = {"Orange","green","White","Blue"}

z = x.intersection(y)
setz = x & y
setx = x ^ y
sety = x | y
print(z)
print(setz)
print(setx)
print(sety)

#set difference
setd = x - setz
print(setd)

#symmetric difference
c = x.symmetric_difference(y)
print(c)
