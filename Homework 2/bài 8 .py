#
a, b, c, d, m, n = map(float, input().split())
D =a*d - b*c
Dx = m*d - n*b
Dy = a*n - c*m
match (D,Dx,Dy):
    case (0,0,0):
        print("He phuong trinh co vo so nghiem")
    case (0,_,_):
        print("He phuong trinh vo nghiem")
    case (_,_,_):
        x = Dx/D + 0
        y = Dy/D + 0
        print(f"x = {x}, y = {y}")    
        
