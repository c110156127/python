a = int(input("請輸入第一個要判斷的數字:"))
b = int(input("請輸入第二個要判斷的數字:"))

a1 = 0
b1 = 0


for i in range(2,(int(a/2)+1)):
    if (a % i) == 0:
        a1 = a1 + 1
        break
    else:
        a1 = a1 + 0

for i in range(2,(int(b/2)+1)):
    if (b % i) == 0:
        b1 = b1 + 1
        break
    else:
        b1 = b1 + 0
        


if a1 != 0 and b1 != 0 and (a-b) == 2 or (a-b) == -2:
    print("Y")
else:
    print("N")
