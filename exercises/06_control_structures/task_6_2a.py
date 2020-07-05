# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Сообщение должно выводиться только один раз.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

result = False
ip_add_list = list()
final_result = {'unicast': False, 'multicast': False, 'local broadcast': False, 'unassigned': False, 'unused': True}

ip_add_input = input("To input ip address by format X.X.X.X: ")

if len(ip_add_input.split('.')) == 4:
    for oct in ip_add_input.split('.'):
        if not (oct.isdigit() and 0 <= int(oct) <= 255):
            pass
    else:
        for oct in ip_add_input.split('.'):
            ip_add_list.append(int(oct))
        result = True
if not result:
    print('IP address is wrong!')
else:
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
