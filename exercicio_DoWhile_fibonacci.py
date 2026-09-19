anterior = 0
atual = 1
proximo = anterior + atual
print (anterior)
print (atual)
print (proximo)
while (atual <= 2000):
    anterior = atual
    atual = proximo
    proximo = anterior + atual
    print(proximo)

# Isso seria um Do While
# Ele faz primeiro e depois faz o laço