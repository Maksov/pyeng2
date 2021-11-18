# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

table_mac = list()
with open('CAM_table.txt', 'r') as f:
    for line in f:
        str = line.split()
        if str and str[0].isdigit():
            vlan, mac, _, intrf = str
            str_mac = [int(vlan), mac, intrf]
            table_mac.append(str_mac)
            #print(f"{vlan:<9} {mac:<20} {intrf}")
            #print(str_mac)
table_mac.sort()
for str in table_mac:
    vlan, mac, intrf = str
    if vlan == 10:
        print(f"{vlan:<9} {mac:<20} {intrf}")