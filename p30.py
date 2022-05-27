a = input("")
b = "1234"

c = 0
d = 0

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:  #如果位置一樣
            if i == j:    #位置一樣 數字也一樣
                c = c+1   
            else:
                d = d+1
print(c,"A",d,"B")

