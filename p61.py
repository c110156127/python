a = int(input("請輸入遊戲時間:"))

time = a - 75

n = (time // 30 ) + 1    #計算波數

cs = n * 6 + (n//3)*1 - (n//2)*1

print(cs)

