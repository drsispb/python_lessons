# 10.1.1
# for a in range (1,10):
#     for b in range (1,10):
#         print(a * b, end='\t')
#     print()
# 10.1.2

# numbers = int(input('Введите число N: '))
#
# for a in range (0, numbers + 1):
#     for b in range (0, numbers + 1):
#         print(a + b, end='\t')
#     print()
# 10.1.3
# numbers = int(input('Введите число N: '))
# for a in range (0, numbers + 1):
#     for b in range (0, numbers + 1):
#         print(a + (-b), end='\t')
#     print()

# 10.2

# size = int(input('Введите размер матрицы: '))
# for row in range (1, size + 1):
#     for col in range (1, size + 1):
#         if row % 2 == 0:
#             print(row, end = ' ')
#         else:
#             print(col, end =' ')
#     print()

# # 10.2.2
# size = int(input('Введите размер матрицы: '))
# for row in range (1, size + 1):
#     for col in range (1, size + 1):
#         if col % 3 == 0:
#             print(col, end = ' ')
#         else:
#             print(row, end =' ')
#     print()

# 10.2.3

# for row in range (20):
#     for col in range (50):
#         if row == 9:
#             print('-', end = '')
#         elif col == 24:
#             print('|', end='')
#         else:
#             print(' ', end='')
#     print()