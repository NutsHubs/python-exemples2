# -*- coding: utf-8 -*-
"""
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv
ignore = ["duplex", "alias", "Current configuration"]

file = argv[1]

with open(file) as f:
    for line in f.readlines():
        for i in ignore:
            if line.find(i) != -1:
                break
        else:
            with open('config_sw1_cleared.txt', 'a') as a:
                a.write(line)

