n = int(input("請輸入正整數n:"))

total = 0

for i in range(1,n):
    if n % i == 0 :
        total = total + i
        continue
    else:
        pass

if total > n:
    print("abundant")
elif total == n:
    print("perfect")
elif total < n:
    print("deficient")



