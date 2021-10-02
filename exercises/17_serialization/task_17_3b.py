# -*- coding: utf-8 -*-
"""
Задание 17.3b

Создать функцию transform_topology, которая преобразует топологию в формат подходящий для функции draw_topology.

Функция ожидает как аргумент имя файла в формате YAML, в котором хранится топология.

Функция должна считать данные из YAML файла, преобразовать их соответственно, чтобы функция возвращала словарь такого вида:
    {('R4', 'Fa 0/1'): ('R5', 'Fa 0/1'),
     ('R4', 'Fa 0/2'): ('R6', 'Fa 0/0')}

Функция transform_topology должна не только менять формат представления топологии, но и удалять дублирующиеся соединения (их лучше всего видно на схеме, которую генерирует draw_topology).

Проверить работу функции на файле topology.yaml (должен быть создан в задании 17.3a).
На основании полученного словаря надо сгенерировать изображение топологии с помощью функции draw_topology.
Не копировать код функции draw_topology.

Результат должен выглядеть так же, как схема в файле task_17_3b_topology.svg

При этом:
* Интерфейсы должны быть записаны с пробелом Fa 0/0
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме
* На схеме не должно быть дублирующихся линков


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

"""
import yaml
from draw_network_graph import draw_topology


def transform_topology(load_file_yaml: str):
    with open(load_file_yaml, 'r') as f:
        read_file = yaml.load(f, Loader=yaml.BaseLoader)
    dict_topology = dict(read_file)
    topology = dict()
    for host, intfs in dict_topology.items():
        for intf, r_device in intfs.items():
            r_device_tuple = tuple(*r_device.items())
            if not(r_device_tuple in topology):
                topology[(host, intf)] = r_device_tuple
    draw_topology(topology, 'topology.svg')
    return topology


if __name__ == '__main__':
    transform_topology('topology.yaml')
