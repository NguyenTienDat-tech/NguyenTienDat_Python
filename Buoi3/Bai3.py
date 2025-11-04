chuoi = "Xin chao toi ten la DAT"

#tách từ và chuyển về chữ thường
chuoi1 = chuoi.lower().split() #không có split --> in từng chữ cái, có split --> in từ

#tạo list các từ duy nhất(theo thứ tự)
list = []
for i in chuoi1:
    if i not in list:
        list.append(i)
print("danh sach cac tu duy nhat la:")
print(list)

#Đếm số lần xuất hiện của từng từ
dem = 0
for i in list:
    dem += 1
print(f"so lan xuat hien cua tung tu la: {dem}")

#In ra từ có tần suất xuất hiện cao nhất
maxDem = 0
tuMax = ""
for i in list:
    if chuoi1.count(i) > maxDem:
        maxDem = chuoi1.count(i) #count: dùng để đếm số lần xuất hiện của giá trị trong chuỗi
        tuMax = i
print(f"Tu co tan suat xuat hien cao nhat: {tuMax} ({maxDem} lan)")

#In ra từ dài nhất trong chuỗi
wordLong = list[0]
for i in list:
    if len(i) > len(wordLong):
        wordLong = i
print(f"tu dai nhat trong chuoi la: {wordLong}")

#tổng số ký tự trong tất cả các từ.
tongKyTu = 0
for i in chuoi1:
    tongKyTu += len(i) #Len:đếm cả khoảng trắng
print(f"tong ky tu trong tat ca cac tu la: {tongKyTu}")

#In ra danh sách các từ được sắp xếp theo độ dài giảm dần
for i in range(len(list)):
    for j in range(i + 1, len(list)):
        if len(list[i]) < len(list[j]):
            list[i], list[j] = list[j], list[i]
print("cac tu sap xep theo do dai giam dan la: ")
print(list)


