
login = input("Insira um nome ").lower()
senha = int(input("Insira sua senha "))
senhav  = False
while (login or senha) and not senhav:
    if login == "tds01" and senha == 123:
        print("voce entrou ")
        senhav = True
    else:
        print("voce errou tente de novo ")
        login = input("Insira um nome ").lower()
        senha = int(input("Insira sua senha ")) 

'''
login = "tds01"
senha = "123"

loginDigitado = input("Digite seu login: ")
senhaDigitada = input("Digite sua senha: ")

while not (login == loginDigitado and senha == senhaDigitada):
    print("Tente Novamente")Tente Novamente
    loginDigitado = input("Digite seu login: ")
    senhaDigitada = input("Digite sua senha: ") 
    
print("Logado com sucesso!")       
'''

'''login =  input("Digite seu login ")
senha =  int(input("digite sua senha"))
while login and senha :
    if login == "tds01"  and senha == 123:
        print("voce esta no sistema ")
    else:
        print("voce errou")    
print(type(login))
print(type(senha))
'''
'''Faça um programa que verifique a senha e o login de um sistema
e só finalize quando ele acertar os dados.  Considere: login = "tds01" | senha = "123"'''
'''(login = tds01 ) and (senha = 123)
'''
'''while True:
    nome = input("Digite uma nome: ")
    if nome.lower().startswith("a"):
        print("Nome:", nome)
    else:'''
'''nome = input("digite um nome: ")

if nome.lower().startswith("a"):
    print("nome",nome)
else:
    print("Nome nao aceito!")  '''