null1 = input("Digite um numero ")
null1 = (int(null1))
null = null1 % 10
null2 = null1 % 5
null3 = null1 % 2
if null == 0 and null2 == 0 and  null3 == 0 :
    print("ele e divisivel por 10 , 5 e 2") 
elif null == 0 :
    print("ele e divisivel por 10")  
elif null2 == 0 :
    print("ele e divisivel por 5")   
elif null3 == 0 :
    print("ele e divisivel por 2 ")  
else :
    print("ele nao e divisivel por 10,5 e 2")        
print(null)
print(null2)
print(null3)
print(type(null))
print(type(null2))
print(type(null3))