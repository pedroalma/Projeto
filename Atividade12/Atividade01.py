
'''Crie um programa de triagem médica que classifique os pacientes com base em seus sintomas e na faixa etária. 
O programa deve: Pedir ao usuário que''' '''insira seu nome, idade e sintomas de uma lista pré-definida''' '''(por exemplo: dor intensa, dificuldade respiratória, fraturas, febre).
Classificar os pacientes nas seguintes categorias, considerando a idade:

Emergência: dor intensa, dificuldade respiratória grave, perda de consciência (todas as idades).

Grave: fraturas visíveis, sangramentos moderados (todas as idades).

Preferencial: febre alta persistente, dores leves (todas as idades).

Classificação de risco:
Crianças (0-12 anos) e idosos (acima de 65 anos) têm prioridade nas classificações "Emergência" e "Grave".
Exibir um resumo da classificação e informações do paciente no final.
'''
'''nome = str (input("seu nome "))
idade = int(input("a idade "))
print(" os sintomas ")
si1 = int(input("dor = 1  nao = 0 ")) 
if si1 == 1:
    si11 = int(input("dores leves ? 1 = sim  nao = 0 "))
    si12 = int(input("dor intensas ? 1 = sim  nao = 0 "))
si2 = int(input(" dificuldade respiratória = 2 nao = 0 "))
if si2 == 2:
    si22 = int(input("grave ? 1 = sim  nao = 0 "))
si3 = int(input("fraturas = 3 nao = 0 "))
if si3 == 3 :
    si33 = int(input("fraturas visíveis ? 1 = sim  nao = 0 "))
si4 = int(input("febre = 4  nao = 0 "))
if si4 == 4 :
    si44 = int(input(" febre alta persistente ? 1 = sim  nao = 0 "))
si5 = int(input("perda de consciência = 5 nao = 0 "))'''

nome = str(input("Insira seu nome: "))
idade = int(input("Insira sua idade: "))
atendimentoPrioritario = int
print ("Selecione um sintoma: 1 - Dor intensa | 2 - Dificuldade respiratória grave | 3 - Perda de consciência ") #Emergência
print ("4 - Fraturas visiveis | 5 - Sangramentos Moderados") #Grave
print ("6 - Febre alta persistente | 7 - Dores leves") #Preferencial          
sintoma = int(input("Digite o número que corresponde ao sintoma: "))
if sintoma == 1:
    n1 = str("Dor intensa")
elif sintoma == 2:
    n1 = str("Dificuldade respiratória grave")
elif sintoma == 3:
    n1 = str("Perda de consciência")
elif sintoma == 4:
    n1 = str("Fraturas visiveis")
elif sintoma == 5:
    n1 = str("Sangramentos Moderados")
elif sintoma == 6:
    n1 = str("Febre alta persistente")
elif sintoma == 7:
    n1 = str("Dores leves")
 
if sintoma <= 0 or sintoma >8 :
    print("OPÇÃO INVÁLIDA!")
elif sintoma > 0 or sintoma <=7:
    if idade <= 12 or idade >= 65 and sintoma == 1 or sintoma == 2 or sintoma == 3 :
       atendimentoPrioritario = 2
       classificacaoDeRisco = "Emergência"
 
    elif idade <= 12 or idade >= 65 and sintoma == 4 or sintoma == 5 :
       atendimentoPrioritario = 1
       classificacaoDeRisco = "Grave"
   
    elif idade > 12 or idade < 65 and sintoma == 1 or sintoma == 2 or sintoma == 3 :
       atendimentoPrioritario = 2
       classificacaoDeRisco = "Emergência"
 
    elif idade > 12 or idade < 65 and sintoma == 4 or sintoma == 5 :
       atendimentoPrioritario = 2
       classificacaoDeRisco = "Grave"  
 
    print("Informações do Paciente:")
    print(f"nome: {nome} idade: {idade}  sintoma: {sintoma}-{n1} classificação de risco: {classificacaoDeRisco}")
    #print("nome :" , nome)
 
    if atendimentoPrioritario == 1:
        print("ATENDIMENTO PRIORITÁRIO")
    elif atendimentoPrioritario == 2:  
        print("ATENDIMENTO SEM PRIORIDADE")  

