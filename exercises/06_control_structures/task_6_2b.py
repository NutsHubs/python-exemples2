# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
result = False
ip_add_list = list()
final_result = {'unicast': False, 'multicast': False, 'local broadcast': False, 'unassigned': False, 'unused': True}

while not result:
    ip_add_input = input("To input ip address by format X.X.X.X: ")

    if len(ip_add_input.split('.')) == 4:
        for oct in ip_add_input.split('.'):
            if not (oct.isdigit() and 0 <= int(oct) <= 255):
                break
        else:
            for oct in ip_add_input.split('.'):
                ip_add_list.append(int(oct))
            result = True
            break

    print('IP address is wrong!')


if ip_add_list[0] == 0 or ip_add_list[0] == 255:
    final_result['local broadcast'], final_result['unassigned'] = True, True
    for ip_oct in ip_add_list:
        if ip_oct == 0 and final_result['unassigned']:
            final_result['local broadcast'] = False
        elif ip_oct == 255 and final_result['local broadcast']:
            final_result['unassigned'] = False
        else:
            final_result['local broadcast'], final_result['unassigned'] = False, False
            break
elif 1 <= ip_add_list[0] <= 223:
    final_result['unicast'] = True
elif 224 <= ip_add_list[0] <= 239:
    final_result['multicast'] = True

for out, state in final_result.items():
    if state:
        print(out)
        break
