a = input("請輸入A的好友:")
b = input("請輸入B的好友:")

a1 = a.split(" ") 
b1 = b.split(" ")

total = 0

for i in range(len(a1)):      #range不能放list 
    for j in range(len(b1)):
        if a1[i] == b1[j]:
            total = total + 1
        else:
            total = total + 0

print(total)

