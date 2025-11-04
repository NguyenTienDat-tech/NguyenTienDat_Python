chuoi = "An:8.5, Binh:7.0, An:9.0, Cuong:6.5, Binh:8.0, Dung:7.5"

#tách dữ liệu thành list(tên, điểm)
tachChuoi = chuoi.split(",")
list = [] #danh sách lưu chuỗi

for i in tachChuoi:
    name, diem = i.strip().split(":") #strip: xóa khoảng trắng và ngăn cách tên, điểm bởi dấu :
    list.append((name, float(diem))) # lưu tên và điểm vào danh sách
print("danh sach ten va diem cua tung sinh vien:")
print(list)

#Tạo set: tên duy nhất
names = set()
for name, _ in list: #dấu , là lấy bởi ngăn cách tên với điểm. còn dấu _ để bỏ qua điểm
    names.add(name)
print("cac ten duy nhat:")
print(names)

#Tính điểm trung bình
list1 = [] #danh sách chứa tên, điểm tb
for n in names:
    tong = 0
    dem = 0
    for name, diem in list:
        if name == n:
            tong += diem
            dem += 1
    tb = (tong / dem)
    list1.append((n, tb))
print("diem trung binh cua sinh vien la:")
print(list1)

#Tìm sinh viên có điểm trung bình cao nhất, thấp nhất.
maxDiem = list1[0]
minDiem = list1[0]
for n, tb in list1:
    if tb > maxDiem[1]:
        maxDiem = (n, tb)
    if tb < minDiem[1]:
        minDiem = (n, tb)
print(f"diem cao nhat cua sinh vien la: {maxDiem}")
print(f"diem thap nhat cua sinh vien la: {minDiem}")

#sắp xếp giảm dần theo điểm trung bình
for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
        if list1[i][1] < list1[j][1]:
            list1[i], list1[j] = list1[j], list1[i]
print("sắp xếp giảm dần theo điểm trung bình của sinh vien la:")
print(list1)
