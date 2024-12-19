entrada = input()
hora_inicial, minuto_inicial, hora_final, minuto_final = map(int ,entrada.split())

total_minutos_inicio = hora_inicial * 60 + minuto_inicial
tota_minutos_final = hora_final * 60 + minuto_final

duracao_total = tota_minutos_final - total_minutos_inicio

if duracao_total > 0:
    duracao_total = duracao_total
else:
    duracao_total = duracao_total + 24 * 60

duracao_horas = duracao_total // 60
duracao_minutos = duracao_total % 60

print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")