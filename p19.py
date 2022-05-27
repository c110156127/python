from telnetlib import EL, PRAGMA_HEARTBEAT


a = str(input(""))
b = str(input(""))
c = str(input(""))
if a == "O" and b =="O":
    if c =="A"or c=="B"or c=="AB":
        print("IMPOSSIBLE")
    elif c == "O":
        print("YES")
if a =="O" and b == "A":
    if c == "B"or c=="AB":
        print("IMPOSSIBLE")
    elif c == "A"or c=="O":
        print("YES")
if a =="O" and b == "B":
    if c == "A"or c=="AB":
        print("IMPOSSIBLE")
    elif c == "B"or c=="O":
        print("YES")
if a =="O" and b == "AB":
    if c == "O"or c=="AB":
        print("IMPOSSIBLE")
    elif c == "B"or c=="A":
        print("YES")
if a =="A" and b == "A":
    if c == "B"or c=="AB":
        print("IMPOSSIBLE")
    elif c == "A"or c=="O":
        print("YES")
if a =="A" and b == "B":
    if c == "A"or c=="AB" or c=="B" or c=="O":
        print("YES")
if a =="A" and b == "AB":
    if c == "O":
        print("IMPOSSIBLE")
    elif c == "B"or c=="AB" or c=="A":
        print("YES")
if a =="B" and b == "B":
    if c == "A"or c=="AB":
        print("IMPOSSIBLE")
    elif c == "B"or c=="O":
        print("YES")
if a =="B" and b == "AB":
    if c == "O":
        print("IMPOSSIBLE")
    elif c == "B"or c=="AB" or c=="A":
        print("YES")
if a =="AB" and b == "AB":
    if c == "O":
        print("IMPOSSIBLE")
    elif c == "B"or c=="A" or c=="AB":
        print("YES")    