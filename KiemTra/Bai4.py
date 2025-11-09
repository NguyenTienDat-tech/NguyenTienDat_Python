chuoi = input("nhap chuoi so: ").split()
chuoi1 = list(map(int, chuoi)) #list(map) để khử các dấu ' '
list1 = []
save = [] #lưu danh sách sau khi xóa

for i in chuoi1:
    if i not in list1:
        list1.append(i)
    else:
        if len(list1) > len(save):
            save = list1.copy() #sao chép, không gán trực tiếp
        list1.clear()
        list1.append(i)
#kiểm tra lần cuối
if len(list1) > len(save):
    save = list1.copy()

print(f"Doan con dai nhat: {tuple(save)}")
print(f"Do dai: {len(list1)}")
