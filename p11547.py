n = int(input())
for i in range(n):
    a = int(input())
    res = (((a * 567) / 9) + 7492) * 235 / 47 - 498
    print(int(abs(res) % 100 // 10))
