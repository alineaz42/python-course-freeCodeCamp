import random
# x = 1+2**3/4*5
# print(x)
# print(type(x))


# l = [i for i in range(1, 100)]
# # print(l)
# l2 = [i for i in l[1::2]]
# # print(l2)
# for i in l2:
#     # if i != 0:
#     #     l2.insert(i, 0)
#     print(i)
# print(l2)


# def randomNumber():

# for i in l:
#     total = sum(l)
#     global ave
#     ave = total/len(l)

#     if i < 25:
#         #     print(i)
#         # # print(ave)
#         l[i] = ave
# print(l)
# print(ave)
l = []
for i in range(1, 10):
    x = random.randint(1, 50)
    l.append(x)
total = sum(l)
ave = total/len(l)
# print(l)
for i in l:

    if i <= 25:
        l[i] = ave
print(l, len(l))
