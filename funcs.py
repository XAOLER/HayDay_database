#!/usr/bin/env python
# -*- coding: utf-8 -*-

GoBack = 'Press "0" to go back'
goMany = 'Enter how many pieces:'
Cops = {}
item = 1
def cops_calculator(name_cops, cost):
    while int(item) > 0:
        global item
        item = input(goMany)
        pcs = (int(item) * (cost/10))
        print('{0}{1}{2}{3}{4}{5}{6}'.format('\n', name_cops, item, 'pcs. - ', int(pcs), ' Coins', '\n'))
        print(GoBack)

cops_calculator('corn ', 72)
