numbers = [2, 3, 2, -4, 3, 5]

#loại bỏ trùng lặp
print("sau khi loai trung lap: ")
delete = list(set(numbers))
print(delete)

#Số chẵn bình phương và ố lẻ lập phương
list = []
for number in delete:
    if number % 2 == 0:
        chan = number * number
        list.append(chan) #append: hàm dùng để thêm một phần tử vào cuối danh sách (list).
    else:
        le = number * number * number
        list.append(le)
print("so chan binh phuong, so le lap phuong:")
print(list)

#Tính trung bình cộng số chẵn
tinh = 0
dem = 0
print("trung binh cong so chan: ")
for number in delete:
    if number % 2 == 0:
        tinh += number
        dem += 1
if dem > 0:
    ketQua = tinh / dem
    print(ketQua)
else:
    print("khong co so chan nao")

#sắp xếp trị tuyệt đối tăng dần
list1 = []
for i in range(len(delete)):
    for j in range(i + 1, len(delete)):
        if (abs(delete[i]) > abs(delete[j])):
            delete[i], delete[j] = delete[j], delete[i]
list1.append(delete)
print("sap xep day so tri tuyet doi tang dan: ")
print(list1)
