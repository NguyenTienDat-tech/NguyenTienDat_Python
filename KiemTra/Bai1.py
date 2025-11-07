#in chuỗi
chuoi = "TV, Laptop, Phone, TV, Tablet, Laptop, Camera"

#1. Chuyển chuỗi thành list.
chuoiList = chuoi.split(", ")

#2. Loại bỏ trùng lặp bằng set, sau đó chuyển lại thành tuple. In ra tuple
chuoiSet = set(chuoiList) #xóa bỏ trùng lặp
chuoiTuple = tuple(chuoiSet) #thay thành ngoặc đơn
print("chuoi sau khi xoa bo trung lap:")
print(chuoiTuple)

#3. Đếm số loại hàng hoá (len() tuple) và in ra số loại hàng hóa
chuoiDem = len(chuoiTuple) #đếm chuỗi
print(f"tong so san pham la: {chuoiDem}")

#4. Có 3 sản phẩm bán chạy là :
BanChay = {"Phone", "Laptop", "Smartwatch"}

#5. In ra danh sách loại sản phẩm có trong kho và bán chạy (intersection).
BanChaySet = set()
for i in chuoiTuple:
    if i in BanChay:
        BanChaySet.add(i)
print("san pham ban chay: ")
print(chuoiSet.intersection(BanChaySet))

#6. In ra loại sản phẩm chỉ có trong kho nhưng không bán chạy (difference).
print("san pham ban khong chay: ")
print(chuoiSet.difference(BanChaySet))