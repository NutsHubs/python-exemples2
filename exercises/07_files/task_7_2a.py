# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv
ignore = ["duplex", "alias", "Current configuration"]

file = argv[1]

with open(file) as f:
    for line in f.readlines():
        if not line.startswith('!'):
            for i in ignore:
                if line.find(i) != -1:
                    break
            else:
                print(line.strip('\n'))

