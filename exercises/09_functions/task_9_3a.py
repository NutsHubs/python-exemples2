# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


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
        interface, mode, vlans = str(), str(), str('1')
        mode_chk = False
        for line_config in config_file.readlines():
            line_config = line_config.strip()
            if line_config.startswith('interface'):
                interface = line_config.split()[1]
                continue
            elif line_config.startswith('switchport mode'):
                mode = line_config.split()[-1]
                mode_chk = True
                continue
            elif (line_config.startswith('switchport access vlan') or
                  line_config.startswith('switchport trunk allowed')):
                vlans = line_config.split()[-1]

            if mode_chk:
                if mode == 'access':
                    access[interface] = int(vlans)
                else:
                    trunk[interface] = [int(vlan) for vlan in vlans.split(',')]
                mode_chk = False
                vlans = str('1')

        result = (access, trunk)
    return result


print(get_int_vlan_map('config_sw2.txt'))
