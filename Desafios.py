# contador = 0
# valor_total = 0
# valor_desconto = 0.0

# while True:
#     valor_produto = float(input ("Digite o valor do produto: "))

#     if valor_produto == 0:
#         print (f"O total de clientes foi de {contador} e o valor total de compras foi {valor_total}")
#         break
    
#     contador += 1

#     while valor_produto != -1:
#         valor_total += valor_produto
#         valor_produto = float(input ("Digite o valor do produto: "))
#     print (valor_total)
        
#     if valor_total > 200:
#         valor_desconto = valor_total * 0.10
#         print (f"Seu desconto foi de {valor_desconto} Reais")

#     elif valor_total > 100:
#         valor_desconto = valor_total * 0.05
#         print (f"Seu desconto foi de {valor_desconto} Reais")

#     else:
#         print (f"Você não teve desconto")

#     parcelas = int(input ("De 1 a 6, digite o número de parcelas desejadas: "))

#     while parcelas < 0 or parcelas > 6:
#             parcelas = int(input ("Essa quantidade não é possível, escolha de 0 a 6 parcelas: "))

#     if parcelas == 0 or parcelas <= 6:
#         valor_parcela = valor_total/parcelas
#         for i in range(parcelas):
#             i += 1
#             print (f'No mês {i} o valor da parcela será {valor_parcela}')
#     break
    


# pc sorteia numero entre 1 e 50
# tu tem 5 chances de acertar
# import random

# print('Bem vindo(a) ao jogo de adivinhação')
# pontos = 0
# for i in range(3):
#     print(f'Essa é sua {i+1}ª rodada')
#     numero_aleatorio = random.randint(1, 10)
#     tentativas = 0 # numero de chances
#     acertou = False # variavel de controle
#     # enquanto tiver chances
#     while tentativas < 5:
#         palpite = int(input('Dê seu chute (1 à 10): '))

#         # se acertou
#         if palpite == numero_aleatorio:
#             print('Você acertou Miseraví!')
#             acertou = True
#             if tentativas == 4:
#                 pontos += 10
#             else:
#                 pontos += (100 - tentativas*25)

#             break # para a execução do laço While

#         # ajudas
#         elif palpite < numero_aleatorio:
#             print('Tente um número maior')5

#         elif palpite > numero_aleatorio:
#             print('Tente um número menor')

#         tentativas += 1 # usou uma tentativa

#     if not acertou:
#         print(f'Nessa rodada ({i+1}), você errou muito, gastou tudo')
#         print(f'O número aleatório era: {numero_aleatorio}\n\n')

# if pontos >= 200:
#     print(f'Sabe muito, faturou {pontos} pontos')
# elif 100 < pontos < 200:
#     print(f'Até que tu sabe algo, {pontos} pontos para tu')
# else:
#     print(f'Tente de novo, ou não, só {pontos} pontos')


# Crie um sistema de autenticação de terminal que 
# valida a segurança da senha cadastrada e gerencia o acesso do usuário.
# Primeiro, o usuário define uma senha numérica de 4 dígitos. 
# Use um loop while que continue solicitando até que o valor 
# digitado esteja rigorosamente entre 1000 e 9999.

# senha = int(input('Informe sua senha: '))
# while senha < 1000 or senha > 9999:
#     senha = int(input('Informe sua senha: '))

# fica ai em cima até digitar uma senha (PIN) válida
# -------------------------------------------------

# Em seguida, o sistema entra em modo de bloqueio e 
# pede a confirmação da senha para liberar o sistema, 
# permitindo até 3 tentativas via loop while.
# print('\n\n\n\n')

# acesso_liberado = False # variavel de controle
# tentativa = 3
# while tentativa > 0:
#     confirmacao_senha = int(
#     input('Para entrar no sistema, digite o PIN: '))

#     if senha == confirmacao_senha:
#         acesso_liberado = True
#         break

#     else:
#         tentativa = tentativa - 1

#     print(f'Você ainda tem {tentativa} tentativas')

# # Se o acesso for liberado com sucesso, use um loop 
# # for para simular uma contagem regressiva de 
# # inicialização do sistema (de 5 até 1).

# if acesso_liberado:
#     for i in range(5, 0, -1):
#         print(f'{i}...')
#     print('Sistema Inicializado com Sucesso')
# else:
#     print('Acesso Negado. \nSua conta foi bloqueada')