num = int(input(""))
total = 0

if num // 100 > 0:
    total = total + int(num//100)
    a = num % 100
    
    if a > 0:
        total = total + int(a//50)
        b = a % 50

        if b > 0:
            total = total + int(b//10)
            c = b % 10

            if c > 0:
                total = total + int(c//5)
                d = c % 5

                if d > 0:
                    total = total + int(d//1)

print(total)



    
