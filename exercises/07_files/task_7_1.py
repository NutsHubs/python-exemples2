# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
template_info = [
    'Prefix                 {}',
    'AD/Metric              {}',
    'Next-Hop               {}',
    'Last update            {}',
    'Outbound Interface     {}'
]

with open('ospf.txt') as f:
    for line in f.readlines():
        line_list = line.replace(',', '').replace('via ', '')\
            .replace('[', '').replace(']', '')\
            .strip('\n').split(' ')
        line_list.reverse()
        info_out_list = template_info
        for i in range(5):
            print(info_out_list[i].format(line_list[4-i]))
        else:
            print()

