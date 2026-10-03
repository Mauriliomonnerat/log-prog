#EXERCÍCIO 1

#lista = []

#carros = ['Ferrari', 'Monza', 'Palio']
                                            # O LEN mostra a quantidade de elementos que tem dentro do array.
#for i in range (len(carros)):              # Para cada posição(número) gerada dentro RANGE, o FOR atribui essa posição como número ao i.
    #print(f'{i+1} - {carros[i]}')          # O RANGE não gera exatamente uma "posição"; ele gera números. Nesse caso, esses números representam as posições da lista.
                                            # For i in range(...) é útil quando você precisa da posição do elementro dentro da lista (i).



#EXERCÍCIO 2

#lista = []
#for i in range(0,3):                                # O range cria um laço de repetição de passagens que inicia no 0 e vai até o 2, ou seja, repita 3 vezes.
    #numero = int(input("Digite um número: "))       # Então ele fala "FOR" você vai fazer uma passagem e atribua o valor dessa passagem ao i.
    #lista.append(numero)                            # Só que a primeira passagem é atribuída como 0.

#for numero in list:                  # Percorra cada elemento (que vou chamar de numero) dentro da lista!
    #if numero > 10:                  # Se o elemento for maior que 10.
        #print(numero) 



#EXERCÍCIO 3

#lista = []

#nomes = ['Bruna', 'André', 'Caio']

#lista.sort()                           # O SORT ordena a lista de forma crescente.

#lista.sort(reverse = True)             # O REVERSE ordena a lista de forma decrescente.

#lista = sorted(nomes)                 # O SORTED ordena e salva a lista em outro local (cria outra lista).

#nomes.insert(2, "Maurilio")            # O INSERT insere, na posição que você quer, o que você quer.



# EXERCÍCIO 4

#maiores_que_10 = (                  
#    [numero for numero in lista if numero > 10])   #Aqui vai apresentar os numeros > 10 dentro da lista na variável maiores_que_10.



# EXERCÍCIO 5

#cont1 = 0
#cont2 = 0

# for i in range(0,7):                                
#     numero = int(input("Digite um número: "))                                  
    #if numero % 2 == 0:
        #cont1 += 1    
    #elif numero % 2 != 0:
        #cont2 += 1

#print(f" Você digitou {cont1} números pares e {cont2} números impares." )
             
        
             
# EXERCÍCIO 6

# lista = []

# for i in range(0,3):                                
#      numero = int(input("Digite um número: "))         
#      lista.append(numero)
#      lista.sort()
     
# print (lista)

  
 
# EXERCÍCIODE SUBSTITUIÇÃO DE VALORES

# lista = []
# for i in range (0,3):
#     numero = int(input("Digite o número: "))
#     lista.append(numero)  

# for numero in lista:
#     if numero < 0:
#         posicao = lista.index(numero)  #Guarde essa posição
#         lista.remove(numero)           #Remova o número dessa posição
#         lista.insert(posicao,0)        #Insira 0 nessa posição
        
#     else:
#         print (lista)
# print(lista)



# EXECÍCIOS DE IDENTIFICAÇÃO DE NÚMEROS IGUAIS

# lista = []
# for i in range (0,3):
#    numero = int(input("Digite o número: "))
#    lista.append(numero)

# numero1 = int(input("Digite um número adicional: "))
# for numero in lista:
#     if numero == numero1:
#         posicao = lista.index(numero)
#         print("Este número já foi inserido e está na posição: ", posicao+1)
#         break
        
#     else:
#         lista.append(numero1)
#         print(lista)
#         break



#EXERCÍCIO MEDIA

# lista = []
# for i in range (0,3):
#     nota = int(input("Digite a nota: "))
#     lista.append(nota)

# media = sum(lista)/len(lista)

# acima_media = []
# for nota in lista:
#     if nota > media or nota == 6:
#         acima_media.append(nota)

# if len(acima_media) > 0:
#     print(f"{len(acima_media)} notas ficaram acima da média e foram as notas {acima_media}")

# else:
#     print("Nenhuma nota ficou acima da média")
    

# INVERSÃO DE VERTOR

# lista = []
# for i in range (0,3):
#     nota = int(input("Digite a nota: "))
#     lista.append(nota)

# lista_2 = lista.copy()        #Copiei o vetor
# lista_2.reverse()
# print(lista_2)


# MAIOR E MENOR

# lista = []
# for i in range (0,3):
#     nota = int(input("Digite a nota: "))
#     lista.append(nota)
#     menor = min(lista)
#     maior = max(lista)
# print(f"O maior número é o {maior} e ele está na posição {lista.index(maior)+1}")
# print(f"O maior número é o {menor} e ele está na posição {lista.index(menor)+1}")

        
# #ESTUDAR
# lista = [0,1,9,-5,8]
# j = 0
# lista_inversa = []
# for i in range ((len(lista)-1, -1,1)):
#     lista_inversa [j] = lista[i]
#     j = j + 1


# garagem = [["Land Rover", 2014], 
#            ["Palio 97", 1997],
#            ["Gol", 2022]]

# for carro in garagem:                   # aqui ele só coloco um colchete porque com o for in ele já está dentro
#    print(f"{carro[0]}, ano {carro[1]}") # ele vai na primeira coloca que é a 0 e vai na segunda é o ano 


# Modificar um dos carros
# for i in range(0, len(garagem)):
#    if i == 0:
#       garagem[i][0] = "Ferrari F430"
      # o i vai percorrer qual linha 
      # o 0 vai na coluna

# Construa um programa onde o usuário digitará dez números. O programa
# deverá calcular quais deles são maiores que dez.

# lista = []
# for i in range (0,3):
#     numero = int(input("Digite um número: "))
#     lista.append(numero)

# for numero_maior in lista:
#     if numero_maior> 10:
#         print (numero_maior)


# Construa um programa onde o usuário digitará sete números e o programa
# escreverá, na tela, quantos deles são pares e quantos são ímpares.

# lista = []
# for i in range (0,3):
#     numero = int(input("Digite um número: "))
#     lista.append(numero)

# contador_par = 0
# contador_impar = 0

# for numero in lista:
#     if numero % 2 == 0:
#         contador_par += 1

#     else:
#         contador_impar += 1

# print (f"Você digitou {contador_par} número pares e {contador_impar} números impares")

# Construa um programa onde o usuário digitará cinco números e o programa
# deverá colocar esses números dentro do vetor em ordem crescente.

# lista = []
# for i in range (0,3):
#     numero = float(input("Digite um número: "))
#     lista.append(numero)

# lista.sort()
# print (lista)

# Construa um programa onde o usuário digitará o nome e a média de dez
# alunos e o programa escreverá, na tela, o nome de todos com a média acima


# lista = [] #COLOCAR NO ARRAY
# for i in range (0,3):
#     nome = (input("Digite o nome: "))
#     nota = float(input("Digite a nota: "))
#     lista.append([nome, nota])

# soma = 0

# for aluno in lista:         # Aluno será cada vetor = [Maurilio, 10]
#     soma += aluno[1]        # Soma a coluna da nota

# media = soma / len(lista)   # Não pode usar o sum(lista) porque é uma matriz que contém strings

# for aluno in lista:
#     if aluno[1] > media:    
#         print (aluno[0])


# Construa um programa que o usuário digitará o nome e a idade de dez
# pessoas e o programa escreverá o nome do usuário mais novo.

# lista = []
# for i in range (0,3):
#     nome = (input("Digite o nome: "))
#     idade = float(input("Digite a idade: "))
#     lista.append([nome, idade])

# mais_novo = lista[0]

# for pessoa in lista:
#     if pessoa [1] < mais_novo[1]:
#         mais_novo = pessoa

# print("A pessoa mais nova é:", mais_novo[0])


# Construa uma página/programa onde o usuário digitará o nome e o bairro de
# dez pessoas. O programa exibirá o nome e bairro das pessoas em ordem
# alfabética.

# lista = []
# for i in range (0,3):
#     nome = (input("Digite o Nome: "))
#     bairro = (input("Digite a Bairro: "))

#     lista.append([nome, bairro])

#     cadastro[i] = [nome,bairro]

# Versão 1
#lista.sort(key=lambda lugares: lugares[1])       #Crie uma função que recebe lugares e retorna lugares[0]

#Versão 2
# def pegar_nome(pessoa):
#     return pessoa[0]
# lista.sort(key=pegar_nome)   


# for pessoa in lista:
#     print(pessoa[0], "-", pessoa[1])


# Construa uma página onde o usuário digitará o nome e a média de cinco
# alunos e o programa só aceitará a média do aluno caso ela esteja entre zero
# e dez.

# lista = []

# for i in range(0, 5):
#     nome = input("Digite o Nome: ")
#     media = float(input("Digite a Média: "))
#     while media < 0 or media > 10
#       media = float(input("Digite a Média: "))
#     lista.append([nome, media])


# print(lista)


# Construa uma matriz 2X2 e, como saída desse programa, a média 
# e a soma dos valores digitados deverão ser calculadas. ERRADO

 # matriz []                              ESTUDAR!
# for i in range (2):
#     for j in range(2):
#         matriz [i][j] = int (input("Digite um numero: "))

#Versão 1
# soma = 0
# for linha in matriz:
    # for coluna in linha:
        # soma += contador

# #Versão 2
# for i in range(len(matriz)):
#     for j in range(len(matriz[0])):



# Construa um jogo Quadrado Mágico 3X3, no qual o usuário 
# preencherá o vetor com números de um a nove (sem repetir números)
# e a soma de todas as linhas, colunas e 
# diagonais será igual a quinze.

# iniciar a matriz com o que o usuario digitar (matriz 3x3)
# matriz = []
# for i in range(3): # 3 linhas
#     linha = [] # inicia a linha vazia
#     for j in range(3): # 3 colunas
#         numero = int(input('Digite um número entre 1 e 9: '))
#         # garantir que não tenha numeros fora do intervalo 1~9
#         while numero < 1 or numero > 9:
#             numero = int(input('Digite um número entre 1 e 9: '))

#         linha.append(numero) # guarda o numero na linha

#     matriz.append(linha) # adiciona a linha completa a matriz

# # Forma 1 - logica
# soma = 0 # soma cada possibilidade
# somas = [] # guarda todas as somas em posições diferentes

# # Verificação das linhas
# for linha in matriz:
#     soma = 0
#     for numero in linha:
#         soma += numero
#     somas.append(soma)

# # Verificar colunas
# for i in range(3): # trava as colunas para 'andar' nas linhas
#     soma = 0 # cria uma variavel para somar os numeros das colunas
#     for j in range(3): # isso é para andar nas linhas
#         soma += matriz[j][i]
#     somas.append(soma)

# # verificar diagonais
# diagonal_principal = 0 # da esquerda para direita
# for i in range(3):
#     diagonal_principal += matriz[i][i]

# somas.append(diagonal_principal)

# diagonal_secundaria = 0
# for i in range(3): # da direita para esquerda
#     diagonal_secundaria += matriz[i][2-i]

# somas.append(diagonal_secundaria)

# if all(soma == 15 for soma in somas):
#     print('Vitoria')
# else:
#     print('Derrota')
