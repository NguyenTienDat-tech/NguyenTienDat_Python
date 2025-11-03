chuoi = "Able , was I saw Elba!"

#xóa kí tự không phải chữ thường
print("xoa ki tu khong phai khoang trang: ")
for i in chuoi:
    if i.isalpha() or i == " ": #isalpha: xóa kí tự không phải chữ cái
        print(i, end = "")

#chuyển về chữ thường
print("\nchuyen ve chu thuong: ")
for i in chuoi:
    if i.isalpha() or i == " ":
        inchuoi = i.lower()
        print(inchuoi, end = "")

#dem nguyen am phu am
nguyenam = "ueoai"
demNguyenAm = 0
demPhuAm = 0
for dem in chuoi:
    if dem.isalpha() and dem.lower() in nguyenam:
        demNguyenAm += 1
    elif dem.isalpha():
        demPhuAm += 1
print()
print(f"nguyen am = {demNguyenAm}")
print(f"phu am = {demPhuAm}")

#tách chuỗi thành danh sách và đảo ngược từ
chuoiMoi = ""
for i in chuoi:
    if i.isalpha() or i == " ":
        chuoiMoi += i
tachChuoi = chuoiMoi.split()
DaoChuoi = [t[::-1] for t in tachChuoi]
print("chuoi sau khi dao la: ")
print(DaoChuoi)

#Kiểm tra xem chuỗi có phải là palindrome không (bỏ qua khoảng trắng, hoa/thường).
print("kiem tra chuoi co phai la palindrome: ")
for i in chuoi:
    if i.isalpha() or i == " ":
        chuoi3 = i.lower()
if chuoi3 == chuoi3[::-1]:
    print("True")
else:
    print("False")



