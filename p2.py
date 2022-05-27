a = float(input("請輸入度數:"))
if a < 120:
    print("Summer months:",a*2.1)
    print("Non-Summer months:",a*2.1)
elif 121 < a < 330:
    print("Summer months:",(120*2.1)+(a-120)*3.02)
    print("Non-Summer months:",(120*2.1)+(a-120)*2.68)
elif 331 < a < 500 :
    print("Summer months:",(120*2.1)+(330-120)*3.02+(a-330)*4.39)
    print("Non-Summer months:",(120*2.1)+(330-120)*2.68+(a-330)*3.61)
elif 501 < a < 700 :
    print("Summer months:",(120*2.1)+(330-120)*3.02+(500-330)*4.39+(a-500)*4.97)
    print("Non-Summer months:",(120*2.1)+(330-120)*2.68+(500-330)*3.61+(a-500)*4.01)
