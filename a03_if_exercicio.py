idade=int(input("Digite sua idade: "))
if idade>=60:
    print("O voto é opcional")
elif idade>=18:
    print("O voto é obrigatório")
elif idade>=16:
    print("O voto é opcional")
else:
    print("Você não pode votar")

if idade>=60 or idade <=16 and idade >= 16:
    print("O voto é opcional")