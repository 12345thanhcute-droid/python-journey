"""
Bài tập 03: Trò chuyện với Python
Mục tiêu: Sử dụng input() để nhận dữ liệu từ người dùng
"""

# TODO 1: Hỏi tên người dùng và in lời chào
ten = input("Nhập tên của bạn: ")
print("Xin chào,", ten)

# TODO 2: Hỏi tuổi và tính năm sinh
tuoi = int(input("Nhập tuổi của bạn: "))
nam_sinh = 2026 - tuoi
print("Bạn sinh năm:", nam_sinh)

# TODO 3: Nhập 2 số và tính tổng
so1 = int(input("Nhập số thứ nhất: "))
so2 = int(input("Nhập số thứ hai: "))
tong = so1 + so2
print("Tổng:", so1, "+", so2, "=", tong)

# TODO 4: Tạo Mad Libs mini
ten = input("Nhập tên: ")
tinh_tu = input("Nhập một tính từ: ")
con_vat = input("Nhập tên con vật: ")
so = input("Nhập một số: ")

print(ten, "có một chú", con_vat, tinh_tu,
      "và nó đã chạy được", so, "vòng quanh sân!")