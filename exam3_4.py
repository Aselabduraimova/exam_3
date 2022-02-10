a = [1, 5, 3, 8, 6, 2]
b = [3, 7, 3, 4, 5, 9, 1, 9]

c = set(a) & set(b)
print(c)

result_list = [i for i in a if i in b]
print(result_list)