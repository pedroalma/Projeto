'''uma_lista = [1, 2, 3, 4,7]
outra_lista = [3, 4, 5, 6,7]


print(set(uma_lista) & set(outra_lista))'''
uma_lista = ['oi','ba','ba', 'bem', 'certo']
outra_lista = ['oi','ba','ba','belo', 'jeito']
iguais = [elemento for elemento in uma_lista if elemento in outra_lista]
print(iguais)

