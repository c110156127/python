n = int(input("輸入筆數n:"))
a = []

for i in range(n):
    b = str(input("輸入獎牌與數量"))
    a.append(b)

for i in range(n):
    print(a[i][0],"牌得到",a[i][1],"面")