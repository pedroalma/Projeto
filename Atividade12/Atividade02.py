quantidadePts = int (0)
respotaCBonus = int (3)
respostaEBonus = int (-2)
respostaCA = int(0)
respostaEA = int(0)
respostaCB = int(0)
respostaEB = int(0)
print("Olá, Bem-vindo ao programa de perguntas!")
 
print("Pergunta 01: ")
 
print("Qual o maior planeta do Sistema Solar? (2Pts) ")
 
print("A - Marte")
print("B - Júpiter") #alternativa correta
print("C - Terra")
print("D - Vênus")
 
pergunta = str(input("Selecione uma alternativa correta: "))
 
if ((pergunta == "B") or (pergunta == "b")) :
    respostaCA = 2
    totalPts = (respostaCA)
    print("Resposta correta!")
    print(f"Sua quantidade de pontos atual é: {totalPts}")
elif (pergunta == "A") or (pergunta == "C") or (pergunta == "D") :
    respostaEA = 0
    totalPts = (respostaEA)
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
 
if (pergunta == "D") :
    respostaCB = 2
    totalPts = (respostaCA) + (respostaCB)
    print("Resposta correta!")
    print(f"Sua quantidade de pontos atual é: {totalPts}")
elif (pergunta == "A") or (pergunta == "B") or (pergunta == "C") :
    respostaEB = 0
    print("Resposta incorreta!")
    print(f"Sua quantidade de pontos atual é: {totalPts} ")
else:
    print("OPÇÃO INVÁLIDA")
 
 
# --------------------------------------------------------------------#
 
print ("Pergunta 03 : ")
 
print ("Qual o resultado da operação 9x8 ?")
 
print ("A - 56")
print ("B - 63")
print ("C - 72")#correta
print ("D - 81")
 
pergunta = str(input ("Selecione uma alternativa correta"))
 
if (pergunta == "C") :
   respostaCC = 2
   totalPts = (respostaCA) + (respostaCB) + (respostaCC)
   print ("Resposta correta!")
   print (f"Sua quantidade de pontos atual é : {totalPts}")
elif (pergunta == "A") or (pergunta == "B") or (pergunta == "D") :
    respostaCC = 0
    print ("Resposta incorreta!")
    print (f"Sua quantidade de pontos atual é {totalPts}")
else:
   print ("OPÇÃO INVÁLIDA")
 
 
 
# --------------------------------------------------------------------#
'''
4. **Qual foi o primeiro elemento químico a ser descoberto por meio da espectroscopia?**
  - A) Hélio *(correta)*
  - B) Hidrogênio
  - C) Oxigênio
  - D) Neônio
'''
 
print ("Pergunta 04 : ")
 
print ("Qual foi o primeiro elemento químico a ser descoberto por meio da espectroscopia?")
 
print ("A - Hélio")#correta
print ("B - Hidrogênio")
print ("C - Oxigênio")
print ("D - Neônio")
 
pergunta = str(input ("Selecione uma alternativa correta"))
 
if (pergunta == "A") :
   respostaCA = 2
   totalPts = (respostaCA) + (respostaCB) + (respostaCC)+(respostaCA)
   print ("Resposta correta!")
   print (f"Sua quantidade de pontos atual é : {totalPts}")
elif (pergunta == "B") or (pergunta == "C") or (pergunta == "D") :
    respostaCA = 0
    print ("Resposta incorreta!")
    print (f"Sua quantidade de pontos atual é {totalPts}")
else:
   print ("OPÇÃO INVÁLIDA")
 
#--------------------------------------------------------------------------------------#
'''
4. **Qual é a capital da Austrália?**
  - A) Sydney
  - B) Melbourne
  - C) Canberra *(correta)*
  - D) Brisbane
'''
print ("Pergunta 05 : ")
 
print ("Qual é a capital da Austrália?")
 
print ("A - Sydney")
print ("B - Melbourne")
print ("C - Canberra")#correta
print ("D - Brisbane")
 
pergunta = str(input ("Selecione uma alternativa correta"))
 
if (pergunta == "C") :
   respostaAC = 2
   totalPts = (respostaCA) + (respostaCB) + (respostaCC)+(respostaCC)
   print ("Resposta correta!")
   print (f"Sua quantidade de pontos atual é : {totalPts}")
elif (pergunta == "B") or (pergunta == "A") or (pergunta == "D") :
    respostaAA = 0
    print ("Resposta incorreta!")
    print (f"Sua quantidade de pontos atual é {totalPts}")
else:
   print ("OPÇÃO INVÁLIDA")
 
 
 
 
# Pergunta "3" (2.0)
 
# Pergunta "4" (2.0)
 
# Pergunta "5" (2.0)
 
# Pergunta **Bônus** (3.0)
 
 
print("SUA PONTUAÇÃO: ")
 
if(totalPts == 10) :
   print(f"Você é um mestre! Pontuação final: {totalPts}")
elif(totalPts == 0) or (totalPts <= 2) :
  print(f"Sem recompensa! Pontuação final: {totalPts}")
elif(totalPts == 3) or (totalPts <= 5) :
  print(f"Bronze! Pontuação final: {totalPts}")
elif(totalPts == 6) or (totalPts <= 8) :
   print(f"Prata! Pontuação final: {totalPts}")
elif(totalPts == 9) or (totalPts <= 10) :
   print(f"Ouro! Pontuação final: {totalPts}")