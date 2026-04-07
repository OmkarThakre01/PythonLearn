# 1
# d1 = {1:10, 2:20, 3:30}
# d2 = {4:40, 5:50, 6:60}

# for i in d2:
#     d1[i] = d2[i]
# print(d1)

# 2
# d1 = {1:10, 2:20, 3:30}
# sum = 0

# for i in d1:
#     sum = sum + d1[i]
# print(sum)


# 3

# l = [1, 1, 2, 3, 2, 1, 3, 3, 3, 4, 4, 3]

# d={}

# for i in l:
#     if i in d.keys():
#         d[i] = d[i] + 1
#     else:
#         d[i] = 1
# print(d)


# 4
d1 = {1:10, 2:20, 4:30}
d2 = {4:40, 5:50, 6:60}

for i in d2:
    if i in d1.keys():
        d1[i] = d1[i] + d2[i]
    else:
        d1[i] = d2[i]
print(d1)