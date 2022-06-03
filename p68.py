num1 = (input("請輸入第一組數字:"))
num2 = (input("請輸入第二組數字:"))

a = 0
b = 0

for i in range(len(num1)):
    for j in range(len(num2)):
        if num1[i] == num2[j]:
            if i == j:
                a = a + 1
            else:
                b = b + 1
total = (str(a)+"A"+str(b)+"B")

if total == "4A0B":
    print(a,"A",b,"B","全對")
else:
    print(a,"A",b,"B","加油")