#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == "__main__":
    n = int(input("Общее кол-во учеников = "))
    m = int(input("Кол-во мальчиков = "))
    d = n-m
    sm = 0
    sd = 0
    rm = list(map(float, input('Рост мальчиков: ').split()))
    rd = list(map(float, input('Рост девочек: ').split()))
    if len(rm) == m:
        for i, item in enumerate(rm):
            sm += item
    else:
        print(
            'Неверное кол-во',
            file=sys.stderr
        )
    if len(rd) == d:
        for i, item in enumerate(rd):
            sd += item
    else:
        print(
            'Неверное кол-во',
             file = sys.stderr
        )
    r_sr_m = sm / m
    r_sr_d = sd / d
    print('Средний рост мальчиков: {:.1f}\nСредний рост девочек: {:.1f}'.format(r_sr_m, r_sr_d))