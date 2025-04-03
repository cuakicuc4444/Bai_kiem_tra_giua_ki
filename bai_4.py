def fibonacci(n):
    fib = [0] * (n + 1)
    
    if n >= 0:
        fib[0] = 0
    if n >= 1:
        fib[1] = 1
    
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[n]

n = int(input("Nhập số nguyên không âm n: "))

if n < 0:
    print("Vui lòng nhập một số nguyên không âm!")
else:
    print(f"Số Fibonacci thứ {n} là: {fibonacci(n)}")
