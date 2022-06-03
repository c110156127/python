#第1部分

a = str(input("請輸入時間1(時:分:秒):"))
list1 =a.split(":")

total1 = (int(list1[0])*60*60) + (int(list1[1])*60) + (int(list1[2])*1)
print("時間1" + "("+ a + ")"+ "格式為轉換後為",5420,"秒")


#第2部分

b = int(input("請輸入時間2(秒):"))
s = 0
min = 0
hr = 0

hr = (b//60) // 60
min = (b//60) -60
s = b - (hr*3600) - (min*60)

print(hr,":",min,":",s)

