# usuario digita uma nota
# programa verifica e só aceita se estiver
# entre 0 e 10, caso contrario, peça para digital de novo

nota = float(input("Digite a nota: "))

while nota < 0 or nota > 10:                                           # Enquanto ele digita uma nota menor que 0 e maior que 10, ele vai pro print e depois pro input
    print(f"Você digitou {nota}, mas ela deve estar entre 0 e 10")     # Mas se ele digitar algo entre esse intervalo, não vai pro while
    nota = float(input("Digite a nota: "))



# while not (nota>= 0 and nota <=10)
# pass
# aqui ele nega o que ta certo