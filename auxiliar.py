import os
from sys import argv
from colorama import init, Fore

init()

def adicionar():
    n_labs = int(input("Número do maior lab: "))
    nome = input("Digite seu nome: ")
    ano = input("Digite o ano (ex. 023): ")
    source = input("Digite o caminho para o diretório fonte: ")

    if not os.path.isdir(ano):
        os.mkdir(ano)

    for n in range(1, n_labs+1):
        if not os.path.exists(os.path.join(ano, f"lab{n:02}")):
            os.mkdir(os.path.join(ano, f"lab{n:02}"))
        
        if os.path.exists(os.path.join(ano, f"lab{n:02}",f"{nome}.py")):
            print(Fore.BLUE, f"Solução para Lab {n:02} já existe")
        elif os.path.exists(os.path.join(source, f"lab{n:02}.py")):
            os.rename(os.path.join(source, f"lab{n:02}.py"), os.path.join(ano, f"lab{n:02}",f"{nome}.py"))
            print(Fore.GREEN, f"Solução para Lab{n:02} adicionada")
        else:
            print(Fore.RED, f"Arquivo {os.path.join(source, f'lab{n:02}.py')} não encontrado")

def enunciados():
    n_labs = int(input("Número do maior lab: "))
    ano = input("Digite o ano (ex. 023): ")
    source = input("Digite o caminho para o diretório fonte: ")
    
    if not os.path.isdir(ano):
        os.mkdir(ano)

    for n in range(1, n_labs+1):
        if not os.path.exists(os.path.join(ano, f"lab{n:02}")):
            os.mkdir(os.path.join(ano, f"lab{n:02}"))
            
        if os.path.exists(os.path.join(ano, f"lab{n:02}",f"enunciado.pdf")):
            print(Fore.BLUE, f"Enunciado para Lab {n:02} já existe")
        elif os.path.exists(os.path.join(source, f"Lab {n:02}.pdf")):
            os.rename(os.path.join(source, f"Lab {n:02}.pdf"), os.path.join(ano, f"lab{n:02}",f"enunciado.pdf"))
            print(Fore.GREEN, f"Enunciado para Lab{n:02} adicionado")
        else:
            print(Fore.RED, f"Arquivo {os.path.join(source, f'Lab {n:02}.pdf')} não encontrado")

if __name__ == '__main__':
    if len(argv) < 2:
        print("Escolha o modo")
    else:
        exec(f"{argv[1]}()")