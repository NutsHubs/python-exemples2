# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
vlan_in = input('To input VLAN number: ')
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
    if i[0] == int(vlan_in):
        print(f'{i[0]:<8}{i[1]:<17}{i[2]}')