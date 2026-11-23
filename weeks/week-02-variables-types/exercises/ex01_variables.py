"""
Bài tập 01: Biến trong Python 📦
=================================
Mục tiêu: Hiểu cách khai báo và sử dụng biến
"""

# TODO 1: Tạo 4 biến lưu thông tin cá nhân
name = "An"
age = 18
average_score = 8.5
is_learning = True

for label, value in (
    ("ten", name),
    ("tuoi", age),
    ("diem_tb", average_score),
    ("dang_hoc", is_learning),
):
    print(f"{label}: {value}, type={type(value).__name__}")

# TODO 2: Hoán đổi giá trị 2 biến KHÔNG dùng biến tạm
a = 10
b = 20
a, b = b, a
print(f"Sau hoán đổi: a = {a}, b = {b}")

# TODO 3: Augmented assignment
x = 100
x += 25
print("Sau +=:", x)
x -= 10
print("Sau -=:", x)
x *= 2
print("Sau *=:", x)
x //= 5
print("Sau //=:", x)

# TODO 4 (Thử thách): Multiple assignment
ho = "Nguyen"
ten = "An"
tuoi = 18
print(f"Họ tên: {ho} {ten}, {tuoi} tuổi")
