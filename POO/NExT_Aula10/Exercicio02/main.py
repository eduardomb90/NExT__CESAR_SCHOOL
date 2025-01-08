from decorators import log_execucao

@log_execucao
def comeca_maiusculo1() -> None:
        textos = [
        "Banana", "laranja", "Cachorro", "gato", "Elefante",
        "tigre", "Abacaxi", "morango", "Uva", "pera",
        "Carro", "bicicleta", "Moto", "avião", "Trem",
        "barco", "Navio", "canoa", "Peixe", "Tubarão",
        "Golfinho", "Arara", "papagaio", "Falcão", "águia",
        "Gorila", "macaco", "Cavalo", "Zebra", "leão",
        "Girafa", "hipopótamo", "Rinoceronte", "Formiga",
        "abelha", "Borboleta", "escorpião", "Cobra",
        "Jacaré", "lagarto", "Tartaruga", "Lobo", "urso",
        "Raposa", "sapo", "Pato", "Galo", "galinha",
        "Vaca", "boi", "Porco", "ovelha", "Cordeiro",
        "Morango", "Melancia", "Pêssego", "kiwi", "Framboesa",
        "Tomate", "Pimenta", "Manga", "Carambola", "Coco",
        "Amora", "Cereja", "Limão", "Mamão", "Jabuticaba",
        "Pinhão", "Mandioca", "Cebola", "Alho", "Chuchu",
        "Abóbora", "Beterraba", "Alface", "Couve", "Espinafre",
        "Berinjela", "Repolho", "Rabanete", "Gengibre", "Pepino",
        "Pimentão", "Brócolis", "Quiabo", "Jiló", "Maxixe",
        "Nabo", "Cará", "Ervilha", "Graviola", "Pitanga",
        "Lichia", "Guaraná", "Tâmara", "Mexerica", "Noz",
        "Castanha", "Amêndoa", "Avelã", "Pistache", "Macadâmia",
        "Salsa", "Coentro", "Manjericão", "Orégano", "Alecrim",
        "Tomilho", "Louro", "Cebolinha", "Hortelã", "Sálvia",
        "Canela", "Cravo", "Noz-moscada", "Anis", "Cardamomo",
        "Erva-doce", "Mostarda", "Páprica", "Cominho", "Goiaba"
    ]

        contador = 0
        for texto in textos:
            if texto[0] == texto[0].upper():
                contador += 1

        print(contador)



if __name__ == '__main__':

    comeca_maiusculo1()