a = input("輸入五張牌:")
s = 0
list1 = a.split()
for i in range(len(list1)):
    if list1[i] == "A":
        s = s+1
    elif list1[i] == "J":
        s = s+11
    elif list1[i] == "Q":
        s = s+12
    elif list1[i] == "K":
        s = s+13
    else:
        s = s + int(list1[i])
    print(s)
