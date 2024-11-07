'''import numpy as np

# Criar um array de tamanho 5
a = np.empty(5, dtype=object)  # Usando dtype=object para permitir strings

# Preencher o array com strings vazias
a.fill("*")

# Exibir o array sem mostrar os apóstrofos
print(' '.join(a))  # Saída: (nada aparece, porque são strings vazias)
'''
'''a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))'''
'''print("The below program uses join() method for joining list with specified separator:")
print("\n")
l = ['1', '2', '3', '4']
print("The given list is as follows:")
print(l)
print("\n")
sptr = '_'
print("The obtained list after joining the given list with given separator")
print(sptr.join(l))'''
'''string = " ###Hello, word! "
trimmed_string = string.lstrip("#")
print(string)
print(trimmed_string)'''
import re

texto = "Aqui está um texto com apóstrofe: 'exemplo'."
texto_sem_apostrofe = re.sub(r"'", "", texto)
print(texto_sem_apostrofe)