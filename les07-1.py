class Matrix():
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for i in range(len(self.my_list)):
            for j in range(len(self.my_list[i])):
                print(self.my_list[i][j], end=' ')
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for j in range(len(other.my_list[i])):
                new_matrix = self.my_list.copy()
                new_matrix[i][j] = self.my_list[i][j] + other.my_list[i][j]
        return Matrix(new_matrix)


M = Matrix([[1, 2, 3], [4, 5, 6], [2, 4, 6]])
N = Matrix([[4, 5, 6], [1, 2, 3], [2, 4, 6]])

# print(M.my_list)
# print(N.my_list)
print(M+N)