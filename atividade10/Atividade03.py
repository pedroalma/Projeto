null1 = input("valor total ")
null1 = (float(null1))
null2 = input("numero de prestacoes desejadas ")
null2 = (float(null2))
if null2 < 12:
    print("numeros de prestacoes indesejados ")
elif  null2 >= 12 and  null2 < 24:
    null3 = (null1 + (null1 * 5)/100)/null2
    null4 = null3 * null2
    print(f"voce tera {null2} prestacoes o valor de cada prestacao e {null3} ") 
elif   null2 >= 24 and  null2 < 36:
    null3 =  (null1 + (null1 * 10)/100)/null2
    null4 = null3 * null2
    print(f"voce tera {null2} prestacoes o valor dcfe cada prestacao e {null3} ")    
elif null2 >= 36:
    null3 = ( null1 + (null1 * 15)/100)/null2
    null4 = null3 * null2
    print(f"voce tera {null2} prestacoes o valor de cada prestacao e {null3} ")        
print(null1)
print(null2)
print(null3)
print(null4)
print(type(null1))
print(type(null2))
print(type(null3))
print(type(null4))