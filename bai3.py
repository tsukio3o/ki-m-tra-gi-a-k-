def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

arr = list(map(int, input("Nhập vào mảng số nguyên, các phần tử cách nhau bởi dấu cách: ").split()))

bubble_sort(arr)

print("Mảng sau khi sắp xếp theo thứ tự tăng dần là:", arr)
