def str_to_int(text):
    result = 0
    for char in text:
        result = result * 10 + (ord(char) - 48)
    return result  

def decimal_sub(str_num1, str_num2):
    y = []
    borrow = 0
    str_num1 = str_num1.zfill(len(str_num2))
    str_num2 = str_num2.zfill(len(str_num1))
    for i in range(1, len(str_num1) + 1):
        num1 = str_to_int(str_num1[len(str_num1) - i]) - borrow
        num2 = str_to_int(str_num2[len(str_num2) - i])
        borrow = 0
        if num1 < num2:
            num1 += 10
            borrow = 1
        y.append(num1 - num2)
    y_str = [str(ele) for ele in reversed(y)]
    return ''.join(y_str).lstrip('0')

print(decimal_sub("2156", "1094"))