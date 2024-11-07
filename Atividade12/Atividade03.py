

print("Olá, Bem-vindo!")

print('''Para calcular a distância e o quadrante de um ponto,
       insira abaixo as coordenadas X e Y: 
      ''')

coordenadaX = float(input("Digite a coordenada X: "))

coordenadaY = float(input("Digite a coordenada Y: "))

print('''======================# Quadrante #=====================''')

if (coordenadaX) > (0) and coordenadaY > (0) :
    print("O ponto está localizado no Quadrante I")

elif (coordenadaX) < (0) and coordenadaY > (0) :
    print("O ponto está localizado no Quadrante II")

elif (coordenadaX) < (0) and coordenadaY < (0) :
    print("O ponto está localizado no Quadrante III")

elif (coordenadaX) > (0) and coordenadaY < (0) :
    print("O ponto está localizado no Quadrante IV")

elif (coordenadaX) == (0) and coordenadaY == (0) :
    print("O ponto está localizado na Origem do plano.")

elif (coordenadaY) == (0) :
    print("O ponto está localizado sobre o eixo X")

elif (coordenadaX) == (0) :
    print("O ponto está localizado sobre o eixo Y")

# -----------------------# Formúla calculo distância # -----------------------# 

formulaCalculoDistancia = (f"{(coordenadaX ** (2) + coordenadaY ** (2)) ** (0.5)}")

print('''======================# Distância #=====================''')

print(f"A distância do ponto até a origem: {formulaCalculoDistancia:.4}")
