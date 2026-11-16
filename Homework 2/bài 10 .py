import math
x0, y0, R = map(float, input().split())
I = (x0,y0)
x, y = map(float, input().split())
A = (x,y)
AI = math.sqrt((x - x0)**2 + (y - y0)**2)
if AI > R:
    print("Diem A nam ngoai duong tron")
elif math.isclose(AI, R) :
    print("Diem A thuoc duong tron")
else:
    print("Diem A nam trong duong tron")
