# -*- coding: utf-8 -*-
"""
Задание 17.3a

Создать функцию generate_topology_from_cdp, которая обрабатывает вывод команды show cdp neighbor из нескольких файлов и записывает итоговую топологию в один словарь.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_filename - имя файла в формате YAML, в который сохранится топология.
 * значение по умолчанию - None. По умолчанию, топология не сохраняется в файл
 * топология сохраняется только, если save_to_filename как аргумент указано имя файла

Функция должна возвращать словарь, который описывает соединения между устройствами, независимо от того сохраняется ли топология в файл.

Структура словаря должна быть такой:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}},
 'R5': {'Fa 0/1': {'R4': 'Fa 0/1'}},
 'R6': {'Fa 0/0': {'R4': 'Fa 0/2'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.

Проверить работу функции generate_topology_from_cdp на списке файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Проверить работу параметра save_to_filename и записать итоговый словарь в файл topology.yaml.

"""
import re
import yaml


def generate_topology_from_cdp(list_of_files: list, save_to_filename=None):
    result = dict()
    regex_host = re.compile(r'(?P<host>\S+)>', re.DOTALL)
    regex_int = re.compile(r'(?P<r_device>\S+)\s+'
                           r'(?P<intf>\S+ \S+)\s+\d+.*?'
                           r'(?P<r_intf>\S+ \S+)\n', re.DOTALL)
    for file in list_of_files:
        with open(file) as f:
            str_file = f.read()
            host = regex_host.search(str_file).group('host')
            relation = dict()
            for match in regex_int.finditer(str_file):
                relation[match.group('intf')] = {match.group('r_device'): match.group('r_intf')}
            result[host] = relation
    if save_to_filename:
        with open(save_to_filename, 'w') as fw:
            yaml.dump(result, fw)
    return result


if __name__ == '__main__':
    files = ['sh_cdp_n_sw1.txt',
             'sh_cdp_n_r1.txt',
             'sh_cdp_n_r2.txt',
             'sh_cdp_n_r3.txt',
             'sh_cdp_n_r4.txt',
             'sh_cdp_n_r5.txt',
             'sh_cdp_n_r6.txt']
    print(generate_topology_from_cdp(files, 'topology.yaml'))
    pass
