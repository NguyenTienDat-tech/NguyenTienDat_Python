chuoi = "Happiness23424h"

#1.In ra chuỗi thường
chuoi1 = chuoi.lower()

#3.Tạo một danh sách rỗng để lưu các từ
list1 = {}

#4.Tạo một vòng for kiểm tra
for i in chuoi1:
    if i.isalpha():
        if i not in list1:
            list1.update({i : 1})
        else:
            list1[i] += 1 #nếu từ xuất hiện lần 2 thì tăng thêm 1 số
print(list1)