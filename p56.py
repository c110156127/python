n = int(input("請輸入一個正整數(<=10):"))

if n > 10:
    print("錯誤!")
else:
    for i in range(n):
        for j in range(0,i+1):
            print(str((i+1)*(j+1)) + " ",end="")
        print()