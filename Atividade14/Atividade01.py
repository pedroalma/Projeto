'''Escrever um algoritmo que lê 5 valores, um de cada vez, e conta quantos destes valores são negativos, escrevendo esta informação.'''
n = 0
null1 = 0 
null2 = 0
null3 = 0 
null4 = 0
null5 = 0
null = int(input("insira um nomero: "))
for x in range(4,-1,-1):
    if x == 5:
        null = int(input("1-insira um nomero: "))
        null1 = null 
    elif x == 4:
        null = int(input("2-insira um nomero: "))
        null2 = null
    elif x == 3:
        null = int(input("3-insira um nomero: "))
        null3 = null 
    elif x == 2:
        null = int(input("4-insira um nomero: "))
        null4 = null
    elif x == 1:
        null = int(input("5-insira um nomero: "))
        null5 = null 
r=[null1,null2,null3,null4,null5]
if n == 0:
        if r[0] < 0:
            print("seu numero e negativo",r[0])
        if r[1] < 0:
            print("seu numero e negativo",r[1])
        if r[2] < 0:
            print("seu numero e negativo",r[2])
        if r[3] < 0:
            print("seu numero e negativo",r[3])    
        if r[4] < 0:
            print("seu numero e negativo",r[4])        