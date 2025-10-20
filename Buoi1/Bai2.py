nhap = input("nhap chuoi ky tu: ")

# Dong 1: in ra true neu co tu hit hoac "HIT" va nguoc lai
print("dong 1:")
if "hit" in nhap.lower():
    print(True)
else:
    print(False)

# Dong 2: in ra true neu khong co so 16 trong nhap va nguoc lai
print("dong 2:")
if "16" not in nhap:
    print(True)
else:
    print(False)