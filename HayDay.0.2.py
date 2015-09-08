#!/usr/bin/env python
# -*- coding: utf-8 -*-

lang_sel = '''
Нажміть клавішу "1" і кнопку "Enter" щоб вибрати українську мову
Press key "2" and press "Enter" to select English language
'''
lang = input(lang_sel)

if lang == '1':
    from langUA import *

else:
    from langEN import *

print(Start_Mess)
input(go)
while True:
    print(select_mode, '\n')
    item = input(conty)       # select section
    if item == '1':     # Simple mode
        while True:
            print(contents)  # contents simple mode
            item = input(conty)
            if item == '0' or item == '00':
                break
            try:
                item = int(item)
                print(content[item])
            except ValueError:
                print('\n', mess_error, '\n')
            input(conty)
    elif item == '2':   # Advanced mode
        while True:
            print(contents)
            item = input(conty)
            if item == '1':      # calculator for cops
                while True:
                    print(select_cops)
                    item = input(conty)
                    x = 1
                    while int(item) > 0:
                        item = input(goMany)
                        try:
                            item = int(item)
                            if x == 1:
                                x -= 1
                                name = (nameCop[item])
                                cost = (costCop[name])
                                print('{0}{1}: {2}{3}- {4} {5} {6}.'.format('\n', name, 10, pcs_, cost_, cost, coins))
                            pcs = (int(item) * (cost/10))
                            print('{0}{1} {2}{3} - {4}{5}{6}'.format('\n', name, item, pcs_,  int(pcs), coins, '\n'))
                        except ValueError:
                            print('mess_error')
                        print(GoBack)
                        if item == 0:
                            break
            if item == '2':     # calculator for Trees and Bush
                while True:
                    print(TreesBush)
                    item = input(conty)
                    if item == '1':
                        while int(item) > 0:
                            print()
                    elif item == '0':
                        break
            if item == '3':    # calculator for products
                while True:
                    Products1 = ('''
                    1.Chicken egg''')
            elif item == '00':
                break
    print('bb')
