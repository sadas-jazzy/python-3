#Laço de repetição "For()" e range

ListaNacoes = ["Brasil", "EUA", "China", "Canada", "Inglaterra", "EUA"]

for país in ListaNacoes:
    print(país)

for caracter in "Ciência de dados":
    print(caracter)

meninas = [["Amélia", "Ana Paula", "Alice"],["Beatriz", "Bianca", "Berenice"],["Sofia", "Sandra"]]
for menina in meninas:
    print(menina)
    for nome in menina:
        print(nome)

#Range:
for i in range(5):
    print(1)

for i in range (2, 9):
    print(1)

for i in range (5, 17, 2):
    print(1)