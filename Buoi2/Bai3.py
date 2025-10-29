n = int(input("nhap so luong hoc vien n = "))

#duyệt từng học viên
for i in range(1, n + 1):
    print(f"nhap tung thong tin hoc vien thu {i}")
    hoTen = input("nhap ho ten: ")
    Diem1 = int(input("Nhap diem bai kiem tra thu nhat: "))
    Diem2 = int(input("Nhap diem bai kiem tra thu hai: "))

#tính tổng điểm
TongDiem = Diem1 + Diem2

#Xếp loại học lực
if TongDiem >= 160:
    xepLoai = "hoc luc gioi"
elif 110 <= TongDiem < 160:
    xepLoai = "hoc luc kha"
else:
    xepLoai = "hoc luc kem"

#in kết quả
print(f"hoc vien thu {i} co ten {hoTen}, tong diem {TongDiem}, xep loai {xepLoai}")
