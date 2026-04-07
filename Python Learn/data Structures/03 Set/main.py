a = {1, 2, 3, 4, 5, 5, 4} # does not store duplicates
print(a)
# print(a[0]) # sets are unordered


# hash function in sets & sets are un ordered 

b = hash("hello")
print(b)

ab = {1, 2, 3, 8, "hello", 9, 4, 5, 5, 4}
for i in ab:
    print(i)

# methods

c = {1, 2, 3, 4, 5, 5, 4}
# c.remove(2)

# c.pop()
c.clear()
print(c)



# perfrom betn two sets

A = {1, 2, 3}
B = {3, 4, 5}

# union = A.union(B)
# print(union)
# print(A|B) # union

# intersection = A.intersection(B)
# intersection = A & B
# print(intersection) # which parts is comman

# diffrence = A.difference(B)
# diffrence = B.difference(A)
# diffrence = A - B
# diffrence = B - A
# print(diffrence)

# symmetric_diffrence = A.symmetric_difference(B)
# symmetric_diffrence = A ^ B
# print(symmetric_diffrence)# remove comman part 

# compound Operation
B-= A
print(B)