import re
from typing import Dict

# Kiểm tra tính hợp lệ của biểu thức logic
def is_valid_expression(expression: str) -> bool:
    try:
        # Thay các biến bằng True để kiểm tra cú pháp
        sanitized_expression = re.sub(r'\b[A-Z]\b', 'True', expression)
        # Thay các ký hiệu logic bằng các toán tử Python tương ứng
        python_expression = sanitized_expression.replace('∧', 'and').replace('∨', 'or').replace('¬', 'not ').replace('→', ' <= ').replace('↔', ' == ')
        eval(python_expression)
        return True
    except Exception:
        return False

# Tính giá trị biểu thức logic
def evaluate_expression(expression: str, values: Dict[str, bool]) -> bool:
    try:
        # Thay các biến trong biểu thức bằng giá trị tương ứng từ `values`
        for variable, value in values.items():
            expression = expression.replace(variable, str(value))
        # Thay các ký hiệu logic bằng các toán tử Python tương ứng
        python_expression = expression.replace('∧', 'and').replace('∨', 'or').replace('¬', 'not ').replace('→', ' <= ').replace('↔', ' == ')
        return eval(python_expression)
    except Exception as e:
        raise ValueError(f"Lỗi khi tính giá trị biểu thức: {e}")

# Hàm chính
def main():
    # Nhập biểu thức logic
    expression = input("Nhập biểu thức logic: ")
    # Kiểm tra tính hợp lệ
    if not is_valid_expression(expression):
        print("Biểu thức không hợp lệ.")
        return

    print("Biểu thức hợp lệ.")

    # Nhập giá trị các biến logic
    print("Nhập giá trị các biến logic (dạng A: True, B: False,...):")
    values_input = input()
    try:
        values = {k.strip(): eval(v.strip()) for k, v in (item.split(":") for item in values_input.split(","))}
    except Exception:
        print("Lỗi khi nhập giá trị biến logic. Hãy chắc chắn định dạng đúng.")
        return

    try:
        # Tính giá trị biểu thức
        result = evaluate_expression(expression, values)
        print(f"Kết quả của biểu thức: {result}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()