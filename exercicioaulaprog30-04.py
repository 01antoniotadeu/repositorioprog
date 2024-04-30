def imprimir_informacoes(nome, idade, cidade):
    print("Nome:", nome, "-", "Idade:", idade, "-", "Cidade:", cidade, end="!\n")

# Exemplo de uso:
imprimir_informacoes("Alice", 25, "São Paulo")

def calcular_operacao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação desejada (+, -, *, /): ")

    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Não é possível dividir por zero!")
            return

    print("O resultado de", num1, operacao, num2, "é:", resultado)

calcular_operacao()

def lista_de_compras():
    itens = input("Digite os itens da lista de compras, separados por vírgula: ")
    lista = itens.split(",")  # Separa os itens pela vírgula e cria uma lista

    print("Itens da lista de compras:")
    for i, item in enumerate(lista, 1):  # Itera sobre a lista de itens
        print("Item {}: {}".format(i, item.strip()))  # Imprime cada item

lista_de_compras()

def celsius_para_fahrenheit():
    celsius = float(input("Digite a temperatura em graus Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("A temperatura em Fahrenheit é:", fahrenheit)

# Exemplo de uso:
celsius_para_fahrenheit()

def pedir_nomes():
    nomes = []
    while True:
        nome = input("Digite um nome (ou 'sair' para sair): ")
        if nome.lower() == 'sair':
            break
        nomes.append(nome)
    for nome in nomes:
        print(nome)

# Para testar a função
pedir_nomes()