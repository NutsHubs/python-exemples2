# -*- coding: utf-8 -*-
"""
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2': ('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

"""
import re


def get_ip_from_cfg2(file_name):
    result = dict()
    regex = re.compile(r'(?=\s+ip address ).*?'
                       r'(?P<ip>(?:\d{1,3}\.)+\d{1,3}) '
                       r'(?P<mask>(?:\d{1,3}\.)+\d{1,3})')
    with open(file_name) as f:
        interface = ip_mask = None
        for line in f:
            match_interface = re.search(r'interface (?P<interface>.*)$', line)
            match_ip = regex.search(line)
            if match_interface:
                interface = match_interface.group('interface')
            elif match_ip:
                ip_mask = match_ip.group('ip', 'mask')
            elif interface and ip_mask:
                result[interface] = ip_mask
                interface = ip_mask = None

    return result


def get_ip_from_cfg(file_name):
    result = dict()
    regex = re.compile(r'(?:interface (?P<interface>\S+))[^!]*'
                       r'(?:ip address (?P<ip>(?:\d{1,3}\.)+\d{1,3}) '
                       r'(?P<mask>(?:\d{1,3}\.)+\d{1,3}))',
                       re.DOTALL)
    with open(file_name) as f:
        for match_iter in regex.finditer(f.read()):
            interface = match_iter.group('interface')
            ip_mask = match_iter.group('ip', 'mask')
            result[interface] = ip_mask

    return result


if __name__ == '__main__':
    print(get_ip_from_cfg('config_r1.txt'))