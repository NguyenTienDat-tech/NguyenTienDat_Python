import math

n = int(input("nhap n = "))
x = int(input("x = "))

#Câu 1
ex = 1.0
for i in range(1, n + 1): #dùng range để tạo dãy
    ex += (x ** i) / math.factorial(i)   # **: số mũ


#Câu 1
S = 1.0
for i in range(2, n + 1):
    S += 1 / math.factorial(i)

#In kết quả
print(f"gia tri gan dung cua e^{x} = {ex}")
print(f"gia tri cau S la: {S}")