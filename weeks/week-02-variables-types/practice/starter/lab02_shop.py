"""Bài tương tự 02 — chuyển số lượng, tính tiền và nhận biết dữ liệu sai."""

unit_price_text = "25000"  # VND, text
quantity_text = "3"
invalid_text = "ba"

# TODO 1: đổi unit_price_text và quantity_text sang số nguyên bằng int().
unit_price_vnd = int(unit_price_text)
quantity = int(quantity_text)

# TODO 2: tính total_vnd = đơn giá * số lượng và in:
# Thành tiền: 75,000 VND
total_vnd = unit_price_vnd * quantity
print(f"Thành tiền: {total_vnd:,} VND")

# TODO 3: kiểm invalid_text.isdigit() trước khi đổi, in:
# Tình huống sai: ba không phải số lượng hợp lệ
# Không dùng float cho tiền VND của ví dụ này.
if invalid_text.isdigit():
    invalid_quantity = int(invalid_text)
    print(invalid_quantity)
else:
    print(f"Tình huống sai: {invalid_text} không phải số lượng hợp lệ")
