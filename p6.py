a = input("")
a1 = a.split(",")


b1 = sorted(a1)

min = b1[0] + b1[1] + b1[2] + b1[3] + b1[4]
max = b1[4] + b1[3] + b1[2] + b1[1] + b1[0]

min1 = int(min)
max1 = int(max)
total = max1 - min1

print("最大值數列與最小值數列差值為:",total)
#c1 = [int(i) for i in b1]  #將str轉成int

#d1 = ""

#d2 = c1[0] + c1[1] + c1[2] + c1[3] + c1[4]

#print(d2)



