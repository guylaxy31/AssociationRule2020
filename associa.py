import random
from collections import Counter
import operator
import math 
import itertools

#  PRODUCT NAME
product = ["Apple", "Banana", "Coke", "Icesream", "Sprice", "Knife", "Pan", "Pork", "Yogurt", "Tomato sauce",
"Spaghetti", "Steamed bun", "Mama", "Orange juice", "Sandwich", "Water", "Sausage", "Beer", "Spy", "M150",
"C-vit", "Umbrella", "TV", "Computer", "Notebook", "Pen", "Pencil", "Eraser", "Ruler", "T-shirt",
"Ski", "Winter coat", "Football", "Badminton racket", "Stud shoes", "Picture frame", "Keyboard", "Mouse", "Canned food", "Plate",
"Toy", "Metal", "Wood", "Glass", "Battery", "Lay", "Vegetable", "Gun", "Smart watch", "Dumbell"]

# GENERATE TRANSACTIONS
transacNO = [None]*10

buyAmount1 = [None]*random.randrange(2, 6)
buyAmount2 = [None]*random.randrange(6, 9)

lenBuyAmount1 = len(buyAmount1)
lenBuyAmount2 = len(buyAmount2)

maxProduct = 0
eightypct=0
twentypct=0

while maxProduct < len(transacNO):
    instType = random.randrange(2)

    def createInsType1():
        i=0
        inst1 = []*lenBuyAmount1
        while i < lenBuyAmount1:
            inst1.append(product[random.randrange(50)])
            i += 1
        return inst1

    def createInsType2():
        i=0
        inst1 = []*lenBuyAmount2
        while i < lenBuyAmount2:
            inst1.append(product[random.randrange(50)])
            i += 1
        return inst1

    if (instType == 0 and eightypct < 0.8*len(transacNO)):
        transacNO[maxProduct] = createInsType1()        
        eightypct += 1
        maxProduct += 1
    if (instType == 1 and twentypct < 0.2*len(transacNO)):
        transacNO[maxProduct] = createInsType2()        
        twentypct += 1
        maxProduct += 1
 

# ASSOCIATION RULE

minSup = math.floor(0.6*len(transacNO)/math.log(len(transacNO)))
minCon = 0.8
line = 0
results = {}
realResults = {}
data = []

for line in range(len(transacNO)):
    globals()["myset" + str(line)] = set(transacNO[line])
    data.append(globals()["myset" + str(line)])

counts = dict()

for product in data:
    for i in product:
        counts[i] = counts.get(i, 0) + 1

sorted_d = sorted(counts.items(), key=operator.itemgetter(1), reverse=True)
print('(---------------------------------------------)')
print('*** Sorted ***')
print(sorted_d,'\n')
print('       -----------------------------------')
print('       | Min-support Transactions = ',minSup,' |')
print('       -----------------------------------\n')

filterProduct1 = []

for product in sorted_d:
    if(product[1] >= minSup):
        filterProduct1.append(product)

KeyofList = []
KeyofList2 = []
resultsKey = []

for productKey in filterProduct1:
    KeyofList.append(productKey[0])
    KeyofList2.append(productKey[0])

resultsKey.append(KeyofList)
resultsKey.append(KeyofList2)

matchProduct = []
for element in itertools.product(*resultsKey):
    if element[0] != element[1] and element[0] not in matchProduct:
        matchProduct.append(element)
if len(matchProduct) == 0:
    print("[ !!!!! No any product is strong rule !!!!! ]")
else:
    print('*** TWO PRODUCTS ***')
    print(matchProduct)
    
# COUNT WITH ORIGINAL TRANSACTIONS

print('***********************',transacNO)

for listTrans in transacNO:
    for prodct in matchProduct:
        if prodct[0] and prodct[1] in listTrans:
            print(prodct,'Matched')
        else:
            print(prodct,'Not matched!')