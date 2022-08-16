'''Задача 10. Сортировка
Что нужно сделать
Дан список из N чисел. Напишите программу, которая сортирует элементы списка по возрастанию и
выводит их на экран. Дополнительный список нельзя использовать.
Постарайтесь придумать и написать как можно более эффективный алгоритм сортировки.
Пример:
Изначальный список: [1, 4, -3, 0, 10]
Отсортированный список: [-3, 0, 1, 4, 10]
'''
# '''спасибо интернету'''
# star_list = [1, 4, -3, 0, 10]
# star_list.sort()
# print(star_list)
#
# '''типо я не смотрел инет'''
#
# star_list = [1, 4, -3, 0, 10]
# for i in star_list:
#     if i <= 0:
'''вообще тоже интернет, но пытался сам '''
def insertion_sort(nums):
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert

random_list_of_nums = [1, 4, -3, 0, 10]
insertion_sort(random_list_of_nums)
print(random_list_of_nums)