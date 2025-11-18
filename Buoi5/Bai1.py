def remove_punctuation(s):
    list1 = " "
    for i in s:
        if i.isalpha() or i == " ":
            list1 += i
    return list1

def to_lower(s):
    return s.lower()

def remove_stopwords(s, stopwords):
    chuoi = s.split()
    list2 = " "
    for i in chuoi:
        if i not in stopwords:
            list2 += i + " "
    return list2

def pipeline(s, stopwords):
    s = remove_punctuation(s)
    s = to_lower(s)
    s = remove_stopwords(s, stopwords)
    return s



s = input("nhap chuoi: ")
print(f"chuoi sau khi xoa dau la: {remove_punctuation(s)}")
print(f"chuoi sau khi chuyen ve chu thuong la: {to_lower(s)}")

stopwords = input("nhap chuoi xoa: ").split()
print(f"chuoi sau khi xoa tu da chon la: {remove_stopwords(s, stopwords)}")
print(f"chuoi sau khi ket hop tat ca: {pipeline(s, stopwords)}")









