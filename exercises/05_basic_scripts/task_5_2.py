# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_mask = input('Enter IP address by format A.B.C.D/MASK: ')

ip = ip_mask[:ip_mask.find('/')]
mask = ip_mask[(ip_mask.find('/')-len(ip_mask)):]
oct1, oct2, oct3, oct4 = ip.split('.')

mask_bin = format(2 ** int(mask.strip('/'))-1, 'b')
mask_bin = '{:0<32}'.format(mask_bin)

mask_oct1 = mask_bin[0:8]
mask_oct2 = mask_bin[8:16]
mask_oct3 = mask_bin[16:24]
mask_oct4 = mask_bin[24:]

ip_out = f'Network:\n' \
         f'{oct1:8} {oct2:8} {oct3:8} {oct4:8}\n' \
         f'{int(oct1):08b} {int(oct2):08b} {int(oct3):08b} {int(oct4):08b}\n' \
         f'\n' \
         f'Mask:\n' \
         f'{mask}\n' \
         f'{int(mask_oct1, 2):<8} {int(mask_oct2, 2):<8} {int(mask_oct3, 2):<8} {int(mask_oct4, 2):<8}\n' \
         f'{mask_oct1} {mask_oct2} {mask_oct3} {mask_oct4}'

print(ip_out)