# escrita
file = open("arquivo.txt", mode="w")
LINES = ["Olá\n", "mundo\n", "belo\n", "do\n", "Python\n"]
file.writelines(LINES)
file.close()

# leitura
file = open("arquivo.txt", mode="r")
for line in file:
    # não esqueça que a quebra de linha também é um caractere da linha
    print(line)
file.close()  # não podemos esquecer de fechar o arquivo
