#lista = conjunto de valores
#lista = [valor1 , valor2, ...]
#lista = list(valor1, valor2, ...)

ListaVazia = [] #cria lista vazia
ListaComElementos = [1, 2, 3, 4, 5, 6, 7]
ListaComElementosMista=[7, "python", 3.14159, True, 'c']

ListaComElementos[0] #pega o primeiro elemento
ListaComElementos[-1] #pega o ultimo elemento
ListaComElementos[:4] #pega os 3 primeiros elementos 
ListaComElementos[3:] #pega do terceiro item em diante
ListaComElementos[3:8] #pega do terceiro até o ultimo 
ListaComElementos[3:6] #pega do terceiro até o quinto
ListaComElementos[3:8:2] #pega do terceiro ao sétmo de 2 em 2

print(ListaComElementos[3:6])

len(ListaComElementos) #retorna o numero de elementos
print(len(ListaComElementos))

max(ListaComElementos) #retorna o maior valor
print(max(ListaComElementos)) 

min(ListaComElementos) #retorna o menor valor
sum(ListaComElementos) #retorna a soma de todos os elementos

print(sum(ListaComElementos))
sorted(ListaComElementos) #retorna a lista em ordem crescente 

ListaVazia.append(1) #Adiciona um elemento
ListaVazia.append("Texto")
ListaVazia.append(True)

print(ListaVazia)

ListaVazia.insert(2, "novo elemento") #adiciona elemento no indicie 2 
print(ListaVazia)

ListaVazia.remove("Texto") #remove o primeiro elemento 
print(ListaVazia)

print(ListaVazia.pop(0))
print(ListaVazia)

print(ListaVazia.index("novo elemento"))

ListaNacoes=["Brasil", "EUA", "China", "Canada", "Inglaterra", "EUA"]

print(ListaNacoes.count("EUA"))

NovaLista= ListaNacoes.copy()
print(NovaLista)

TemElemento = "Canada" in NovaLista
print(TemElemento)

while True:
    if "Brasil" in ListaNacoes:
        print("Descobri o Brasil")
        ListaNacoes.remove("Brasil")
    elif "Inglaterra" in ListaNacoes:
        print("Fui para a Inglaterra")
        ListaNacoes.remove("Inglaterra")
    else:
        print("Nada encontrado")
        break