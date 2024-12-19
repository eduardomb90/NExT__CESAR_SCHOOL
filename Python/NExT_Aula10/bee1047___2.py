hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

total_minutos_inicial = hora_inicial * 60 + minuto_inicial
total_minutos_final = hora_final * 60 + minuto_final

duracao_total = total_minutos_final - total_minutos_inicial

if duracao_total <= 0:
    duracao_total = 60 * 24 + duracao_total

duracao_horas_total = duracao_total // 60
duracao_minutos_total = duracao_total % 60


print(f"O JOGO DUROU {duracao_horas_total} HORA(S) E {duracao_minutos_total} MINUTO(S)")