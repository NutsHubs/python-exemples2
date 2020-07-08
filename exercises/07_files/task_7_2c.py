# -*- coding: utf-8 -*-
"""
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
from sys import argv
ignore = ["duplex", "alias", "Current configuration"]

file_read = argv[1]
file_write = argv[2]

with open(file_read) as f:
    for line in f.readlines():
        for i in ignore:
            if line.find(i) != -1:
                break
        else:
            with open(file_write, 'a') as a:
                a.write(line)

