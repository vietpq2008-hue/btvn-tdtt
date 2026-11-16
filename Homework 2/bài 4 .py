#
a, b = map(float, input().split())
if a == 0 and b != 0:
    print("Phuong trinh vo nghiem")
elif a == 0 and b == 0:
    print("vo so nghiem")
else:
    x = -b/a
    print(x + 0)