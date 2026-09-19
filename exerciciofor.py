numero = int(input("Digite um número: "))

for i in range (0,10):
    i += 1                  #aqui ele cria uma lista com número de 0 a 9
    resultado = numero * (i)                 #aqui ele ta multiplicando o numero pelos numeros criado pela tabela i
    print (f"{numero} x {i} = {resultado}" )


# para cada vez que ele repetir, coloque um numero do intervalo do loop nele, o loop é definido pelos número dentro do intervalo.