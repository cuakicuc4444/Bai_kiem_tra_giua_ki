def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = list(map(int, input("Nhập một mảng số nguyên (các số cách nhau bởi dấu cách): ").split()))

sorted_arr = bubble_sort(arr)

print("Mảng sau khi sắp xếp theo thứ tự tăng dần:", sorted_arr)
