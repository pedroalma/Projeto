pontuacao = int(0)

print("Olá, Bem-vindo ao programa de perguntas!")

print("Pergunta 01: ")

print("Qual o maior planeta do Sistema Solar? (2Pts) ")

print("A - Marte")
print("B - Júpiter") #alternativa correta
print("C - Terra")
print("D - Vênus")

pergunta = str(input("Selecione uma alternativa correta: "))

if ((pergunta == "B") or (pergunta == "b")) :
    pontuacao += (2)
    totalPts = (pontuacao)
    print("Resposta correta!")
    print(f"Sua quantidade de pontos atual é: {totalPts}")
elif (pergunta == "A") or (pergunta == "a") or (pergunta == "C") or (pergunta == "c") or (pergunta == "D") or (pergunta == "d") :
    pontuacao += (0)
    totalPts = (pontuacao)
    print("Resposta incorreta!")
    print(f"Sua quantidade de pontos atual é: {totalPts} ")
else: 
    print("OPÇÃO INVÁLIDA")
# ---------------------------------------------------------------------#  
print("Pergunta 02: ")

print("Qual Elemento Químico tem o símbolo O? (2Pts) ")

print("A - Ouro")
print("B - Orto") 
print("C - Ósmio")
print("D - Oxigênio") #alternativa correta

pergunta = str(input("Selecione uma alternativa correta: "))

if ((pergunta == "D") or (pergunta == "d")) :
    pontuacao += (2)
    totalPts = (pontuacao)
    print("Resposta correta!")
    print(f"Sua quantidade de pontos atual é: {totalPts}")
elif (pergunta == "A") or (pergunta == "a") or (pergunta == "C") or (pergunta == "c") or (pergunta == "B") or (pergunta == "b") :
    pontuacao += (0)
    totalPts = (pontuacao)
    print("Resposta incorreta!")
    print(f"Sua quantidade de pontos atual é: {totalPts} ")
else: 
    print("OPÇÃO INVÁLIDA")

# --------------------------------------------------------------------#

print ("Pergunta 03: ")

print ("Qual o resultado da operação 9x8 ? (2Pts) ")

print ("A - 56")
print ("B - 63")
print ("C - 72") #alternativa correta
print ("D - 81")

pergunta = str(input ("Selecione uma alternativa correta "))

if ((pergunta == "C") or (pergunta == "c")) :
   pontuacao += (2) 
   totalPts = (pontuacao)
   print ("Resposta correta!")
   print (f"Sua quantidade de pontos atual é : {totalPts}")
elif (pergunta == "A") or (pergunta == "a") or (pergunta == "B") or (pergunta == "b") or (pergunta == "D") or (pergunta == "d")  :
    pontuacao += (0)
    totalPts = (pontuacao)
    print ("Resposta incorreta!")
    print (f"Sua quantidade de pontos atual é {totalPts}")
else:
   print ("OPÇÃO INVÁLIDA")

# --------------------------------------------------------------------#

print ("Pergunta 04: ")

print ("Qual é a capital da Austrália? (2Pts) ")

print ("A - Sydney") 
print ("B - Melbourne")
print ("C - Canberra") #alternativa correta
print ("D - Brisbane")

pergunta = str(input ("Selecione uma alternativa correta "))

if ((pergunta == "C") or (pergunta == "c")) :
   pontuacao += (2) 
   totalPts = (pontuacao)
   print ("Resposta correta!")
   print (f"Sua quantidade de pontos atual é : {totalPts}")
elif (pergunta == "A") or (pergunta == "a") or (pergunta == "B") or (pergunta == "b") or (pergunta == "D") or (pergunta == "d")  :
    pontuacao += (0)
    totalPts = (pontuacao)
    print ("Resposta incorreta!")
    print (f"Sua quantidade de pontos atual é {totalPts}")
else:
   print ("OPÇÃO INVÁLIDA")

#--------------------------------------------------------------------------------------#

print ("Pergunta 05: ")

print ("Quem pintou o famoso quadro Mona Lisa? (2Pts) ")

print ("A - Vincent van Gogh")
print ("B - Pablo Picasso")
print ("C - Claude Monet") 
print ("D - Leonardo da Vinci") #alternativa correta

pergunta = str(input ("Selecione uma alternativa correta "))

if ((pergunta == "D") or (pergunta == "d")) :
   pontuacao += (2) 
   totalPts = (pontuacao)
   print ("Resposta correta!")
   print (f"Sua quantidade de pontos atual é : {totalPts}")
elif (pergunta == "A") or (pergunta == "a") or (pergunta == "B") or (pergunta == "b") or (pergunta == "C") or (pergunta == "c")  :
    pontuacao += (0)
    totalPts = (pontuacao)
    print ("Resposta incorreta!")
    print (f"Sua quantidade de pontos atual é {totalPts}")
else:
   print ("OPÇÃO INVÁLIDA")

#--------------------------------------------------------------------------------------#

print (" Pergunta BÔNUS: ")

print ("Quem é considerado o Pai da Computação? (3Pts) ")

print ("A - Steve Jobs")
print ("B - Alan Turing") #alternativa correta
print ("C - Bill Gates") 
print ("D - Charles Babbage") 

pergunta = str(input ("Selecione uma alternativa correta "))

if ((pergunta == "B") or (pergunta == "b")) :
   pontuacao += (3) 
   totalPts = (pontuacao)
   print ("Resposta correta!")
   print (f"Sua quantidade de pontos final é : {totalPts}")
elif (pergunta == "A") or (pergunta == "a") or (pergunta == "C") or (pergunta == "c") or (pergunta == "D") or (pergunta == "d")  :
    pontuacao -= (2)
    totalPts = (pontuacao)
    print ("Resposta incorreta!")
    print (f"Sua quantidade de pontos final é : {totalPts}")
else:
   print ("OPÇÃO INVÁLIDA")

print("SUA PONTUAÇÃO: ")


if(totalPts) > (10) or (totalPts) == (10) :
   print(f"Você é um mestre! Pontuação final: {totalPts}")
elif(totalPts == 0) or (totalPts <= 2) :
  print(f"Sem recompensa! Pontuação final: {totalPts}")
elif(totalPts == 3) or (totalPts <= 5) : 
  print(f"Bronze! Pontuação final: {totalPts}")
elif(totalPts == 6) or (totalPts <= 8) :
   print(f"Prata! Pontuação final: {totalPts}")
elif(totalPts == 9) or (totalPts <= 10) : 
   print(f"Ouro! Pontuação final: {totalPts}")
  