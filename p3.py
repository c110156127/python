a = int(input("請輸入年分:"))
n = (a-1911)%12
if n == 1:
    print("虎")
elif n == 2 :
    print("兔")
elif n == 3 :
    print("龍")
elif n == 4 :
    print("蛇")
elif n == 5:
    print("馬")
elif n == 6:
    print("羊")
elif n == 7:
    print("猴")
elif n == 8:
    print("雞")
elif n == 9:
    print("狗")
elif n == 10 :
    print("豬")
elif n == 11 :
    print("鼠")
elif n == 0:
    print("牛")