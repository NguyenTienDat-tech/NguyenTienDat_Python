#in ra chuoi
inchuoi1 = "Chao mung den CLB Tin Hoc HIT"
print(inchuoi1)

#in ra cau tren + 10 diem
inchuoi2 = "CLB Tin Hoc HIT truc thuoc Truong CNTT"
print(inchuoi2, "- 10 diem")

#In ra các chữ cái hoa của chuỗi trên
for i in inchuoi2:
    if i.isupper():
       print(i, end = " ")
print()
#In ra các chữ cái thường của chuỗi trên
for i in inchuoi2:
    if i.islower():
        print(i, end = " ")
print()

#Kiểm tra xem từ ‘CNTT’ có thuộc chuỗi không
if "CNTT" in inchuoi2:
    print("Yes")
else:
    print("No")

#Thay thế các chữ hoa thành thường và ngược lại
print(inchuoi2.swapcase())



