num1=0
num2=0
action=1
x=0


while action != 0:
    print('Escolha uma operação:')
    print('1-Adição')
    print('2-Subtração')
    print('3-Multiplicação')
    print('4-Divisão')
    print('5-Potênciação')
    action = int(input(''))

    num1 = int(input("Digite o primeiro valor "))
    num2 = int(input("Digite o segundo valor "))

    if action == 1:
        x = num1 + num2
        print(x)
    elif action == 2:
        x = num1 - num2
        print(x)
    elif action == 3:
        x = num1 * num2
        print(x)
    elif action == 4:
        x = num1 / num2
        print(x)
    elif action == 5:
        pot = 0
        x = 1
        while pot < num2:
            pot += 1
            x *= num1
        print(x)

    action = int(input("Deseja repetir?\n1-Sim\n0-Não\n"))
