objeto1 = (input("Escolha um e digite pedra, papel ou tesoura: "))
objeto2 = (input("Escolha um e digite pedra, papel ou tesoura: "))

if objeto1 == "pedra" and objeto2 == "tesoura":
    print = (input(f"Pedra ganhou!"))

elif  objeto1 == "pedra" and objeto2 == "papel":
    print = (input(f"Papel abraçou a pedra e ganhou!"))

elif  objeto1 == "pedra" and objeto2 == "pedra":
    print = (input(f"Empate!"))

elif objeto1 == "papel" and objeto2 == "tesoura":
    print = (input(f"Tesoura rasgou o papel!"))

elif  objeto1 == "papel" and objeto2 == "papel":
    print = (input(f"Empate!"))

elif  objeto1 == "papel" and objeto2 == "pedra":
    print = (input(f"Papel abraçou a pedra e ganhou"))

elif objeto1 == "tesoura" and objeto2 == "tesoura":
    print = (input(f"Empate!"))

elif  objeto1 == "tesoura" and objeto2 == "papel":
    print = (input(f"Tesoura rasgou o papel!"))

elif  objeto1 == "tesoura" and objeto2 == "pedra":
    print = (input(f"Pedra quebrou a tesoura!"))

else: 
    print = (input(f"Você digitou algo errado, volte e escolha entre pedra, papel ou tesoura!"))