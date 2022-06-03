group = int(input("組數為:"))

total = 0



for i in range(group):
    s = "第" + str(i+1) + "組"
    a = input(s).split(" ")
    total = int(a[0]) *250 + int(a[1]) * 175
    print("第" + str(i+1) + "組應收費用:",total)
    


    



    