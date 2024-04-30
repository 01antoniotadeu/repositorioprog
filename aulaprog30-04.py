#print("Olá", "mundo", sep="-") # Saída: Olá-mundo
#print("Olá", "Python", end="!\n") # Saída: Olá Python

#print("18", "04", "2023", sep="/") 

#print("Antonio", "Tadeu", "tadeuantoniosa@gmail.com", sep="; ")

#print("Loading", end=" ")

#print("[OK]") # Saída: Loading [OK]

#input("Digite seu nome: ")
#print("Olá", nome)

#input("Digite itens separados por vírgula: ").split(',')
#print("Itens:", itens)

#int(input("Digite sua idade: "))
#print("Daqui a cinco anos, você terá", idade + 5, "anos.")

#float(input("Digite sua altura em metros: "))
#print("Sua altura é", altura, "metros."

print("Digite números para adicionar à lista (digite 'done' para terminar):")
   numeros = []
    while True:
        entrada = input()
    if entrada.lower() == 'done':
        break
 else:
         numeros.append(int(entrada))
 print("Números coletados:", numeros