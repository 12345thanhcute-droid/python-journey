"""
Bài tập 02: Chuyển đổi kiểu dữ liệu 🔄
=========================================
Mục tiêu: Thành thạo int(), float(), str(), bool()
"""

# TODO 1: Cho so_text = "42"
so_text = "42"
so = int(so_text)
print(so + 8)

# TODO 2: Cho pi = 3.14159
pi = 3.14159
pi_integer = int(pi)
print(pi_integer)

# TODO 3: Kiểm tra bool() của các giá trị sau
values = (0, 1, "", "hello", [], [1, 2])
for value in values:
    print(f"bool({value!r}) = {bool(value)}")

# TODO 4: Nhập chiều cao (m) và cân nặng (kg)
height_text = input("Chiều cao (m): ")
weight_text = input("Cân nặng (kg): ")
height = float(height_text)
weight = float(weight_text)
bmi = weight / (height ** 2)
print(f"BMI: {bmi:.1f}")

# TODO 5 (Thử thách): Nhập số giây
seconds_text = input("Số giây: ")
total_seconds = int(seconds_text)
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print(f"{hours} giờ {minutes} phút {seconds} giây")
