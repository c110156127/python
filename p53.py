from telnetlib import PRAGMA_HEARTBEAT


n = int(input("輸入n值:"))

l = {}

for i in range(n):
    name = input("請輸入姓名:")
    email = input("請輸入電子郵件:") 
    l[name] = email

a = input("請輸入要查詢電子郵件的姓名:")
print(f" {a} 電子郵件帳號為 {l[a]}")
