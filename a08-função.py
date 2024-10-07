#função (def)

def hello():
    print("Olá mundo!")
    
def mensagem(msg):
    return f"Mensagem: {msg}"

def multiplicar(x, y):
    return x * y

hello()
print(mensagem("cambio!!!"))
print(multiplicar(3,12))

def saudacao(nome, cumpr="Olá"):
    print(f"{cumpr}, {nome}")
saudacao("Adas")
saudacao("Martins", "Bom dia")