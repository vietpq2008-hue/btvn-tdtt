#
import math
a, b, c = map(float, input().split())
match (a,b,c):
    case(0,0,c):
        print("Phuong trinh vo nghiem")
    case (0,0,0):
        print("Phuong trinh co vo so nghiem")
    case(0,b,c):
        x = -c/b
        print(x+0)
    case(a,b,c):
        delta = b**2 - 4*a*c
        if delta == 0:
            x = (-b/2*a)
            print(x)
        elif delta < 0:
            print("Phuong trinh vo nghiem")
        else:
            x1 = (-b - math.sqrt(delta))/(2*a)
            x2 = (-b + math.sqrt(delta))/(2*a)
            print(x1)
            print(x2)


         
    
