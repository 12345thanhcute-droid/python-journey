"""
Mini-Project: ASCII Art Generator 🎨
=====================================
Tạo chương trình in hình ASCII đẹp từ tên người dùng.

Chạy: python starter.py
"""

# Bước 1: Hỏi tên người dùng
ten = input("Nhập tên của bạn: ")

# Bước 2: Tính độ rộng khung
width = len(ten) + 6

# Bước 3: In khung trên
print("╔" + "═" * width + "╗")

# Bước 4: In tên ở giữa
print("║" + ten.center(width) + "║")

# Bước 5: In khung dưới
print("╚" + "═" * width + "╝")


# Gợi ý: Dùng str.center(width) để căn giữa
