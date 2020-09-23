# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список, где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список IP-адресов и/или диапазонов IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последний октет адреса.

Функция возвращает список IP-адресов.


Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""

import argparse
import ipaddress
import subprocess


def check_ip_address(ip):
    result = list()
    try:
        for ip in args.ip:
            result.append(ipaddress.ip_address(ip))
    except ValueError as e:
        print('Wrong ip addresse(s). Enter correct ip addresse(s)', e)
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


def convert_ranges_to_ip_list(ip_list):
    """
    Convert ranges ip addresses
    by format a.b.c.d-a.b.c.n
    or a.b.c.d-n
    in list of particular ip addresses
    """
    result = list()

    for ip_range in ip_list:
        a = int(str(ip_range).find('-'))
        if a > 1:
            ip_range_split = str(ip_range).split('-')
            if ip_range_split[1].count('.') == 3:
                rangestart, rangestop = ip_range_split[0].split('.')[3], \
                                        ip_range_split[1].split('.')[3]
            else:
                rangestart, rangestop = ip_range_split[0].split('.')[3], \
                                        ip_range_split[1]

            ipstart = ip_range_split[0][:ip_range_split[0].rfind('.') + 1]
            for ipiter in range(int(rangestart), int(rangestop) + 1):
                result.append("{}{}".format(ipstart, ipiter))
        else:
            result.append(ip_range)

    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script check IP addresses')
    parser.add_argument('ip', nargs='+', help='IP addresse(s) by format a.b.c.d or range a.b.c.d-n or a.b.c.d-a,b,c,n')
    args = parser.parse_args()

    args.ip = ['10.1.1.1', '10.4.10.10-13', '192.168.1.12-192.168.1.15']


    print(convert_ranges_to_ip_list(args.ip))


    #ipaddress_list = check_ip_address(ip_list)

    #print(ping_ip_addresses(ipaddress_list))
