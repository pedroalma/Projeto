print("1. Candidato Jair Rodrigues")
print("2. Candidato Carlos Luz ")
print("3. Candidato Neves Rocha ")
print("4. Nulo ")
print("5. Branco")
jair = (0)
luz = (0)
neves = (0)
nulo = (0)
branco = (0)
n = (1)
vota = int(input(""))
votav = False
while vota and not votav:
   if vota == 1:
      jair = (jair + n)
      print("1. Candidato Jair Rodrigues")
      print("2. Candidato Carlos Luz ")
      print("3. Candidato Neves Rocha ")
      print("4. Nulo ")
      print("5. Branco")    
      vota = int(input(""))
   elif vota == 2:
      luz = luz + n
      print("1. Candidato Jair Rodrigues")
      print("2. Candidato Carlos Luz ")
      print("3. Candidato Neves Rocha ")
      print("4. Nulo ")
      print("5. Branco")    
      vota = int(input(""))
   elif vota == 3:
      neves = neves + n  
      print("1. Candidato Jair Rodrigues")
      print("2. Candidato Carlos Luz ")
      print("3. Candidato Neves Rocha ")
      print("4. Nulo ")
      print("5. Branco")    
      vota = int(input(""))
   elif vota == 4:
      nulo = nulo + n  
      print("1. Candidato Jair Rodrigues")
      print("2. Candidato Carlos Luz ")
      print("3. Candidato Neves Rocha ")
      print("4. Nulo ")
      print("5. Branco")    
      vota = int(input(""))
   elif vota == 5:
      branco = branco + n
      print("1. Candidato Jair Rodrigues")
      print("2. Candidato Carlos Luz ")
      print("3. Candidato Neves Rocha ")
      print("4. Nulo ")
      print("5. Branco")    
      vota = int(input(""))
   elif vota == 6:
      r = [ [jair,"Jair Rodrigues "] , [luz,"Carlos Luz"] , [neves,"Neves Rocha"] , [nulo,"nulos"] , [branco,"Branco"]]
      if luz < jair >  neves :
            print(f"jair Rodrigues venceu com {jair} votos ")
            fim = "votacoes encerradas"  
      elif jair < luz > neves:
            print(f"Carlos Luz venceu com {luz} votos ")
            fim = "votacoes encerradas"
      elif jair < neves > luz:
            print(f"Neves Rocha venceu com {neves} votos ")  
            fim = "votacoes encerradas"
      elif jair == luz:
         print("Jair Rodrigues e Carlos Luz vao para o segundo turno")
         fim = "segundo turno"
      elif jair == neves:
         print("Jair Rodrigues e Neves Rocha vao para o segundo turno")
         fim = "segundo turno"
      elif luz == neves:
           print("Carlos Luz e Neves Rocha vao para o segundo turno")  
           fim = "segundo turno"
      '''if  nulo > jair and luz and neves and branco:
         maiort = "nulos"  
      elif branco > jair and luz and neves and nulo:
         maiort = "brnco"
      elif jair > luz and neves and branco and nulo:
         maiort = "jair"
      elif luz > jair and neves and branco and nulo:
         maiort = "luz"
      elif neves > luz and jair and branco and nulo:  
         maiort = "neves"
      elif jair == luz:
         maiort = "jair e luz"
      elif jair == neves:
         maiort = "jair e neves"
      elif luz == neves:  
         maiort = "luz e neves"
      elif nulo == branco:
         maiort = "nulos e brancos"  '''   
      total = jair + luz + neves + nulo + branco                   
      print("total de votos",total)
      print( "porcemtagem nulo", (total*nulo)/100)
      print("poncentagem branco",(total*branco)/100)
      print(f"numero maior de votos {max(r)}")
      print(fim)
      print(f"total de votos: Candidato Jair Rodrigues {jair} \nCandidato Carlos Luz {luz} \nCandidato Neves Rocha {neves} \nNulo {nulo} \nBranco {branco}")
      votav = True
      

'''
print("1. Candidato Jair Rodrigues")
print("2. Candidato Carlos Luz ")
print("3. Candidato Neves Rocha ")
print("4. Nulo ")
print("5. Branco")
jair = (0)
luz = (0)
neves = (0)
nulo = (0)
branco = (0)
n = (1)
vota = int(input(""))
while vota:
   if vota == 1:
      jair = (jair + n)
      print("1. Candidato Jair Rodrigues")
      print("2. Candidato Carlos Luz ")
      print("3. Candidato Neves Rocha ")
      print("4. Nulo ")
      print("5. Branco")     
      vota = int(input(""))
   elif vota == 2: 
      luz = luz + n
      print("1. Candidato Jair Rodrigues")
      print("2. Candidato Carlos Luz ")
      print("3. Candidato Neves Rocha ")
      print("4. Nulo ")
      print("5. Branco")     
      vota = int(input(""))
   elif vota == 3: 
      neves = neves + n  
      print("1. Candidato Jair Rodrigues")
      print("2. Candidato Carlos Luz ")
      print("3. Candidato Neves Rocha ")
      print("4. Nulo ")
      print("5. Branco")     
      vota = int(input(""))
   elif vota == 4: 
      nulo = nulo + n  
      print("1. Candidato Jair Rodrigues")
      print("2. Candidato Carlos Luz ")
      print("3. Candidato Neves Rocha ")
      print("4. Nulo ")
      print("5. Branco")     
      vota = int(input(""))
   elif vota == 5: 
      branco = branco + n 
      print("1. Candidato Jair Rodrigues")
      print("2. Candidato Carlos Luz ")
      print("3. Candidato Neves Rocha ")
      print("4. Nulo ")
      print("5. Branco")     
      vota = int(input(""))
   elif vota == 6:
      r = [jair , luz , neves , nulo , branco]
      if jair > luz > neves :
         print("jair vence",max(r))
      print(max(r))
      print("fim")     
      print(f"Candidato Jair Rodrigues {jair} Candidato Carlos Luz {luz} Candidato Neves Rocha {neves} Nulo {nulo} Branco {branco}")
      break
'''