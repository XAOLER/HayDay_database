#!/usr/bin/env python
# -*- coding: utf-8 -*-

Start_Mess = ('''
    Welcome to Hay Day database.
    How does it work?
    Select the appropriate number desired section, eg You want garden you plant?
    Click the key with the number "1" and press key "Enter" Ta-da-a-a :)
    ''')
go = 'Press key "Enter" to continue :'
conty = 'Enter the section:'
contb = 'Press "Enter" to go back:'
mess_error = 'Value error, try again'

select_mode = ('''
    1.Simple mode.   - Information only
    2.Advanced mode. - Much information calculator ''')
contents = ('''
    1.Cops
    2.Trees and Bush
    3.Animals and Fish-zone products
    4.Factory-made products
    5.Iron, Ingots and Jewelry
    6.Builds
    7.All tools
    8.Another and advice.

    00. Exit

    The maximum price of 10 pieces, in a roadside bench.
    Cost "14.4" - 10pcs.  "14.x" cost to point  - 1pcs
    ''')

Cops = ('''

    Wheat - 3.6
    Corn - 7.2
    Carrot - 7.2
    Soybean - 10.8
    Sugarcane - 14.4
    Rice - 18.8
    Indigo - 25.2
    Cotton - 28.8
    Pumpkin - 32.4
    Lettuce - 32.4
    Potato - 36.0
    Chili - 36.0
    Tomato - 43.2
    Strawberries - 50.4

    More information, see Advanced mode
    ''')
TreeBush = ('''
    Max. Cost - 10oct.
    Bush:
    Raspberry - 46.8
    Blackberry - 82.8
    Coffee - 64.8
    Nectar - 68.6

    Tree:
    Apple - 39.4
    Cherry - 68.4
    Cacao - 86.4
    Olive - 82.8
    Lemon -

    More information, see Advanced mode
    ''')
Animal_Fish_Product = ('''
    Animals products:
    Egg - 18.0
    Cow Milk - 32.4
    Pig Bacon - 50.4
    Sheep Wool - 54.0
    Goat Milk - 64.8

    Fish-zone:
    Fish Fillet - 54.0
    Lobster Tail - 201.6
    Duck Feather - 140.4

    More information, see Advanced mode
    ''')
FMP = ('''

    ''')
IIJ = ('''
    Silver Ore - 18.0
    Silver Bar - 147.6

    Gold Ore - 21.6
    Gold Bar - 180.0

    Platinum Ore - 32.4
    Platinum Bar - 205.2

    Coal - 10.8
    Refined Coal - 108.0

    Iron Ore - 14.4
    Iron Bar - 129.6

    Jeweler:
    Bracelet - 514.8
    Necklace - 363.6
    Diamond Ring - 824.4
    Iron Bracelet - 658.8

    More information, see Advanced mode
    ''')
build = ('''
    Chicken Coop - 20+20+20=60
       1st group - 1lvl (1-6 chickens - 10 coins)
       2nd group - 12lvl (7-12 chickens - 140 coins)
       3rd group - 23lvl (13-18 chickens - 270 coins)

    Cow Pasture - 20+20+20=60
       1st group - 6lvl (1-5 cows - 50 coins)
       2nd group - 15lvl (6-10 cows - 600 coins)
       3rd group - 27lvl (11-15 cows - 1150 coins)

    Pig Pen - 150+150+150=450
       1st group - 10lvl (1-5 pigs - 500 coins)
       2nd group - 18lvl (6-10 pigs - 1400 coins)
       3rd group - 32lvl (11-15 pigs  - 2300 coins)

    Sheep Pasture - 300+300+300=900
       1st group - 16lvl (1-5 sheep - 800 coins)
       2nd group - 26lvl (6-10 sheep - 2300 coins)
       3rd group - 42lvl (11-15 sheep - 3800 coins)

    Goat Yard - 1000+1000+1000=3000
       1st group - 32lvl (1-4 goats - 2150 coins)
       2nd group - 37lvl (5-8 goats - 5400 coins)
       3rd group - 50lvl (9-12 goats - 8650 coins)

    Beehive tree(39) - 4000c. 1-3 bees 1500
       2lvl 4000drops - 4-6 bees 2000
       3lvl 40000drops - 7-9 bees 2500
       4lvl 400000drops - 10-12 bees 3000

    City :
    Grocery Store - 500c. 14sec
    Cinema - 4500c. 5h.30m.
    Diner - 19000c. 1d.
    Bed and Breakfast - 31000c. 1d.7h.
    Spa - 62000c. 1d.11h.
    Gift shop - 67000c. 1d.15h.
    Beach cafe - 71000c. 1d.23h.

     Fish-zone:
     Fishing boat(27) - 35000c. 3d.
     Lure Workbench(27) - free
     Net Maker(30) - 28000c. 2d.
     Lobster Pool(44) - 80000 2d.
     Up.1st - 45000c. 12h.
        2nd - 52500c. 14h.
        3rd - 63800c. 16h.
        4th - 79800c. 18h.
        5th - 102000c. 20h.
     Duck Salon(50) -90000c. 2d.9h.
     Up.1st -51000c. 13h.30m.
        2nd - 59000c. 16h.
        3rd - 72000c. 18h.
        4th - 90000c. 20h.30m.
        5th - 115000c. 22h.

     Boat dock(17) - 14000c. 1d.7h.
     Neighborhood house(18) - 2500c. 8h.
     Mine(24) - 21000c. 1d.11h.
     Farm Station(34) - 39000c. 3d.
     Personal Train(Rep.lvl.4) - 13000c. 6h.
    ''')

city = ('''

    ''')

tools = ('''
    Expansion territory:
    Map Piece - 450.0
    Marker Stake - 403.2
    Land Deed - 403.2
    Mallet - 403.2

    Upgrade Silo:
    Nail - 270.0
    Screw - 270.0
    Wood Panel - 270.0

    Upgrade Bran:
    Bolt - 270.0
    Plank - 270.0
    Duct Tape - 270.0

    Upgrade Builds City:
    Stone Block -
    Hammer -
    Paint Bucket -

                ''')
load = ('''

    ''')

select_cops = ('''
    1.Wheat
    2.Corn
    3.Carrot
    4.Soybean
    5.Sugarcane
    6.Rice
    7.Indigo
    8.Cotton
    9.Pumpkin
    10.Lettuce
    11.Potato
    12.Chili
    13.Tomato
    14.Strawberries

    0.Come back
    ''')

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

GoBack = 'Press "0" to go back'
goMany = 'Enter how many pieces:'
pcs_ = 'pcs.'
cost_ = 'cost'
coins = 'Coins'

content = {1: Cops, 2: TreeBush, 3: Animal_Fish_Product, 4: FMP, 5: IIJ, 6: build, 7: tools, 8: load}

nameCop = {1: 'Wheat', 2: 'Corn', 3: 'Carrot', 4: 'Soybean',
           5: 'Sugarcane', 6: 'Rice', 7: 'Indigo', 8: 'Cotton',
           9: 'Pumpkin', 10: 'Lettuce', 11: 'Potato', 12: 'Chili',
           13: 'Tomato', 14: 'Strawberries'}

costCop = {'Wheat': 36, 'Corn': 72, 'Carrot': 72, 'Soybean': 108,
           'Sugarcane': 144, 'Rice': 188, 'Indigo': 252, 'Cotton': 288,
           'Pumpkin': 324, 'Lettuce': 324, 'Potato': 360, 'Chili': 360,
           'Tomato': 432, 'Strawberries': 504}
