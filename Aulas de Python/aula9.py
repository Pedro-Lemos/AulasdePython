def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('teste.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def copia_arquivo(nome_arquivo):
    import shutil
    shutil.copy(nome_arquivo, 'C:/Users/User/Desktop/Python/')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Users/User/Desktop/Python/')


if __name__ == '__main__':
    #escrever_arquivo('Primeira linha.\n')
    atualizar_arquivo('Segunda linha.\n')