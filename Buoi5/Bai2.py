def find_by_id(data, id):
    for i in data:
        if i["id"] == id:
            return i
    return None

def filter_by_score(data, min_score):
    list1 = []
    for i in data:
        if i["score"] >= min_score:
            list1.append(i)
    return list1

def sort_by_score(data, reverse=False):
        data.sort(key=lambda x: x["score"], reverse=reverse)
        return data

def add_student(data, student_dict):
    data.append(student_dict)
    return data

def remove_student(data, id):
    student_to_remove = find_by_id(data, id)
    data.remove(student_to_remove)
    return data

def statistics(data, total=None):
    total_score = sum(s["score"] for s in data)
    dem = len(data)
    mean_score = total_score / dem

    highest = max(data, key=lambda x: x["score"])
    lowest = min(data, key=lambda x: x["score"])

    return mean_score, highest, lowest


students = [{"id": 1, "name": "An", "score": 8.5}, {"id": 2, "name": "Bình", "score": 7.2}, {"id": 3, "name": "Chi", "score": 9.0}]
print(f"tim thay sinh vien: {find_by_id(students, 2)}")
print(f"tim thay sinh vien co diem: {filter_by_score(students, 8.0)}")
print(f"sap xep giam dan: {sort_by_score(students, False)}")

new_student = {"id": 4, "name": "Dung", "score": 6.8}
print(f"danh sach sau khi them: {add_student(students, new_student)}")

print(f"sinh vien con lai sau khi xoa: {remove_student(students, 1)}")

print(statistics(students, 1))