a = int(input("nhap a = "))
b = int(input("nhap b = "))

print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
print("a // b = ", a // b)
print("a ** b = ", a ** b)
print("a % b = ", a % b)

if (a > b):
   print("a lon hon b")
elif (a < b):
   print("a nho hon b")
else:
   print("a bang b")

print("a AND b = ", a & b)
print("a OR b = ", a | b)
print("a XOR b = ", a ^ b)
print("NOT (a == b) ", not (a == b))
print("a dich phai 5 bit: ", a >> 5)
print("a dich trai 6 bit: ", a << 6)

nhiphana = bin(a)[2:]
dao_nhiphana = nhiphana[::-1]
print("he co so 2 dao nguoc cua a la: ", dao_nhiphana)