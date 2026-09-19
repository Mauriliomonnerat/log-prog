def verificacao_local (cidade,nome):
    if cidade == "Rio de Janeiro":
        return f"Seja Bem-vindo à Cidade Maravilhosa, {nome}!"
    return cidade

nome1 = input("Digite o seu nome: ")
cidade1 = input("Digite a sua cidade: ")

c = verificacao_local (cidade1,nome1)
print (c)


