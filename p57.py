a = input("請選擇主餐及升級的套餐:").split(" ")
b = str(input("是否升級成大杯飲料:"))
c = str(input("是否換成大薯:"))
total = 0

if a[0] == "1":
    total = total + 72
elif a[0] == "2":
    total = total + 62
elif a[0] == "3":
    total = total + 82
elif a[0] == "4":
    total = total + 44
elif a[0] == "5":
    total = total + 60

if a[1] == "A":
    total = total + 55
elif a[1] == "B":
    total = total + 68

if b == "是":
    total = total + 7
elif b == "否":
    total = total + 0

if c == "是":
    total = total + 13
elif c == "否":
    total = total + 0

print("總共為",total,"元")
