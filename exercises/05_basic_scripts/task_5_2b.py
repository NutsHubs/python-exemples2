#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

ip_mask = argv[1]+'/'+argv[2]

ip = ip_mask[:ip_mask.find('/')]
mask = ip_mask[(ip_mask.find('/')-len(ip_mask)):]
oct1, oct2, oct3, oct4 = ip.split('.')

bin_network = f'{int(oct1):08b}{int(oct2):08b}{int(oct3):08b}{int(oct4):08b}'[:int(mask.strip('/'))]
bin_network = f'{bin_network:0<32}'

mask_bin = format(2 ** int(mask.strip('/'))-1, 'b')
mask_bin = '{:0<32}'.format(mask_bin)

net_oct1 = bin_network[0:8]
net_oct2 = bin_network[8:16]
net_oct3 = bin_network[16:24]
net_oct4 = bin_network[24:]

mask_oct1 = mask_bin[0:8]
mask_oct2 = mask_bin[8:16]
mask_oct3 = mask_bin[16:24]
mask_oct4 = mask_bin[24:]

ip_out = f'Network:\n' \
         f'{int(net_oct1, 2)} {int(net_oct2, 2)} {int(net_oct3, 2)} {int(net_oct4, 2)}\n' \
         f'{bin_network[0:8]} {bin_network[8:16]} {bin_network[16:24]} {bin_network[24:]}\n' \
         f'\n' \
         f'Mask:\n' \
         f'{mask}\n' \
         f'{int(mask_oct1, 2):<8} {int(mask_oct2, 2):<8} {int(mask_oct3, 2):<8} {int(mask_oct4, 2):<8}\n' \
         f'{mask_oct1} {mask_oct2} {mask_oct3} {mask_oct4}'

print(ip_out)
