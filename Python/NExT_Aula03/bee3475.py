def conversor(n):
    numeros = {
        "0": "zero", "zero": "0",
        "1": "um", "um": "1",
        "2": "dois", "dois": "2",
        "3": "tres", "tres": "3",
        "4": "quatro", "quatro": "4",
        "5": "cinco", "cinco": "5",
        "6": "seis", "seis": "6",
        "7": "sete", "sete": "7",
        "8": "oito", "oito": "8",
        "9": "nove", "nove": "9"
    }

    numero = numeros.get(n)
    print(numero)


while True:
    entrada = input()
    conversor(entrada)


# def conversor(n):
#     if n == "0":
#         print("zero")
#     elif n == "zero":
#         print("0")
#     elif n == "1":
#         print("um")
#     elif n == "um":
#         print("1")
#     elif n == "2":
#         print("dois")
#     elif n == "dois":
#         print("2")
#     elif n == "3":
#         print("três")
#     elif n == "três":
#         print("3")
#     elif n == "4":
#         print("quatro")
#     elif n == "quatro":
#         print("4")
#     elif n == "5":
#         print("cinco")
#     elif n == "cinco":
#         print("5")
#     elif n == "6":
#         print("seis")
#     elif n == "seis":
#         print("6")
#     elif n == "7":
#         print("sete")
#     elif n == "sete":
#         print("7")
#     elif n == "8":
#         print("oito")
#     elif n == "oito":
#         print("8")
#     elif n == "9":
#         print("nove")
#     elif n == "nove":
#         print("9")
        
# numero = input()
# conversor(numero)

