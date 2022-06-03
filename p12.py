a = input("輸入一整數序列為:").split(" ")

total = 0

for i in range(len(a)):
    if a.count(a[i]) >= (len(a)/2):
        print("過半元素為:",a[i])
        total = total + 1
        break
    
if total == 0:
    print("過半元素為:NO")
