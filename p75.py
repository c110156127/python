num = 0

while num >= 0:
    a = input("請輸入事項(若以無事項，請輸入end):")
    num = num + 1
    if a == "end":
        break
    else:
        print(num,".",a)