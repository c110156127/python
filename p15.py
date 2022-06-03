n = input("輸入一組四位數字為:")

num = []

for i in range(len(n)):
    num.append(n[i])


a = (int(n[0]) + 7) % 10  #8
b = (int(n[1]) + 7) % 10  #9
c = (int(n[2]) + 7) % 10  #0
d = (int(n[3]) + 7) % 10  #1

a1 = str(a)
b1 = str(b)
c1 = str(c)
d1 = str(d)

print("輸出加密後的數字為:" + c1 + d1 + a1 + b1)