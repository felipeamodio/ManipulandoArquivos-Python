#manipulando os arquivos
arquivo = open("primeiro_arquivo.txt", "w")

arquivo.write("Meu primeiro arquivo!!!")

arquivo.close()


#modo melhorado de fazer || o as é passando um apelido

with open("segunto_arquivo.txt", "a") as arquivo:
    arquivo.write("\nHakuna Matata!!")

#manipulando arquivos em pastas do finder

arquivo2 = open("/Users/felipeamodio/PycharmProjects/Cap9/Manipulacao_Arquivos/print2.txt")

#vai ler o conteúdo do arquivo
print(arquivo2.read())

#ler uma linha de cada vez
print(arquivo2.readline())
print(arquivo2.readline())

#fazer um loop pra printar todas as linhas

for linha in arquivo2.readlines():
    print(linha)

#colocar cada linha do arquivo como um intem em uma lista e depois manipular como quisermos

linhasDoArquivo = arquivo2.readlines()

print("Consegui transformar meu arquivo em uma {}".format(linhasDoArquivo))

#colocando lista em ordem alfabética
linhasDoArquivo.sort()

#exibir a lista agora em ordem alfabética
print(linhasDoArquivo)

arquivo2.close()