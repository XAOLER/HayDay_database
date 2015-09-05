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
    item = input(conty)
    if item == '1':
        while True:
            print(contents)
            item = input(conty)
            if item == '00': break
            item = int(item)
            while item >= 0 & item <= 9:
                print(content[item])
                break
            input(contb)
    elif item == '2':
        while True:
            print(contents)
            print(oth)
            item = input(conty)
            if item == '1':
                while True:
                    print(cop)
                    item = input(conty)
                    if item == '1':
                        print('Wheat:10pcs. -  cost 36g.')
                        while int(item) > 0:
                            item = input('Enter how many pieces:')
                            pcs = (int(item) * (36/10))
                            print('')
                            print('{}{}{}{}{}'.format('Wheat:', item, 'pcs. - ', int(pcs), ' Coins'))
                            print ('')
                            print ('Press "0" to go back ')
                    elif item == '2' :
                        print ('Corn: 10pcs. - cost 72g.')
                        while int(item) > 0 :
                            item = input ('Enter how many pieces:')
                            pcs = (int(item) * (72/10))
                            print('')
                            print ('{}{} {}{}{}'.format('Corn:',item,'pcs. - ',int(pcs),' Coins'))
                            print ('')
                            print ('Press "0" to go back ')
                    elif item == '3' :
                        print ('Carrot: 10pcs. - cost 72g.')
                        while int(item) > 0 :
                            item = input ('Enter how many pieces:')
                            pcs = (int(item) * (72/10))
                            print('')
                            print ('{}{} {}{}{}'.format('Carrot:',item,'pcs. - ',int(pcs),' Coins'))
                            print ('')
                            print ('Press "0" to go back ')
                    elif item == '4' :
                        print ('Soybean: 10pcs. - cost 108g.')
                        while int(item) > 0 :
                            item = input ('Enter how many pieces:')
                            pcs = (int(item) * (108/10))
                            print('')
                            print ('{}{} {}{}{}'.format('Soybean:',item,'pcs. - ',int(pcs),' Coins'))
                            print ('')
                            print ('Press "0" to go back ')
                    elif item == '5' :
                        print ('Sugarcane: 10pcs. - cost 144g.')
                        while int(item) > 0 :
                            item = input ('Enter how many pieces:')
                            pcs = (int(item) * (144/10))
                            print('')
                            print ('{}{} {}{}{}'.format('Sugarcane:',item,'pcs. - ',int(pcs),' Coins'))
                            print ('')
                            print ('Press "0" to go back ')
                    elif item == '6' :
                        print ('Rice: 10pcs. - cost 188g.')
                        while int(item) > 0 :
                            item = input ('Enter how many pieces:')
                            pcs = (int(item) * (188/10))
                            print('')
                            print ('{}{} {}{}{}'.format('Rice:',item,'pcs. - ',int(pcs),' Coins'))
                            print ('')
                            print ('Press "0" to go back ')
                    elif item == '7' :
                        print ('Indigo: 10pcs. - cost 252g.')
                        while int(item) > 0 :
                            item = input ('Enter how many pieces:')
                            pcs = (int(item) * (252/10))
                            print('')
                            print ('{}{} {}{}{}'.format('Indigo:',item,'pcs. - ',int(pcs),' Coins'))
                            print ('')
                            print ('Press "0" to go back ')
                    elif item == '8' :
                        print ('Cotton: 10pcs. - cost 288g.')
                        while int(item) > 0 :
                            item = input ('Enter how many pieces:')
                            pcs = (int(item) * (288/10))
                            print('')
                            print ('{}{} {}{}{}'.format('Cotton:',item,'pcs. - ',int(pcs),' Coins'))
                            print ('')
                            print ('Press "0" to go back ')
                    elif item == '9' :
                        print ('Pumpkin: 10pcs. - cost 324g.')
                        while int(item) > 0 :
                            item = input ('Enter how many pieces:')
                            pcs = (int(item) * (324/10))
                            print('')
                            print ('{}{} {}{}{}'.format('Pumpkin:',item,'pcs. - ',int(pcs),' Coins'))
                            print ('')
                            print ('Press "0" to go back ')
                    elif item == '10' :
                        print ('Lettuce: 10pcs. - cost 324g.')
                        while int(item) > 0 :
                            item = input ('Enter how many pieces:')
                            pcs = (int(item) * (324/10))
                            print('')
                            print ('{}{} {}{}{}'.format('Lettuce:',item,'pcs. - ',int(pcs),' Coins'))
                            print ('')
                            print ('Press "0" to go back ')
                    elif item == '11' :
                        print ('Potato: 10pcs. - cost 360g.')
                        while int(item) > 0 :
                            item = input ('Enter how many pieces:')
                            pcs = (int(item) * (360/10))
                            print('')
                            print ('{}{} {}{}{}'.format('Potato:',item,'pcs. - ',int(pcs),' Coins'))
                            print ('')
                            print ('Press "0" to go back ')
                    elif item == '12' :
                        print ('Chili: 10pcs. - cost 360g.')
                        while int(item) > 0 :
                            item = input ('Enter how many pieces:')
                            pcs = (int(item) * (360/10))
                            print('')
                            print ('{}{} {}{}{}'.format('Chili:',item,'pcs. - ',int(pcs),' Coins'))
                            print ('')
                            print ('Press "0" to go back ')
                    elif item == '13' :
                        print ('Tomato: 10pcs. - cost 432g.')
                        while int(item) > 0 :
                            item = input ('Enter how many pieces:')
                            pcs = (int(item) * (432/10))
                            print('')
                            print ('{}{} {}{}{}'.format('Tomato:',item,'pcs. - ',int(pcs),' Coins'))
                            print ('')
                            print ('Press "0" to go back ')
                    elif item == '14' :
                        print ('Strawberries: 10pcs. - cost 504g.')
                        while int(item) > 0 :
                            item = input ('Enter how many pieces:')
                            pcs = (int(item) * (504/10))
                            print('')
                            print ('{}{} {}{}{}'.format('Strawberries:',item,'pcs. - ',int(pcs),' Coins'))
                            print ('')
                            print ('Press "0" to go back ')
                    elif item == '0' : break
            if item == '2' :
                while True :
                    TreesBush = ('''
                    Bush:
                    1.Raspberry
                    2.Blackberry
                    3.Coffee
                    4.Nectar

                    Tree:
                    5.Apple
                    6.Cherry
                    7.Cacao
                    8.Olive
                    9.Lemon:
                    0.Come back''')
                    print(TreesBush)
                    item = input('Enter the section :')
                    if item == '1' :
                        while int(item) > 0 :
                            print()
                    elif item == '0' : break
            if item == '3' :
                while True :
                    Products1 = ('''
                    1.Chicken egg''')
            elif item == '00' : break
    print('bb')
