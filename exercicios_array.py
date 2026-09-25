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

#nomes.sort()                           # O SORT ordena a lista de forma crescente.

#nomes.sort(reverse = True)             # O REVERSE ordena a lista de forma decrescente.

#nomes2 = sorted(nomes)                 # O SORTED ordena e salva a lista em outro local (cria outra lista).

#nomes.insert(2, "Maurilio")            # O INSERT insere, na posição que você quer, o que você quer.



#EXERCÍCIO 4

#maiores_que_10 = (                  
#    [numero for numero in lista if numero > 10])   #Aqui vai apresentar os numeros > 10 dentro da lista na variável maiores_que_10.



#EXERCÍCIO 5

#cont1 = 0
#cont2 = 0

# for i in range(0,7):                                
#     numero = int(input("Digite um número: "))                                  
    #if numero % 2 == 0:
        #cont1 += 1    
    #elif numero % 2 != 0:
        #cont2 += 1

#print(f" Você digitou {cont1} números pares e {cont2} números impares." )
             
        
             
#EXERCÍCIO 6

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



#EXECÍCIOS DE IDENTIFICAÇÃO DE NÚMEROS IGUAIS

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

lista = []
for i in range (0,3):
    nota = int(input("Digite a nota: "))
    lista.append(nota)

media = sum(lista)/len(lista)

acima_media = []
for nota in lista:
    if nota > media:
        acima_media.append(nota)

if len(acima_media) > 0:
    print(f"{len(acima_media)} notas ficaram acima da média e foram as notas {acima_media}")

else:
    print("Nenhuma nota ficou acima da média")
    




        
        
