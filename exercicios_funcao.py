# Somar 2 numeros
def somar (a,b):  #a e b são parâmetros
    a = a + b # esse "a" só existe dentro do escopo da função
    return a #isso faz ser uma função

a = 5 # esse "a" aqui não é o mesmo da função
b = 4

c = somar (b,a) # 4,5
#parametros são posicionais, eles não olham os nomes
print (c)
print (a)

#Substrair
def subtrair (a,b):
    """
    Essa função subtrai o "a" de "b" e retorna o valor
    """
    #Isso faz com o que essa mensagem apareça no subtrair

    return a - b

subtrair()

#Saber se é impar
def impar (numero):
    return not numero % 2 == 0  #retorne verdadeiro se o resto da divisão por 2 não for 0

numero_1 = impar (1)

#verificar  se na senha tem 8 caracteres
def verificar_senha (senha):
    #len() ->
    return len (senha) >= 8
