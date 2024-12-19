palavras = ["python", "java", "javascript", "c++", "c#", "ruby", "go"]

palavras_filtradas = list(filter(lambda x: x[0] == 'j', palavras))

print(palavras_filtradas)