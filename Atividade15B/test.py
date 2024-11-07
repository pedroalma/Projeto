'''
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
    print("seu menor numero e",min(r)))
'''
f1 = 0
f2 = 0
f3 = 0 
nome = False
while not nome:
    for x in range(3,-1,-1):
        if x ==3:
              f0 = int(input("um numero"))
              f1 = f0 
        elif x ==2:
              f0 = int(input("um numero"))
              f2 = f0 
        elif x ==1:
              f0 = int(input("um numero"))
              f3 = f0         
        if x == 0:
            nome = True 
            r =[f1,f2,f3]
            print("seu menor numero e",min(r))      