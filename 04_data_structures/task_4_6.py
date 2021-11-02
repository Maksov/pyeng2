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

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

info = ospf_route.split(',')
ip = info[0].lstrip().split(' ')
ip.extend(info[1:])
ip.remove('via')
ip[1] = ip[1].strip('[').strip(']')
ospf_route_info='''
Prefix              {}
AD/Metric           {}
Next-Hop            {}
Last update         {}
Outbound Interface  {}   
'''
print(ospf_route_info.format(ip[0],ip[1],ip[2],ip[3].lstrip(),ip[4].lstrip()))

