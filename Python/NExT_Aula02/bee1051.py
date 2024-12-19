# #valor 2 casas decimais --> salário

# vvvv MINHA SOLUÇÃO ORIGINAL vvvv

# salario = float(input())
# valor_ir = 0
# imposto = 0

# if 0 <= salario <= 2000:
#     print("Isento")

# if 2000 < salario:
#     if 3000 < salario:
#         imposto = 1000 * 0.08
#     else:
#         incide = salario - 2000
#         imposto = incide * 0.08

#     valor_ir += imposto

# if 3000 < salario:
#     if 4500 < salario:
#         imposto = 1500 * 0.18
#     else:
#         incide = salario - 3000
#         imposto = incide * 0.18

#     valor_ir += imposto

# if 4500 < salario:
#     incide = salario - 4500
#     imposto = incide * 0.28

#     valor_ir += imposto

# print(f'{valor_ir:.2f}')

# ^^^^^ MINHA SOLUÇÃO ORIGINAL ^^^^^^

# vvvv EXERCÍCIO CORRIGIDO vvvv
salario = float(input())
valor_ir = 0

if salario <= 2000.00:
    print("Isento")
else:
    if salario <= 3000.00:
        valor_ir = (salario - 2000.00) * 0.08
    elif salario <= 4500.00:
        valor_ir = (1000 * 0.08) + ((salario - 3000.00) * 0.18)
    else:
        valor_ir = (1000 * 0.08) + (1500 * 0.18) + ((salario - 4500.00) * 0.28)
    
    print(f"R$ {valor_ir:.2f}")
