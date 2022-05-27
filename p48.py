n = int(input("輸入筆數n:"))
animal = {}

for i in range(n):
    a, b = input().split()
    animal[a] = b

c = input("輸入欲查詢單字:")
if c in animal:
    print(c,"中文意思是",b)
else:
    print("字典未有此單字")
    