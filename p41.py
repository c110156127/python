number = int(input("搭幾次電梯:"))
now = 1
total = 0
for i in range(number):
    stage = int(input(""))
    if stage > now:
        total = total+(stage-now)*20
    else:
        total = total+(now-stage)*10
    now = stage
print(total)