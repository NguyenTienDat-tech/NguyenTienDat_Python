nhap = input("nhap gmail cua ban: ")

#Kiểm tra các điều kiện
if "@" in nhap and "." in nhap:
    lay = nhap.index("@") #lấy dấu @
    lay1 = nhap.rindex(".") #lấy dấu chấm

    # @ phải đứng trước . và có it nhât 1 ký tự giữa chúng
    if lay < lay1 - 1: #Kiểm tra @ có đứng trước dấu chấm hay không
        print("Valid")
    else:
        print("Invalid")
else:
    print("Invalid")