def factorial(nnn):
    if nnn == 0:  
        return 1
    result = 1
    for i in range(1, nnn + 1):  
        result *= i
    return result

while True:
    nnn = input("Nhập số nguyên không âm n (hoặc 'q' để thoát): ")

    if nnn.lower() == 'q':
        break

    if not nnn.isdigit():
        print("Vui lòng nhập một số nguyên không âm")
        continue

    nnn = int(nnn)

    if nnn < 0:
        print("Vui lòng nhập số nguyên không âm")
    else:
        print(f"Giai thừa của {nnn} là: {factorial(nnn)}")
