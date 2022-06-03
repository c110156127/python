a = input("甲方的數字:")
b = input("乙方的數字:")

for i in range(len(a)):
    if int(a[i]) == "1" and int(b[i]) == "5":
        print("贏",end="")
    elif a[i] == "2" and b[i] == "1":
        print("贏",end="")
    elif a[i] == "3" and b[i] == "2":
        print("贏",end="") 
    elif a[i] == "4" and b[i] == "3":
        print("贏",end="")
    elif a[i] == "5" and b[i] == "4":
        print("贏",end="")
    else:
        print("和",end="")


