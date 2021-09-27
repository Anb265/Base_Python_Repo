from functools import reduce
# new_list = [i for i in range(100, 1001, 2)]
#
# def multi(a,b):
#     return a*b
#
# print(reduce(multi, new_list))

print(reduce(lambda a, b: a * b, [i for i in range(100, 1001, 2)]))
