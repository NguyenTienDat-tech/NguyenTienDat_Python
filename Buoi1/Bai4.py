hoten = input("nhap ho va ten: ")
tuoi = input("nhap tuoi: ")
gioitinh = input("nhap gioi tinh(nam/nu): ")
honnhan = input("nhap tinh trang hon nhan(da ket hon/ chua ket hon): ")
print()

print("ho va ten:", hoten)
print("tuoi:", tuoi)
print("gioi tinh:", gioitinh)
print("tinh trang hon nhan:", honnhan)
print()

print("anh hung oi: ")
if gioitinh == "nu" and honnhan == "chua ket hon":
    print("ho ten:", hoten, "tuoi:", tuoi, "gioi tinh:", gioitinh, "dang doc than ne")
else:
    print("hien khong co ban nu nao ==> hung doc than tiep nhe")


