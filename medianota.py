# Pegue as notas 
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

# Faça a média
media = (nota1 + nota2)/2

if media < 6:
    print(" Aluno Reprovado ")
else:
    print(" Aluno Aprovado ")
