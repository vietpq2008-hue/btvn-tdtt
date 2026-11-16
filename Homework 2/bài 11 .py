#
x, y = map(float, input().split())
if y < 0 and x == 0 :
    print("Khong ton tai")
elif y == int(y):
    print(pow(x,y))
else:
    if x < 0 :
        print("Khong ton tai")
    else:
        print(pow(x,y))