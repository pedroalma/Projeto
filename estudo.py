'''x = int(input("Digite um inteiro menor que 11: "))
while x > 10:
    print("O numero deve ser menor que 11.")
    x = int(input("Digite um inteiro menor que 11: "))
print("Seu numero e",x)    '''

'''
x = 0
while x < 3:
    x = x + 1
    print("O valor de x é",x)
    if x == 2:
        continue
    print("Cheguei á ultima linha do laço")
print("fim")   
'''

'''
Fibonacci
f1,f2 =  1,1
while f1 <= 1000:
    print(f1)
    f1,f2 = f2,f1+f2
'''
'''n,c = 0,1
while c <= 10**9:
    print(c)
    c = (4*n+2)*c//(n+2)
    n = n + 1
'''
'''
x,y,z = 1,1,2
r = [x,y,z]
print(r)
x = 0
print(x,y,z)
print(r)
'''
'''
from math import sqrt
r = [ 1.0 , 1.5,-2.2]
comprimento = sqrt( r[0]**2 + r[1]**2 + r[2]**2)
print(comprimento)
'''

r = [1.0,1.5,-2.2,-2,-3]
print(r)
r[1] = 3.5
print(r)
print(min(r))
'''
r = [ 1.0 , 1.5 ,-2.2]
soma = sum(r)
tamanho = len(r)
media = soma/tamanho
print("A lista é",r)
print("A soma dos elementos da lista é",soma)
print(f"A lista contém {tamanho} elementos")
print("A média dos elementos é",media)
print("O menor elemento é",min(r))
print("O maior elemento é",max(r))'''

'''
from math import log2,sqrt
r = [ 1,4,16,64]
lr2 = list(map(log2,r))
sr = list(map(sqrt,r))
print("A lista é",r)
print("Aplicar log2 resulta em",lr2)
print("Aplicar sqrt resulta em",sr)
'''
'''
r = [ 1, 4,16,64]
print("A lista é",r)
r.append(256)
print("Agora a lista é",r)
r.append(1024)
print("Agora a lista é",r)
'''
'''
r = []
print("A lista é",r)
r.append(2)
r.append(4)
r.append(6)
r.append(7)
print("Agora a lista é",r)
r.pop()
print("Agora a lista é",r)
'''
'''
r = [1,3,5,7,9,11,13]
print("A lista é",r)
s =r[2:5]
print("O terceiro, o quarto e o elemento forma a lista",s)
t = r[:5]
print("Até o quinto elemento a lista é",t)
u = r[2:]
print("A partir do terceiro elemento a lista é",u)
'''
'''
r = [1,3,5]
print("A primeira lista é",r)
s = [7,9,11]
print("A segunda lista é ",s)
print("A soma das duas listas resulta em ",r+s)
'''
'''
from numpy import array
r1 = [ 1,3,5]
r2 = [ 7,9,11]
print(f"As listas são {r1} e {r2}")
print(f"A soma das arrays resulta em {r1 + r2}")
a1 = array(r1,int)
a2 = array(r2,int)
print(f"As arrays sao {a1} e {a2}")
print(f"A soma das arrays resulta em {a1 + a2}")
'''
'''

from numpy import array
v = array([8,6,4],float)
print("O vetor é",v)
a = array([ [1,3,5], [7,9,11] ],float)
print("A matriz é",v)
print(a)
print("O primeiro elemento do vetor é",v[0])
print("O elemento no canto inferior direito da matriz é",a[1,2])
'''