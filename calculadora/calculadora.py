import os

operadores = ["+", "-", "*", "/", "**"]

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu():
    print("Calculadora Simples\n")
    print("0. Adição")
    print("1. Subtração")
    print("2. Multiplicação")
    print("3. Divisão")
    print("4. Exponenciação")
    print("\n======================")

    while True:
        try:
            opcao = int(input("Escolha uma operação (0-4): "))
            if opcao in range(5):
                return opcao
            else:
                print("Opção inválida. Por favor, escolha um número entre 0 e 4.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

def calcular(opcao, num1, num2):
    if opcao == 0:
        return num1 + num2
    elif opcao == 1:
        return num1 - num2
    elif opcao == 2:
        return num1 * num2
    elif opcao == 3:
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero."
    elif opcao == 4:
        return num1 ** num2

while True:
    opcao_escolhida = exibir_menu()
    operacao_escolhida = operadores[opcao_escolhida]

    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira números válidos.")

    resultado = calcular(opcao_escolhida, num1, num2)
    print(f"Resultado: {num1} {operacao_escolhida} {num2} = {resultado}")

    print("=======================")
    while True:
        continuar = input("\nDeseja realizar outra operação? (s/n): ").strip().lower()
        if continuar in ['s', 'n']:
            break
        else:
            print("Entrada inválida. Por favor, digite 's' para sim ou 'n' para não.")

    if continuar == 'n':
        print("Encerrando a calculadora. Até logo!")
        break

    limpar_tela()
