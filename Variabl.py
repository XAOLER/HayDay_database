import sys

Wheat = 3.6
Corn = 7.2
Carrot = 7.2
Soybean = 10.8
Sugarcane = 14.4
Rice = 18.8
Indigo = 25.2
Cotton = 28.8
Pumpkin = 32.4
Lettuce = 32.4
Potato = 36.0
Chili = 36.0
Tomato = 43.2
StrawberriesG = 50.4

RaspberryG = (606 - 220)/13     #вирахунок чистої ціни малиниза 1шт
Raspberry = 29.6
BlackberryG = (1074 - 530)/13   #чиста ціна ожини 1шт
Blackberry = 41.8
CoffeeG = (840 - 375)/13        #чиста ціна кави 1 шт
Coffee = 35.7
NectarG = (342 - 120)/5         #вартість чиста 1 лощиниукк
Nectar = 44.4

AppleG = ((513 - 160)/13) #вартість 1 яблука
Apple = 27.1
CherryG = (888 - 410)/13 # Вишня 1 шт
Cherry = 36.7
CacaoG = (1122-550)/13  # Какао 1 шт
Cacao = 44.0
OliveG = (1074-620)/13  # Оливка 1 шт
Olive = 34.9
Lemon = 0

input()

Egg = 18.0
Milk = 32.4
Bacon = 50.4
Wool = 54.0
GoatMilk = 64.8

FishFillet = 54.0
LobsterTail = 201.6
DuckFeather = 140.4


FeedMill = None # lu(Unlocks at level);c0;t0
ChikenFeed = 7.2
CowFeed = 14.4
PigFeed = 14.4
SheepFeed = 14.4
GoatFeed = 14.4

Bakery = None # lu;c0;t0
Bread = 21.6
CornBread = 72.0
Cookie = 104.4
RaspberryMuffin = 140.4
BlackberryMuffin = 226.8
Pizza = 190.8
SpicyPizza = 226.8
PotatoBread = 284.4
FruttiDeMarePizza = 403.2

Dairy = None # lu;c0;t0
Cream = 50.4
Butter = 82.8
Cheese = 122.4
GoatChesse = 161.0

SugarMill = None # lu;c0;t0
BrownSugar = 32.4
WhiteSugar = 50.4
Syrup = 90.0

PopcornPot = None # lu;c0;t0
Popcorn = 32.4
ButterPopcorn = 126.0
ChiliPopcorn = 122.4
HoneyPopcorn = 360.0
ChocolatePopcorn = 248.4

BBQGrill = None # lu;c0;t0
Pancake = 180.0
BaconAndEggs = 201.6
Hamburger = 180.0
FishBurger = 226.8
RoastedTomatoes = 118.8
BakedPotato = 298.8
FishAndChips = 244.8
LobsterSkewer = 417.6

PieOven = None # lu;c0;t0
CarrotPie = 82.8
PumpkinPie = 158.4
BaconPie = 219.6
ApplePie = 270
FishPie = 226.8
FetaPie = 223.2
Casserole = 367.2
ShepherdsPie = 280.8

Loom = None # lu;c0;t0
Sweater = 151.2
CottonFabric = 108.0
BlueWoollyHat = 111.6
BlueSweater = 208.8
RedScarf = 288.0

SewingMachine = None # lu;c0;t0
CottonShirt = 241.2
WoolyShaps = 309.6
VioletDress = 327.6
Pillow = 676.8
Blanket = 1098.0

CakeOven = None # lu;c0;t0
CarrotCake = 165.6
CreamCake = 219.6
RedBerryCake = 255.6
CheeseCake = 284.4
StrawberryCake = 316.8
ChocolateCake = 320.4
PotatoFetaCake = 309.6
HoteyAppleCake = 482.4

JuicePress = None # lu;c0;t0
CarrotJuice = 46.8
AppleJuice = 129.6
CherryJuice = 108.0
TomatoJuice = 162.0
BerryJuice = 205.2

IceCreamMaker = None # lu;c0;t0
VanillaIceCream = 172.8
CherryPopsicle = 352.8
StrawberryIceCream = 331.2
ChocolateIceCream = 342.0

JamMaker = None # lu;c0;t0
AppleJam = 219.6
RaspberryJam = 252.0
BlackberryJam = 388.8
CherryJam = 334.8
StrawberryJam = 270.0

HoneyExtractor = None # lu;c0;t0
Honey = 154.8
Beeswax = 234.0

CoffeeKiosk = None # lu;c0;t0
Espresso = 248.4
CaffeLatte = 219.6
CaffeMocha = 291.6
RaspberryMocha = 259.2
HotChocolate = 316.8

SoupKitchen = None # lu;c0;t0
LobsterSoup = 612.0
TomatoSoup = 478.8
PumpkinSoup = 392.4
FishSoup = 298.8

CandleMaker = None # lu;c0;t0
StrawberryCandle = 370.8
RaspberryCandle = 360.0
lemonCandle = 0

CandyMachine = None # lu;c0;t0
CaramelApple = 255.6
Toffee = 176.4
Chocolate = 460.8
Lollipop = 342.0
JellyBeans = 684.0

SauceMaker = None # lu;c0;t0
SoySauce = 154.8
OliveOil = 277.2
Mayonnaise = 0

SushiBar = None # lu;c0;t0
SushiRoll = 489.6
LobsterSushi = 637.2

SaladBar = None # lu;c0;t0
FetaSalad = 745.2
BLTSalad = 723.6

SandwichBar = None # lu;c0;t0
VeggieBagel = 532.8

SmoothieMixer = None # 64lvl ;c0;t0

PastaMaker = None # 67lvl ;c0;t0

HatMaker = None # 70lvl ;c0;t0

PastaKitchen = None # 72lvl ;c0;t0

HotDogStand = None # 75lvl ;c0;t0

Smelter = None # lu;c0; lu;c1; lu;c2; lu;c3; lu;c4;t0
SilverOre = 18.0
SilverBar = 147.6
GoldOre = 21.6
GoldBar = 180.0
PlatinumOre = 32.4
PlatinumBar = 205.2
Coal = 10.8
RefinedCoal = 108.0
IronOre = 14.4
IronBar = 129.6

Jeweler = None # lu;c0;t0
Bracelet = 514.8
Necklace = 363.6
DiamondRing = 824.4
IronBracelet = 658.8

#Other
MapPiece = 450.0
MarkerStake = 403.2
LandDeed = 403.2
Mallet = 403.2

#Silo
Nail = 270.0
Screw = 270.0
WoodPanel = 270.0

#Bran
Bolt = 270.0
Plank = 270.0
DuctTape = 270.0
