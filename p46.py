n = int(input("輸入比數n:"))
a = {}

for i in range(n):
    aa , bb  = input().split()
    a[aa] = bb
for aa in a:
    print(f"{aa}牌得到 {a[aa]} 面")