# REVISÃO
# Exercício 1: Somatório Condicional em Intervalo Fechado
# Desenvolva um programa que solicite dois números inteiros representando os
# limites de um intervalo [A, B] (garantindo que A ≤ B). O programa deve iterar sobre
# o intervalo utilizando uma estrutura de repetição e calcular a soma apenas dos
# números ímpares presentes nele, exibindo o resultado final ao usuário.

# lista = []

# numero1 = int(input("Digite o primeiro número: "))
# lista.append(numero1)

# numero2 = int(input("Digite o segundo número: "))
# while numero2 < numero1:
#     numero2 = int(input("Digite um número maior que o primeiro número: "))

# lista.append(numero2)

# numero_novo = numero1
# lista2 = []

# while numero_novo < numero2:
#     numero_novo = numero_novo + 1
#     lista2.append(numero_novo)

# soma = 0

# for numero in lista2:
#     if numero % 2 != 0:
#         soma += numero

# print(f"A soma dos valores ímpares deu: {soma}")


# Exercício 2: Frequência e Ocorrência de Elemento em Lista
# Construa um programa que leia 10 números inteiros, armazene-os em uma lista e,
# em seguida, solicite um número adicional para consulta. O sistema deve verificar e
# exibir se esse valor está presente no vetor e a quantidade exata de vezes que ele se
# repete.

# lista = []
# for i in range (3):
#     numero1 = int(input("Digite um número: "))
#     lista.append(numero1)

# contador = 0

# numero2 = int(input("Digite outro número: "))
# for numero in lista:
#     if numero == numero2:
#         contador += 1

# if contador > 0:
#     print(f"O número {numero2} já existe {contador} vezes na lista.")
# else:
#     lista.append(numero2)
#     print("O número não existe na lista, então foi adicionado.")


# Exercício 3: Análise Térmica Semanal e Filtro de Desvio
# Implemente um programa que receba as temperaturas médias registradas durante
# os 7 dias da semana (armazenadas em um vetor de números reais). O programa
# deve calcular a média aritmética semanal e, em seguida, exibir quais temperaturas
# registradas ficaram estritamente abaixo dessa média.

# lista = []
# for i in range (5):
#     temperatura = float(input(f"Digite a temperatura do {i+1}º dia da semana: "))
#     lista.append(temperatura)

# media = sum(lista)/len(lista)

# #Versão 1
# for j in range (len(lista)):
#     if lista[j] < media:
#         print(f"A média foi {media} e a Temperatura {lista[j]} do dia {j+1} ficou abaixo da média.")

#Versão 2
# for numero in lista:
#     if numero < media:
#         print(f"A média foi {media} e a Temperatura {numero} ficou abaixo da média.")


# Exercício 4: Mapeamento Condicional de Vetor
# Construa um programa que receba 8 números inteiros e os guarde em um vetor. Em
# seguida, crie um segundo vetor de mesmo tamanho no qual os números ímpares do
# vetor original sejam multiplicados por 2 e os números pares permaneçam
# inalterados. Ao final, exiba os dois vetores.

# lista_1 = []
# for i in range (3):
#     a = float(input("Digite o numero: "))
#     lista_1.append(a)

# lista_2 = lista_1.copy()

# for j in range (len(lista_2)):
#     if lista_2[j] % 2 != 0:                      
#         lista_2[j] = lista_2[j] * 2     

# print (lista_1)
# print (lista_2)


# Exercício 5: Contagem de Valores Menores que um Limiar em Matriz 
# Retangular 
# Desenvolva um programa que leia os valores de uma matriz  
# 2 × 4
# de números 
# inteiros. O programa deve contar quantos valores estão abaixo de um limiar, que 
# também será informado pelo usuário, estão presentes na estrutura e exibir a 
# contagem total, além de imprimir a matriz completa formatada em linhas e colunas.

# matriz = []
# for i in range(2):
#     linha = []
#     for j in range (4):
#         numero = int(input("Digite um número: "))
#         linha.append(numero)
#     matriz.append(linha)

# limiar = int(input("Digite um limiar: "))

# contador = 0
# for i in range (2):
#     for j in range(4):
#         if matriz[i][j] < limiar:
#             contador += 1

# print(f"{contador} numeros ficaram abaixo do limiar")

# for i in range (2):
#     for j in range(4):
#         print (matriz[i][j], end=" ")        # Depois de imprimir o número, coloque apenas um espaço. Não pule de linha.
#     print()                                  # Serve para pular a linha.


# Exercício 6: Multiplicação de Matriz por Escalar 
# Desenvolva um programa que solicite o preenchimento de uma matriz  
# 3 × 3 com números inteiros e, em seguida, peça ao usuário um valor numérico constante 
# (escalar). Utilizando laços de repetição aninhados, o programa deve multiplicar cada 
# elemento da matriz original por esse valor escalar e exibir a matriz resultante 
# formatada em linhas e colunas.

matriz = []
for i in range(2):
    linha = []
    for j in range (2):
        numero = int(input("Digite um número: "))
        linha.append(numero)
    matriz.append(linha)


escalar = int(input ("Digite um número escalar: "))

matriz_b = []
for l in range(2):
        linha_b = []
        for m in range(2):
            multiplicacao = matriz[l][m] * escalar
            linha_b.append(multiplicacao)

        matriz_b.append(linha_b)

print("Primeira matriz:")
for i in range (2):
    for j in range(2):
        print (matriz[i][j], end=" ") # Depois de imprimir o número, coloque apenas um espaço. Não pule de linha.
    print()                           # Serve para pular a linha

print()  # pula uma linha

print("Segunda matriz:")
for i in range (2):
    for j in range(2):
        print (matriz_b[i][j], end=" ") 
    print()                           


# Desenvolva um programa que solicite dois números inteiros representando os
# limites de um intervalo [A, B] (garantindo que A ≤ B). 
# O programa deve iterar sobre o intervalo utilizando uma estrutura de repetição 
# e calcular a soma apenas dos
# números ímpares presentes nele, exibindo o resultado final ao usuário.

# def somarImpares(inicio, fim):

#     # while fim < inicio:
#     #     fim = int(input('Digite o segundo numero: '))
    
#     somatorio = 0
#     for i in range(inicio, fim+1): # +1 no 'b' pq tem que incluir ele
#         if i%2 != 0: # verifica se é impar
#             somatorio += i

#     return somatorio

# # inicio do programa
# a = int(input('Digite o primeiro numero: '))
# b = int(input('Digite o segundo numero: '))

# soma = somarImpares(a, b)
# print(soma)