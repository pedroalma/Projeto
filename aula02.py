#variaveis e tipo 
'''
para criar variaveis no python, basta digitar o nome do identificador 
e usar o simbolo de igualdade (=) para fazer a atribuição,apos isso 
é so colocar o valor que deseja armazenar.

Em python , as variaveis sao dinamicamente tipadas, ou seja , não precisamos 
dizer o tipo dela quando a criamos, o que determina essa tipagem e o que e 
e o que e depois guardar um numero inteiro (int) por exemplo.
'''
# variavel do tipo caracter --> sting(str)
produto="Banana" #a string pode ser atribuida usando aspas simples('')ou duplas("")
#variaveis do tipo real -->float 
valor = 4.3#p/ o tipo flutuante (float),usamos o ponto (.) para separar as casas decimais
#variavel do tipo inteiro -> integer(int)
quantidade = 12 #p/ o tipo inteiro (int), basta escrever o valor sem as aspas 

#variavel do tipo logica -> boolean(bool)
#true --> verdadeiro 
#false -->falso
temEstoque = True #variaveis do tipo logico (bool) sempre guardam os valores True ou false 
#paraa saber o tipo de uma variavel usamos a funcao type(), dentro dos parenteses passamos 
# a variavel que queremos saber o tipo 
'''type(produto)
print("Tipo da variavel produto: ",type(produto))
print("Tipo da variavel valor : ", type(valor))
print("Tipo da variavel : ",type(quantidade))
print("Tipo da variavel : ",type(temEstoque))
'''
#-------------------------------------------------------------------------------------------------------
#Operadores aritimeticos
'''
soma  | + |
-------------------
subtracao| - |
--------------------
multiplicacao | * |
---------------------
divisao | / |
----------------------
divisao truncada | // |
(inteira)
-----------------------
potencia | ** |
-----------------------
modulo | % |
'''
'''n1 = int
n2 = int
'''
'''n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
n = n1 + n2 '''

'''n1 = input("Digite oitro numero:")
n1 = float(n1)

n2 = input("Digite oitro numero:")
n2 = float(n2)'''

n1 = input("digite um numero ")
n1 = int(n1)
n2 = input("outro numero ")
n2 =int(n2)
n = n1 + n2 
print( n1 + n2)
print(n)
print(type(n1))
print(type(n2))
#o mais (+) pode ser usado para (quando usando para numeros )
# e para concatenar (quando em strings)
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
divTrun = n1 // n2
mod = n1 % n2
pot = n1 ** n2

'''print("Soma: ",n1,  "+", n2 ,"=",n,) #forma concatenada
print(f"subtracao: {n1} - {n2} = {sub}")#forma interpolada
print(f"multiplicacao: {n1} X {n2} = {mult}")
print(f"divisao: {n1} / {n2} = {div}")
print(f"divisao truncada: {n1} // {n2} = {divTrun}")
print(f"modulo: {n1} % {n2} = {mod}")
print(f"potencia: {n1} ^ {n2} = {pot}")
print(f"subtracao: {n1} X {n2} = {mult}")'''

#----------------------------------------------------------------------------
#Operadores relacionais 
'''
igual | == |
-----------------
diferente | - |
------------------
maior | > |
------------------
Maior igual | >= |
------------------
menor que | < |
------------------
menor igual | <= |
'''
#Operador logico
'''
E | and |
-----------------
ou | or |
-----------------
nao | not |
'''