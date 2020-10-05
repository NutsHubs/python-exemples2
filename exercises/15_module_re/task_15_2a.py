# -*- coding: utf-8 -*-
"""
Задание 15.2a

Создать функцию convert_to_dict, которая ожидает два аргумента:
* список с названиями полей
* список кортежей со значениями

Функция возвращает результат в виде списка словарей, где ключи - взяты из первого списка,
а значения подставлены из второго.

Например, если функции передать как аргументы список headers и список
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up')]

Функция должна вернуть такой список со словарями:
[{'interface': 'FastEthernet0/0', 'address': '10.0.1.1', 'status': 'up', 'protocol': 'up'},
 {'interface': 'FastEthernet0/1', 'address': '10.0.2.1', 'status': 'up', 'protocol': 'up'}]

Проверить работу функции:
* первый аргумент - список headers
* второй аргумент - результат, который возвращает функция parse_sh_ip_int_br из задания 15.2, если ей как аргумент передать sh_ip_int_br.txt.

Функцию parse_sh_ip_int_br не нужно копировать.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
from task_15_2 import parse_sh_ip_int_br

headers = ["interface", "address", "status", "protocol"]


def convert_to_dict(list_name, list_values):
    result = list()
    temp_dict = dict()
    for values in list_values:
        for (header, value) in zip(list_name, values):
            temp_dict[header] = value
        result.append(temp_dict)
        temp_dict = dict()
    return result


if __name__ == '__main__':
    print(convert_to_dict(headers, parse_sh_ip_int_br('sh_ip_int_br.txt')))