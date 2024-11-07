a1 = []
a2 = []
a3 = []
for n in range(13):
    if n in range(1,5):
        v1 = int(input("nota do primeiro aluno "))
        print(n)
        a1.append(v1)
    elif n in range(5,9):
        v2 = int(input("nota do segundo aluno "))
        print(n)
        a2.append(v2)
    elif  n in range(9,13):
        v3 = int(input("nota do terceiro aluno "))
        print(n)
        a3.append(v3)        
if n == 12:         
    print("a media do primeiro aluno",sum(a1)/len(a1))        
    print("a media do segundo aluno",sum(a2)/len(a2))     
    print("a media do terceiro aluno",sum(a3)/len(a3))              