
list1 = ['red','blue','red','green']

a = input("")
list2 = a.split(" ")

s = ""

if list1 == list2:
    print("正確解答")
else:
    for i in range(4):
        if list1[i] == list2[i]:
            s = s + "1"
        elif list2[i] in list1:
            s = s + "2"
        else:
            s = s + "3"
    print(s)


