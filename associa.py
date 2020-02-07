import random
from collections import Counter
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

while maxProduct < 10:
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

    if (instType == 0 and eightypct < 8):
        transacNO[maxProduct] = createInsType1()        
        eightypct += 1
        maxProduct += 1
    if (instType == 1 and twentypct < 2):
        transacNO[maxProduct] = createInsType2()        
        twentypct += 1
        maxProduct += 1
 

# ASSOCIATION RULE

minSup = 0.6
minCon = 0.8
line = 0

myset = set(transacNO[0])
myset2 = set(transacNO[1])

data = []
data2 = []
data += myset
data2 += myset2

results = {}
for i in data:
        results[i] = data2.count(i)+1
for i in data2:
        results[i] = data.count(i)+1      
print(results)

