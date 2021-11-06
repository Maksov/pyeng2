# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
"""
info = ospf_route.split(',')
ip = info[0].lstrip().split(' ')
ip.extend(info[1:])
ip.remove('via')
ip[1] = ip[1].strip('[').strip(']')
"""
ospf_route_info='''
Prefix              {}
AD/Metric           {}
Next-Hop            {}
Last update         {}
Outbound Interface  {}   
'''
with open('ospf.txt', 'r') as f:
    for line in f:
        info, lupdate, ointfr = line.split(',')
        info = info.split(' ')
        info.reverse()
        nhop, _, metric, prefix, *other = info
        metric = metric.strip('[').strip(']')
        print(ospf_route_info.format(prefix, metric, nhop, lupdate.lstrip(), ointfr.lstrip()))