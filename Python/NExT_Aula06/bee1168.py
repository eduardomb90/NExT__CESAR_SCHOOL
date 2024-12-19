'''dic = { '0':6, '1':2, '2':5, '3':5, '4':4, '5':5, '6':6, '7':3, '8':7, '9':6 }

testes = int(input())

for _ in range(testes):
    entrada = input()
    leds = 0
    
    for l in entrada:
        leds += dic.get(l)
    
    print(f'{leds} leds')'''


leds_por_numero = { '0': 6, '1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6 }

# Função para calcular o total de LEDs para um número
def calcular_leds(numero):
    return sum(leds_por_numero[d] for d in numero)

# Lê o número de casos de teste
n = int(input())

# Itera sobre cada caso de teste
for _ in range(n):
    numero = input().strip()
    total_leds = calcular_leds(numero)
    print(f"{total_leds} leds")