#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 19:16:44 2022

@author: konstantinx
"""


print('Задача 1')
my_list = [1, 2, 3, 4, 'sdakjgvh', (1, 2), None, True]
for i in my_list:
    print(type(i))

print('Задача 2')
my_list = []
list_length = int(input('введите длинну списка: '))
for i in range(list_length):
    my_list.append(input('введите элемент списка: '))
print(my_list)
if list_length % 2 == 1:
    last_thing = my_list.pop(-1)
my_list[::2], my_list[1::2] = my_list[1::2], my_list[::2]
if list_length % 2 == 1:
    my_list.append(last_thing)
print(my_list)
#half_list1 = my_list[::2]
#half_list2 = my_list[1::2]
#new_list = []
# for i in range(len(half_list1)):
#    try:
#        new_list.append(half_list2[i])
#    except IndexError:
#        pass
#    new_list.append(half_list1[i])
# print(new_list)

#print('Задача 3')
# year = {'winter': [12, 1, 2], 'spring': [3, 4, 5],
#        'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
#x = int(input('введите месяц в формате числа 1..12: '))
# for i in year:
#    if x in year.get(i):
#        print(i)

#print('Задача 4')
#words = input('введите несколько слов: ')
#split_words = words.split()
# for i, el in enumerate(split_words):
#    print(i+1, el[:10])

print('Задача 5')
my_list = [7, 5, 3, 3, 2]
rate = int(input('введите натуральное число: '))
for i, el in enumerate(my_list):
    if rate > el:
        index = i
        break
    elif i == len(my_list)-1:
        index = i+1
my_list.insert(index, rate)
print(my_list)
