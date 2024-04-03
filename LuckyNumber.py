def is_lucky(n):
  """
  Kiểm tra số n có phải là số may mắn hay không.
  Tham số:
    n: Số nguyên dương <= 10000000.
  Trả về:
    True nếu n là số may mắn, False nếu không.
  """
  seen = set()  # Lưu trữ các số đã được tính
  while n not in seen:
    seen.add(n)
    n = sum(int(d)**2 for d in str(n))
  return n == 1

# Ví dụ sử dụng
while True:
  try:
    n = int(input("Nhập số nguyên dương (<= 10000000): "))
    if n <= 0 or n > 10000000:
      raise ValueError
    break
  except ValueError:
    print("Số nhập vào không hợp lệ! Vui lòng nhập lại.")

if is_lucky(n):
  print(f"{n} là số may mắn")
else:
  print(f"{n} là số đen đủi")
