f1 = 0
f2 = 0
f3 = 0 
nome = False 
while not nome:
    f1 = int(input("um numero"))
    f2 = int(input("um numero"))
    f3 = int(input("um numero"))
    nome = True
    r =[f1,f2,f3]
    print("seu maior numero e",max(r))