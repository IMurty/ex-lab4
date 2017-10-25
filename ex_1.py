#!/usr/bin/env python3
import librip.gens as gens


def print_list(lst):
    print(' ,'.join(map(str, lst)))


goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'},
    {'title': None, 'price': None, 'color': None},
    {'color': 'white'},
]

res_list = []

for item in gens.field(goods, 'title', 'price'):
    res_list.append(item)
print_list(res_list)

print_list([i for i in gens.gen_random(1, 3, 5)])

