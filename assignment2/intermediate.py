def multiplication_table(number):
    outer_list = []
    for i in range(1, number + 1):
        outer_list.append([i * j for j in range(1, i + 1)])
    return outer_list
print(multiplication_table(3))
