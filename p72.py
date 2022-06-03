n = int(input("請輸入n:"))
k = int(input("請輸入k:"))

total = 0
s = 0
y = 0

if k > 1:
    s = (n // k)
    total =  s + n
    if s >= k:
        y = (s // k)
        total = s + n + y
        

print("Peter可以抽",total,"支紙菸")


