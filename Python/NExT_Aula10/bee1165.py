def eh_primo(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

n = int(input())
for _ in range(n):
    x = int(input())
    if eh_primo(x):
        print(f"{x} eh primo")
    else:
        print(f"{x} nao eh primo")