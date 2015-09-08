#!/usr/bin/env python
# -*- coding: utf-8 -*-

GoBack = 'Press "0" to go back'
goMany = 'Enter how many pieces:'
pcs_ = 'pcs.'
cost_ = 'cost'
coins = 'Coins'
item = 1
nameCop = {1: 'Wheat', 2: 'Corn', 3: 'Carrot', 4: 'Soybean',
           5: 'Sugarcane', 6: 'Rice', 7: 'Indigo', 8: 'Cotton',
           9: 'Pumpkin', 10: 'Lettuce', 11: 'Potato', 12: 'Chili',
           13: 'Tomato', 14: 'Strawberries'}

costCop = {'Wheat': 36, 'Corn': 72, 'Carrot': 72, 'Soybean': 108,
           'Sugarcane': 144, 'Rice': 188, 'Indigo': 252, 'Cotton': 288,
           'Pumpkin': 324, 'Lettuce': 324, 'Potato': 360, 'Chili': 360,
           'Tomato': 432, 'Strawberries': 504}
x = 1
while int(item) > 0:
    item = input(goMany)
    try:
        item = int(item)
        if x == 1:
            x -= 1
            name = (nameCop[item])
            cost = (costCop[name])
            print('{0}{1}: {2}{3}- {4} {5} {6}.'.format('\n', name, 10, 'pcs.', 'cost', cost, 'Coins'))
        pcs = (int(item) * (cost/10))
        print('{0}{1} {2}{3} - {4}{5}{6}'.format('\n', name, item, 'pcs.',  int(pcs), ' Coins', '\n'))
    except ValueError:
        print('mess_error')
    print(GoBack)
