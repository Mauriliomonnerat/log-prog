contador = 0
valor_total = 0
valor_desconto = 0.0

while True:
    valor_produto = float(input ("Digite o valor do produto: "))

    if valor_produto == 0:
        print (f"O total de clientes foi de {contador} e o valor total de compras foi {valor_total}")
        break
    
    contador += 1

    while valor_produto != -1:
        valor_total += valor_produto
        valor_produto = float(input ("Digite o valor do produto: "))
    print (valor_total)
        
    if valor_total > 200:
        valor_desconto = valor_total * 0.10
        print (f"Seu desconto foi de {valor_desconto} Reais")

    elif valor_total > 100:
        valor_desconto = valor_total * 0.05
        print (f"Seu desconto foi de {valor_desconto} Reais")

    else:
        print (f"Você não teve desconto")

    parcelas = int(input ("De 1 a 6, digite o número de parcelas desejadas: "))

    if parcelas <= 6:
        valor_parcela = valor_total/parcelas
        for i in range(0,parcelas):
            i += 1
            print (f'No mês {i} o valor da parcela será {valor_parcela}')