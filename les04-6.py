from itertools import count, cycle
from sys import argv

# а) итератор, генерирующий целые числа, начиная с указанного

# for i in count(int(argv[1])):
#     print(i)
#     if i==10:
#         break

# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

counter = 0
for i in cycle(argv[1:]):
    print(i)
    if counter > 15:
        break
    counter += 1