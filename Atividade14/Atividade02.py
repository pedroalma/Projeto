'''
Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles estão nos 
seguintes intervalos: [0 à 25], [26 à 50], [51 à 75] e [76 à 100]. A entrada de dados deve terminar quando for lido um número negativo.'''
n = 0
null1 = 0 
null2 = 0
null3 = 0 
null4 = 0
null5 = 0
for x in range(4,-1,-1):
    if x == 4:
        null = int(input("1-insira um nomero: "))
        null1 = null 
    elif x == 3:
        null = int(input("2-insira um nomero: "))
        null2 = null
    elif x == 2:
        null = int(input("3-insira um nomero: "))
        null3 = null 
    elif x == 1:
        null = int(input("4-insira um nomero: "))
        null4 = null
r=[null1,null2,null3,null4]
if n == 0:
    if (r[0] > n) and (r[0] < 25) :
            print(f"seu numero e {r[0]}, esta entre 0  e 25")
    else:
          print("seu numero nao esta entre 0 e 25")        
    if (r[1] > 26) and (r[1] < 50):
            print(f"seu numero e {r[1]}, esta entre 26  e 50")
    else:
          print("seu numero nao esta entre 26 e 50  ")        
    if (r[2] > 51) and (r[2] < 75):
            print(f"seu numero e {r[2]}, esta entre 51  e 75")
    else:
          print("seu numero nao esta entre 51 e 75  ")         
    if (r[3] > 76) and (r[3] < 100):
            print(f"seu numero e {r[3]}, esta entre 76  e 100")    
    else:
          print("seu numero nao esta entre 76 e 100  ")               