a = (1, 2, 3)
print(type(a))

ab = (1, 2, 3, 4, 4, 5, 4, 3) # its allow duplicates
print(ab[4]) # access through index

ab = (1, 2, 3, 4, 4, 5, 4, 3, 3.3, print("hello"), "Hello") # its also hetrogenous nature

# tupple ke uppar two types of traverse
for i in ab: # here not will access index
    print(i)

for i in range(len(ab)):
    print(i) # here we access the index value 
    print(ab[i]) # access all value in tuples

# print(dir(tuple))
# index 
index = ab.index(4)
print(index)

# count
print(ab.count(3))

af = (1, ) # give a comma to pack to make tupple 
print(type(af)) # tupple

# tupple unpacking
ac,b,c,d,e= (1, 2, 3, 4, 5)
print(c)

ad = (1) # unpack tupple 
print(type(ad)) # int 