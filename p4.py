a = int(input("x軸座標:"))
b = int(input("y軸座標:"))
if a and b > 0:
    print("該點位於第一象限，離原點距離為根號",(a**2+b**2))
elif a==0 and b == 0:
    print("該點位於原點")
elif a == 0 and b >= 0:
    print("該點位於上半平方Y軸上，離原點距離為根號",(a**2+b**2))
elif a < 0 and b >=0:
    print("該點位於左半平方X軸上，離原點距離為根號",(a**2+b**2))