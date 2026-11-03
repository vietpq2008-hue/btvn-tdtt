#
Ten_chu_ho = input("Họ và tên: ")
Chi_so_thang_truoc = int(input())
Chi_so_thang_nay = int(input())
x = Chi_so_thang_nay - Chi_so_thang_truoc
if 0 < x < 51:
    Tien_phai_tra = x*1984
elif 50 < x < 101:
    Tien_phai_tra = 50*1984 + (x-50)*2050
elif 100 < x < 201:
    Tien_phai_tra = 50*1984 + 50*2050 + (x-100)*2380
elif 200 < x < 301:
    Tien_phai_tra = 50*1984 + 50*2050 + 50*2380 + (x-200)*2998
elif 300 < x < 401:
    Tien_phai_tra = 50*1984 + 50*2050 + 50*2380 + 100*2998 + (x-300)*3350
elif x > 400 :
    Tien_phai_tra = 50*1984 + 50*2050 + 50*2380 + 100*2998 + 100*3350 + (x-400)*3460    
Tien_phai_tra_sau_thue = Tien_phai_tra*1.08
print(f"Tien phải trả là: {Tien_phai_tra_sau_thue}")    