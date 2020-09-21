# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import argparse
import ipaddress
import subprocess


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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script check IP addresses')
    parser.add_argument('ip', nargs='+', help='IP addresse(s) by format a.b.c.d')
    args = parser.parse_args()

    ipaddress_list = checkipaddr(args.ip)

    #print(ping_ip_addresses(ipaddress_list))
