# -*- coding: utf-8 -*-
"""
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
result = False
ip_add_input = str()
ip_add_list = list()
final_result = {'unicast': False, 'multicast': False, 'local broadcast': False, 'unassigned': False, 'unused': True}

while not result:
    ip_add_input = input("To input ip address by format X.X.X.X: ")
    for oct in ip_add_input.split('.'):
        if not (oct.isdigit() and 0 <= int(oct) <= 255):
            print('IP address is wrong!')
            break
    else:
        for oct in ip_add_input.split('.'):
            ip_add_list.append(int(oct))
        result = True

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
