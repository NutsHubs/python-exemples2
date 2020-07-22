# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def get_int_vlan_map(config_filename):
    """
    :param config_filename:
    :return: tuple(access{}, trunk{})
    """
    result = tuple()
    with open(config_filename) as config_file:
        access, trunk = dict(), dict()
        interface, mode, vlans = str(), str(), str()
        vlans_chk, mode_chk = False, False
        for line_config in config_file.readlines():
            line_config = line_config.strip()
            if (vlans_chk and mode_chk):
                if mode == 'access':
                    access[interface] = int(vlans)
                else:
                    trunk[interface] = [int(vlan) for vlan in vlans.split(',')]
                vlans_chk, mode_chk = False, False
            if line_config.startswith('interface'):
                interface = line_config.split()[1]
                continue
            elif (line_config.startswith('switchport access vlan') or
                  line_config.startswith('switchport trunk allowed')):
                vlans = line_config.split()[-1]
                vlans_chk = True
                continue
            elif line_config.startswith('switchport mode'):
                mode = line_config.split()[-1]
                mode_chk = True
                continue
        result = (access, trunk)
    return result


print(get_int_vlan_map('config_sw1.txt'))
