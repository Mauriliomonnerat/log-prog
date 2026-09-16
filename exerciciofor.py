numero = int(input("Digite um número: "))

for i in range (0,10):                         #aqui ele cria uma lista com número de 0 a 9
    resultado = numero * (i+1)                 #aqui ele ta multiplicando o numero pelos numeros criado pela tabela i
    print (f"{numero} x {i+1} = {resultado}" )


