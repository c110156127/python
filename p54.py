a = float(input("請輸入路程公里數(km):"))
b = 75
if a < 1.5 :
    print("所需的車資為:",75)
elif a > 1.5:
    a = a - 1.5
    if a > 0.25:
        if a % 0.25 == 0:
            b = b + int(a/0.25)*5
        else:
            b = b + int(a/0.25)*5 + 5
    else:
        b = b + 5
print("所需的車資為:",b) 
     