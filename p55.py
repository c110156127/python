book1 = ["飢餓遊戲3","解憂雜貨店","怪獸與牠們的產地","哈利波特6","我的阿富汗筆友","祈念之樹","樓下的房客","小王子"]
book2 = ["房思琪的初戀樂園","等一個人咖啡","鬼滅之刃14","神農嘗百草","麥田捕手","老人與海","傲慢與偏見","與神同行"]
look = input("請輸入欲租借的書籍:")
if look in book1:
    for i in range(len(book1)):
        if look == book1[i]:
            print("在書架A的第",(i+1),"本")
elif look in book2:
    for i in range(len(book2)):
        if look == book2[i]:
            print("在書架B的第",(i+1),"本")