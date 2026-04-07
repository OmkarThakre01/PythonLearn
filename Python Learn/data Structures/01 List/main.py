a = [12, 13, 14, 15, 16]
# a = [12, 13, 14, 15, 16, 34.2, True, print()]

# print(a[1])
# print(a[0:5:1])
# print(a[-1])
# print(a[-2])


# 1st way using index

# for i in range(len(a)):
#     print(a[i])


# 2nd way directly on values 

# for i in a:
#     print(i) # draw back we does not access the index


# print(dir(list))

# help(list)


a.append(24)
print(a)

a.insert(0, 11)
print(a)

a.extend([17, 18, 19])
print(a)

a.remove(24)
print(a)

hello = a.pop(3)
print(hello)
print(a)


hello = [10, 20, 30, 40, 50, 60]
index = hello.index(40)
print(index)


val = [1, 2, 3, 2, 4, 2, 5, 6, 7, 8]
count = val.count(2)
print(count)


# val.sort()
# val.reverse()
# copy =  val.copy()
# print(copy)
val.clear()
print(val)


l = [1, 2, 3, 4, 5, 6, 7]
l[0] = 12
print(l)


