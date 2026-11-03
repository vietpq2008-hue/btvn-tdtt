#
c = input()
if len(c) == 1:
    if c is c.isdigit():
        print(f"{c} là kí tự alphabet")
    else:
        print(f"{c} không là kí tự alphabet")    