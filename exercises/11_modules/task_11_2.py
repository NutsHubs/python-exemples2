# -*- coding: utf-8 -*-
"""
Задание 11.2

Создать функцию create_network_map, которая обрабатывает
вывод команды show cdp neighbors из нескольких файлов и объединяет его в одну общую топологию.

У функции должен быть один параметр filenames, который ожидает как аргумент список с именами файлов,
в которых находится вывод команды show cdp neighbors.

Функция должна возвращать словарь, который описывает соединения между устройствами.
Структура словаря такая же, как в задании 11.1:
    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}


Cгенерировать топологию, которая соответствует выводу из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt

В словаре, который возвращает функция create_network_map, не должно быть дублей.

С помощью функции draw_topology из файла draw_network_graph.py нарисовать схему на основании топологии,
полученной с помощью функции create_network_map.
Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg


При этом:
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Не копировать код функций parse_cdp_neighbors и draw_topology.

Ограничение: Все задания надо выполнять используя только пройденные темы.

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

"""

# эти заготовки написаны чтобы показать в какой момент должна
# рисоваться топология (после вызова функции)

from draw_network_graph import draw_topology

def create_network_map(filenames):
    result = dict()
    cdp_strings = ''
    cdp_chk = False
    device_orig = str()
    for file in filenames:
        with open(file) as t:
            cdp_strings += t.read()
    cdp_strings.strip()
    for string in cdp_strings.split('\n'):
        string.strip()
        if '>' in string:
            device_orig = string.split('>')[0]
            cdp_chk = False
        elif string.startswith('Device'):
            cdp_chk = True
        elif cdp_chk and string:
            str_lst = string.split()
            result[(device_orig, f'{str_lst[1]}{str_lst[2]}')] = (str_lst[0], f'{str_lst[-2]}'
                                                                              f'{str_lst[-1]}')
        else:
            continue
    for key in set(result.keys()).intersection(set(result.values())):
        if key in result.keys():
            value = result[key]
            del result[value]
    return result


if __name__ == "__main__":
    infiles = [
        "sh_cdp_n_sw1.txt",
        "sh_cdp_n_r1.txt",
        "sh_cdp_n_r2.txt",
        "sh_cdp_n_r3.txt",
    ]

    topology = create_network_map(infiles)
    # рисуем топологию:
    #draw_topology(topology)
    print(topology)
