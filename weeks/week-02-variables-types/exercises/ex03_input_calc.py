"""
Bài tập 03: Máy tính nhận input 🖥️
====================================
Mục tiêu: Kết hợp input() với tính toán
"""

# TODO 1: Nhập 2 số từ người dùng
first = float(input("Số thứ nhất: "))
second = float(input("Số thứ hai: "))
print(f"Tổng: {first + second}")
print(f"Hiệu: {first - second}")
print(f"Tích: {first * second}")
if second != 0:
    print(f"Thương: {first / second}")
else:
    print("Thương: Không thể chia cho 0")

# TODO 2: Nhập bán kính hình tròn
pi = 3.14159
radius = float(input("Bán kính hình tròn: "))
area = pi * radius ** 2
circumference = 2 * pi * radius
print(f"Diện tích: {area}")
print(f"Chu vi: {circumference}")

# TODO 3: Nhập giá gốc và phần trăm giảm giá
price = float(input("Giá gốc: "))
discount_percent = float(input("Phần trăm giảm giá: "))
discounted_price = price * (1 - discount_percent / 100)
print(f"Giá sau giảm: {discounted_price:,.0f}")

# TODO 4 (Thử thách): Máy đổi tiền
amount_vnd = float(input("Số tiền VNĐ: "))
exchange_rate = float(input("Tỷ giá USD/VNĐ: "))
if exchange_rate != 0:
    amount_usd = amount_vnd / exchange_rate
    print(f"Số USD: {amount_usd:.2f}")
else:
    print("Tỷ giá phải khác 0")
