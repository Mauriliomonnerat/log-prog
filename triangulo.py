lado1 = int(input("Digite o primeiro lado do triângulo: "))
lado2 = int(input("Digite o segundo lado do triângulo: "))
lado3 = int(input("Digite o terceiro lado do triângulo: "))

condiexis = (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1)

if condiexis:
    pass

else: 
    print("Números inválidos para condição de existência") 
    
if (lado1 == lado2) and (lado2 == lado3):
    print("Este é um triângulo Equilátero") 

elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
    print("Este é um triângulo Isósceles") 

else:
    print("Este é um triângulo Escaleno") 