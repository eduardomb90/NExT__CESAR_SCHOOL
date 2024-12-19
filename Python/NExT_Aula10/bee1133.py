x = int(input())
y = int(input())

inicio = min(x, y) + 1
fim = max(x, y)

for i in range(inicio, fim):
    if i % 5 == 2 or i % 5 == 3:
        print(i)