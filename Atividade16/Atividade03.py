r = []
a =  ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
for n in range(10):
   c =  input("um caracter ").lower() 
   r.append(c)
#iguais = [ele for ele in r if ele in a]
#print(a)
#print(r)
#print(iguais) 
#oau
print(set(r) & set(a))