a = int(input("小名身上有幾元:"))
type = int(input("販賣機有幾種飲料:"))
drink = []
c = 0
for i in range(type):
    price = int(input(""))
    drink.append(price)     #把錢加進串列裡面
for i in range(type):
    if a >= drink[i]:
        c = c+1
print(c)
