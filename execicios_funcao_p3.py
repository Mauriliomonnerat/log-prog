list = []

carros = ['Ferrari', 'Monza', 'Palio']

for i in range (len(carros)):     # Para cada posição(número) gerada pelo range, o for atribui essa posição como número ao i.
    print(f'{i+1} - {carros[i]}') # O range não gera exatamente uma "posição"; ele gera números. Nesse caso, esses números representam as posições da lista.