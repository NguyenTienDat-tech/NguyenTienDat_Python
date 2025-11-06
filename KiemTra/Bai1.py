chuoi = "TV, Laptop, Phone, TV, Tablet, Laptop, Camera"

list = []
tachchuoi = chuoi.split(",")
for i in tachchuoi:
    list.append(i.strip())

print("xoa trung lap")
names = set(list)
print(names)

dem = 0
for i in names:
    dem += 1
print(f"so san pham co trong chuoi la: {dem}")


print("san pham ban nhay")
SanPhamBanNhay = {"Phone", "Laptop", "Smartwatch"}
print(names.intersection(SanPhamBanNhay), end=" ")

print()

print("Sản phẩm chỉ có trong kho nhưng không bán chạy:")
print(names.difference(SanPhamBanNhay), end=" ")





