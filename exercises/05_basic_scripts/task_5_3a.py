# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

interfaces_template = {
    "access": [
        'interface {}\n'
        ''+str(access_template)
        .strip('[]')
        .replace("'", '')
        .replace(', ', '\n'),
        'To write VLAN number: '
    ],
    "trunk": [
        'interface {}\n'
        ''+str(trunk_template)
        .strip('[]')
        .replace("'", '')
        .replace(', ', '\n'),
        'To write trunk allowed vlan(s): '
    ]
}

mode = input('To write mode of interface is working(access/trunk): ')
num = input('To write type and number of interface: ')
vlans = input(interfaces_template.get(mode)[1])

print(interfaces_template.get(mode)[0].format(num, vlans))
