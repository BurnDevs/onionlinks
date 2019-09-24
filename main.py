####################################
#      Criado por Ryan Aragão      #
#          18/02/2019              #
# Para mais scripts siga no github #
#   https://github.com/BurnDevs/   #
####################################
from googlesearch import search
from clint.textui import colored
import platform
import os

# Apresentação
print("""
             _             _ _       _        
  ___  _ __ (_) ___  _ __ | (_)_ __ | | _____ 
 / _ \| '_ \| |/ _ \| '_ \| | | '_ \| |/ / __|
| (_) | | | | | (_) | | | | | | | | |   <\__ 
 \___/|_| |_|_|\___/|_| |_|_|_|_| |_|_|\_\___/
                                              
      Criado por Ryan Aragão (BurnDev's)
""")

# Pegar tipo de conteúdo
print("Exemplos de conteúdo: Hacking, Forum, eBooks.")
conteudo = str(input("coloque o conteúdo: "))

# Dork para encontrar os URLS/LINKS/SITES
dork = f'{conteudo} site:onion.link | site:onion.cab | site:onion.sh | site:tor2web.fi | site:onion.direct'


# definindo funçoes


def menu():
    print('''
    1. Será criado um TXT com os URLS, caso esteja em branco, aguarde o programa finalizar.
    2. Antes de utilizar os links, retire HTTP:// HTTPS://
    3. Retire tudo que tiver após o .onion do link.
    ''')

def opcoes():
    print("0 - Sair")
    print("1 - Procurar sites onion")
    print("2 - Ver Instruções")


def limpar():
    sistema = platform.platform()
    if "win" in sistema.lower():
        cmd_limpar = "cls"
    else:
        cmd_limpar = "clear"

    os.system(cmd_limpar)


while True:
    opcoes()
    menuzinho = int(input("Selecione uma opção: "))
    if menuzinho == 0:
        limpar()
        break
    elif menuzinho == 1:
        limpar()
        with open("sitesonion.txt", "w") as stream:
            for url in search(dork, stop=50 or 1):
                print(url, file=stream)
    elif menuzinho == 2:
        limpar()
        menu()
        input("Pressione ENTER para continuar")
        limpar()
    else:
        print("Essa opção não existe, tente novamente!")
