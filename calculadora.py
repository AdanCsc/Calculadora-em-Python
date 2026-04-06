def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b


def obter_numeros():
    try:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        return a, b
    except ValueError:
        print("Erro: digite apenas números válidos.\n")
        return None, None


def menu():
    while True:
        print("\n===== CALCULADORA =====")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("Encerrando calculadora...")
            break

        a, b = obter_numeros()
        if a is None:
            continue

        try:
            if opcao == "1":
                print(f"Resultado: {soma(a, b)}")
            elif opcao == "2":
                print(f"Resultado: {subtracao(a, b)}")
            elif opcao == "3":
                print(f"Resultado: {multiplicacao(a, b)}")
            elif opcao == "4":
                print(f"Resultado: {divisao(a, b)}")
            else:
                print("Opção inválida!")

        except ValueError as e:
            print(f"Erro: {e}")


if __name__ == "__main__":
    menu()