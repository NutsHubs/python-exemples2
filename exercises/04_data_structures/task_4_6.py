# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

ospf_route = ospf_route.replace(',', '')
arg_ospf = ospf_route.strip().split(' ')
arg_ospf.remove('via')

prefix, metric, nexthop, update, outbound = arg_ospf
metric = str(metric).strip('[]')

out_ospf = f"Prefix                 {prefix}\n" \
           f"AD/Metric              {metric}\n" \
           f"Next-Hop               {nexthop}\n" \
           f"Last update            {update}\n" \
           f"Outbound Interface     {outbound}"

print(out_ospf)


print(arg_ospf)