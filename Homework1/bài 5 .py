#
a = input().upper()
if a == "A":
    print(a.lower())
else:
    b =a.lower()
    print(chr(ord(b)-1))