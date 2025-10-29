import math

n = int(input("nhap so nguyen dương n = "))
k = int(math.sqrt(n - 1)) #tìm số nguyên k lớn nhất sao cho k^2 < n

#loại bỏ 1^2 = 1 vi không lấy 1
if k > 1:
    result = k - 1
else:
    result = 0

print(f"ket qua = {result}")