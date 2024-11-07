'''
numero = 1 
limite = int(input("digite  ate  qual numero voce quer contar:"))

while numero >= limite:#enquanto o numero for mmemor ou igual que 5
    print(numero)#exibe o numero
    #o simbolo de += para fazer uma soma com atribuicao 
    #numero += 1 ==> numero = numero + 1
    numero -= 1#soma 1 na variavel numero

numero = 1 
limite = int(input("digite  ate  qual numero voce quer contar:"))

while numero >= limite:#enquanto o numero for mmemor ou igual que 5
    print(numero)#exibe o numero
    #o simbolo de += para fazer uma soma com atribuicao 
    #numero += 1 ==> numero = numero + 1
    numero -= 1#soma 1 na variavel numero
       
 '''
'''
nome = input("digite um nome: ")
if "a" in nome:
    print("nome",nome)
else:
    print("Nome nao aceito!")    
'''
'''nome = input("Digite um nome: ")
print(nome.lower())#transforma para minusculo
print(nome.upper())#transforma para maiusculo
print(nome)'''
'''nome = input("Digite um nome: ").lower
print(nome)'''
'''
nome = input("digite um nome: ")

if nome.lower().startswith("a"):
    print("nome",nome)
else:
    print("Nome nao aceito!")  
'''  

'''while True:
    nome = input("Digite uma nome: ")
    if nome.lower().startswith("a"):
        print("Nome:", nome)
    else:
        print("Nao Não Aceito!")    '''
'''
#startswith(stringBuscada)faz uma busca no unicio da palavra 
print(nome.startswith('a'))#busca palavras que iniciam com "a"

#endswith(stringBuscada)faz uma busca no final da palavra
print(nome.endswith("a"))#busca palavras que termina com "a"
'''
'''numero = 1 
limite = int(input("digite  ate  qual numero voce quer contar:"))'''
'''numero = 10 
while numero >= 0:#enquanto o numero for mmemor ou igual que 5
    print(numero)#exibe o numero
    #o simbolo de += para fazer uma soma com atribuicao 
    #numero += 1 ==> numero = numero + 1
    numero -= 1#soma 1 na variavel numero'''

'''
nome = input("Insira um nome ")
while nome:
    if nome == "pedro":
        print("voce entrou ")
        break
    else:
       nome = input("voce errou tente de novo ")   
 '''
'''
n = int(input("digite um valor "))
acu = 0
for numero in range(5):
    aux = int(input("digite um valor"))
    acu = acu + aux  
print("a soma ", acu)    '''

'''
n = int(input("valor"))
for numero in range(5):
    n = int(input("valor"))
    n = n + 1
print("soma",n)
'''