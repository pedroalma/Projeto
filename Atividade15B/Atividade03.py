f1,f2 =  0,1
f4 = int(input("determine qual o intervalo da contagem "))
while f1 <= f4:
    f3 = f1%2 
    f1 = f1+f2
    if f3 == 0:
        print(f1)