# -*- coding: utf-8 -*-
"""
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN

В результате должен получиться такой вывод:
10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9

Обратите внимание на vlan 1000 - он должен выводиться последним.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
macs = list()

with open('CAM_table.txt', 'r') as f:
    for line in f.readlines():
        line_list = line.strip().split(' ')
        out_list = list()
        new_line = str()
        for sp in range(len(line_list)):
            if line_list[sp] != '':
                out_list.append(line_list[sp])

        else:
            if out_list and out_list[0].isdigit() :
                new_line = f'{out_list[0]:<8}{out_list[1]:<17}{out_list[3]}'
                out_list.remove('DYNAMIC')
                out_list[0] = int(out_list[0])
                macs.append(out_list)

macs.sort()

for i in macs:
    print(f'{i[0]:<8}{i[1]:<17}{i[2]}')
