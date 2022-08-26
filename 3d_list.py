a = 1
b = 1
c = 2
n = 3
my_3d_list = [[i, j, k] for i in range(0, a+1) for j in range(0, b+1) for k in range(0, c+1) if (i+j+k) != n]
print(my_3d_list)