import random
from collections import Counter
import operator
import math 
import itertools
from itertools import combinations

#  PRODUCTS NAME
product = ["Apple", "Banana", "Coke", "Ice cream", "Sprite", "Knife", "Pan", "Pork", "Yogurt", "Tomato sauce",
"Spaghetti", "Steamed bun", "Mama", "Orange juice", "Sandwich", "Water", "Sausage", "Beer", "Spy", "M150",
"C-vit", "Umbrella", "TV", "Computer", "Notebook", "Pen", "Pencil", "Eraser", "Ruler", "T-shirt",
"Ski", "Winter clothes", "Football", "Badminton racket", "Stud shoes", "Picture frame", "Keyboard", "Mouse", "Canned food", "Plate",
"Toy", "Metal", "Wood", "Glass", "Battery", "Lay's", "Vegetable", "Gun", "Smart watch", "Dumbell"]

# GENERATE TRANSACTIONS
transacNO = [None]*1000

# buyAmount1 = [None]*random.randrange(2, 6)
# buyAmount2 = [None]*random.randrange(6, 9)

buyAmount1 = [None]*random.randrange(15, 16)
buyAmount2 = [None]*random.randrange(17, 18)

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
print('(---------------------------------------------)')       
print('\n*** Transaction ***\n',transacNO,'\n')

# ASSOCIATION RULE

minSup = math.floor(0.6*len(transacNO)/math.log(len(transacNO)))
minCon = 0.8*100
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
# print('(---------------------------------------------)')
# print('*** Counted & Sorted ***')
# print(sorted_d,'\n')
print('       -----------------------------------')
print('       | Min-support Transactions = ',minSup,' |')
print('       -----------------------------------\n')

filterProduct1 = []

for product in sorted_d:
    if(product[1] >= minSup):
        filterProduct1.append(product)

KeyofList = []

for productKey in filterProduct1:
    KeyofList.append(productKey[0])

matchProduct = []

for element in combinations(KeyofList, 2):
    matchProduct.append(element)

if len(matchProduct) == 0:
    print("[ !!!!! No any product is strong rule !!!!! ]")
else:
    print('*** PRODUCTS LIST > MIN-SUP ***')
    
# COUNT WITH ORIGINAL TRANSACTIONS

matchProductstats = []
for eachMatch in matchProduct:
    counter = 0
    for eachTransac in transacNO:
        check = all(item in eachTransac for item in eachMatch)
        if check is True:           
            counter += 1
            # print("The list {} contains all elements of the list {}".format(eachTransac, eachMatch))
    if counter >= minSup:
        matchProductstats.append(eachMatch)
if len(matchProductstats) > 0:
    print('\n',matchProductstats)

# JOIN BETWEEN 2 LISTS [ Condition is not same itself ] 

copyMatch = matchProductstats.copy()
resultMatch = []

for elem in matchProductstats:
    index_elem = matchProductstats.index(elem)
    for elm in elem:
        for ee in copyMatch[index_elem:]:
            for eee in ee:
                if elm == eee and elem != ee:
                    resultMatch.append(set(elem+ee))

# COUNTING 3 PRODUCT SAME SET

threePdcResults = []
counting = 0
mostCount = 0
max = 0
for x in resultMatch:
    for i in resultMatch:
        if x == i:
            counting += 1 
    if(counting >= mostCount and counting > 1 and x not in threePdcResults):
        max = counting
        mostCount = counting
        threePdcResults.append(set(x))
    print(counting, x)
    counting = 0

# PRINT MOST SAME SET COUNT

if len(threePdcResults) > 0:
    print("\nMost counting is ",max)
    print(threePdcResults)
    findThreeinTran = 0
    countA = 0
    countB = 0
    countC = 0
    countBC = 0
    countAC = 0
    countAB = 0
    patternA = 0
    patternB = 0
    patternC = 0
    patternBC = 0
    patternAC = 0
    patternAB = 0
    resultFromPercent = 0
    for element in threePdcResults:
        for tranNo in transacNO:
            if(list(element)[0] in tranNo and list(element)[1] in tranNo and list(element)[2]):
                findThreeinTran += 1
            if(list(element)[0] in tranNo):
                countA += 1
            if(list(element)[1] in tranNo):
                countB += 1
            if(list(element)[2] in tranNo):
                countC += 1
            if(list(element)[1] in tranNo and list(element)[2] in tranNo):
                countBC += 1
            if(list(element)[0] in tranNo and list(element)[2] in tranNo):
                countAC += 1
            if(list(element)[0] in tranNo and list(element)[1] in tranNo):           
                countAB += 1
        resultFromPercent = round((((findThreeinTran/len(transacNO))/(countA/len(transacNO)))*100),2)
        if resultFromPercent >= minCon:
            patternA = 1
        print(list(element)[0],' -> ',list(element)[1],',',list(element)[2],' COUNT = (',findThreeinTran,'/',len(transacNO),') / (',countA,'/',len(transacNO),')',' Percent is ',resultFromPercent)
        resultFromPercent = round((((findThreeinTran/len(transacNO))/(countB/len(transacNO)))*100),2)      
        if resultFromPercent >= minCon:
            patternB = 1
        print(list(element)[1],' -> ',list(element)[0],',',list(element)[2],' COUNT = (',findThreeinTran,'/',len(transacNO),') / (',countB,'/',len(transacNO),')',' Percent is ',resultFromPercent)
        resultFromPercent = round((((findThreeinTran/len(transacNO))/(countC/len(transacNO)))*100),2)
        if resultFromPercent >= minCon:
            patternC = 1
        print(list(element)[2],' -> ',list(element)[0],',',list(element)[1],' COUNT = (',findThreeinTran,'/',len(transacNO),') / (',countC,'/',len(transacNO),')',' Percent is ',resultFromPercent)
        resultFromPercent = round((((findThreeinTran/len(transacNO))/(countBC/len(transacNO)))*100),2)
        if resultFromPercent >= minCon:
            patternBC = 1
        print(list(element)[1],',',list(element)[2],' -> ',list(element)[0],' COUNT = (',findThreeinTran,'/',len(transacNO),') / (',countBC,'/',len(transacNO),')',' Percent is ',resultFromPercent)
        resultFromPercent = round((((findThreeinTran/len(transacNO))/(countAC/len(transacNO)))*100),2)
        if resultFromPercent >= minCon:
            patternAC = 1
        print(list(element)[0],',',list(element)[2],' -> ',list(element)[1],' COUNT = (',findThreeinTran,'/',len(transacNO),') / (',countAC,'/',len(transacNO),')',' Percent is ',resultFromPercent)
        resultFromPercent = round((((findThreeinTran/len(transacNO))/(countAB/len(transacNO)))*100),2)
        if resultFromPercent >= minCon:
            patternAB = 1
        print(list(element)[0],',',list(element)[1],' -> ',list(element)[2],' COUNT = (',findThreeinTran,'/',len(transacNO),') / (',countAB,'/',len(transacNO),')',' Percent is ',resultFromPercent)
        
        print('*** STRONG CASE FOR MINCON IS ',minCon,' %\n')

        if(patternA):
            print('{',list(element)[0],' -> ',list(element)[1],',',list(element)[2],'}')
        if(patternB):
            print('{',list(element)[1],' -> ',list(element)[0],',',list(element)[2],'}')
        if(patternC):
            print('{',list(element)[2],' -> ',list(element)[0],',',list(element)[1],'}')
        if(patternBC):
            print('{',list(element)[1],',',list(element)[2],' -> ',list(element)[0],'}')
        if(patternAC):
            print('{',list(element)[0],',',list(element)[2],' -> ',list(element)[1],'}')
        if(patternAB):
            print('{',list(element)[0],',',list(element)[1],' -> ',list(element)[2],'}\n')    

        findThreeinTran = 0
        countA = 0
        countB = 0
        countC = 0
        countBC = 0
        countAC = 0
        countAB = 0
        patternA = 0
        patternB = 0
        patternC = 0
        patternBC = 0
        patternAC = 0
        patternAB = 0       
else:
    print("Nothing in list is strong rule")

