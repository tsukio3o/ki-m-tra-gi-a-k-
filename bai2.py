def tinh_giai_thua(n):
    if n == 0:
        return 1  
    giai_thua = 1
    for i in range(1, n + 1):
        giai_thua *= i  
    return giai_thua

n = int(input("Nhập vào một số nguyên không âm n: "))

print(f"Giai thừa của {n} là: {tinh_giai_thua(n)}")
