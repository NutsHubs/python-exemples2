# -*- coding: utf-8 -*-
"""
Задание 12.3


Создать функцию print_ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые переданы ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.


Для этого задания нет тестов
"""

import argparse
import ipaddress
import subprocess
from  tabulate import tabulate


def checkipaddr(ip):
    result = list()
    try:
        for ip in args.ip:
            result.append(ipaddress.ip_address(ip))
    except ValueError as e:
        print('Wrong ip addresse(s). Enter correct ip addresse(s)')
        raise SystemExit
    return result


def ping_ip_addresses(ip_list):
    success = list()
    wrong = list()

    for ip in ip_list:
        reply = subprocess.run(['ping', str(ip), '-c', '4'], stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, encoding='utf-8')
        if reply.returncode == 0:
            success.append(str(ip))
        else:
            wrong.append(str(ip))

    result = (success, wrong)

    return result


def print_ip_table(reachable_list, unreachable_list):

    length_reach = len(reachable_list)
    length_unreached = len(unreachable_list)

    reach_col = list(reachable_list)
    unreached_col = list(unreachable_list)

    if length_reach > length_unreached:
        diff = length_reach - length_unreached
        diff_list = [' ']*diff
        unreached_col.extend(diff_list)
    elif length_unreached > length_reach:
        diff = length_unreached - length_reach
        diff_list = [' '] * diff
        reach_col.extend(diff_list)

    print(tabulate(zip(reach_col, unreached_col), ['reachable', 'unreachable'], ))

    print(reachable_list, unreachable_list)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script check IP addresses')
    parser.add_argument('ip', nargs='+', help='IP addresse(s) by format a.b.c.d')
    args = parser.parse_args()

    #ipaddress_list = checkipaddr(args.ip)
    #pinged_addresses = ping_ip_addresses(ipaddress_list)
    #print(pinged_addresses)
    print_ip_table(['10.1.1.1', '10.1.1.2'], ['12.1.1.1', '12.1.1.2', '12.1.1.3'])
