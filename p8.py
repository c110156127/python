from ast import Num


a = int(input("輸入第一行正整數為:"))
b = input("第二行中數列中的數字為:")
b1 = b.split(" ")

total = 1

for i in b1:
    if b1.count(i) > total:
        total = b1.count(i)
        c = i

if total == 1:
    print("每個數字剛好只出現1次")
else:
    print("n最大出現次數的數字為:",c,"n出現次數為:",total)
