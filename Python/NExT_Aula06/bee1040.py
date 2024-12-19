animais = {
    "aguia": ("vertebrado", "ave", "carnivoro"),
    "pomba": ("vertebrado", "ave", "onivoro"),
    "homem": ("vertebrado", "mamifero", "onivoro"),
    "vaca": ("vertebrado", "mamifero", "herbivoro"),
    "pulga": ("invertebrado", "inseto", "hematofago"),
    "lagarta": ("invertebrado", "inseto", "herbivoro"),
    "sanguessuga": ("invertebrado", "anelideo", "hematofago"),
    "minhoca": ("invertebrado", "anelideo", "onivoro")
}

caract = []
for _ in range(3):
    caract.append(input())

caract_tupla = tuple(caract)

animal = None
for chave, valor in animais.items():
    if valor == caract_tupla:
        animal = chave
        break

print(animal)