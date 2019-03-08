###################################
#     Criado por Ryan Aragão      #
#          18/02/2019             #
# Para mais scripts siga no github#
# https://github.com/RyanAragao2  #
###################################
from googlesearch import search

# Apresentação
print("Para entender melhor sobre a ferramenta")
print("Ou para mais scripts, siga no github:")
print("https://github.com/RyanAragao2")
print("")
input('Aperte ENTER para continuar')

# Pegar tipo de conteúdo
print("Exemplos de conteúdo: Hacking, Forum, eBooks")
conteudo = str(input("coloque o conteúdo:"))

# Dork para encontrar os URLS/LINKS/SITES
dork = f'{conteudo} site:onion.link | site:onion.cab | site:onion.sh | site:tor2web.fi | site:onion.direct'

# Menu de escolhas/seleção


def menu():
    banner = '''
    +-------------------------------------------------------+
    |          Script para buscar sites da Onion            |
    | 1. Enquanto não estiver pronto o txt ficara em branco |
    | 2. Tire o HTTP/HTTPS do URL para usa-lo no TOR.       |
    | 3. Tire tudo que tiver depois do .onion               |
    |     Exemplo Certo: exemplo293884.onion                |
    |     Exemplo Errado: https://exemplo283874.onion.sh/   |
    +-------------------------------------------------------+
    '''

    print(banner)
    print("0 - Sair")
    print("1 - Procurar sites onion")


while True:
    menu()
    menuzinho = int(input("Selecione uma opção: "))
    if menuzinho == 0:
        print("Até a proxima")
        break
    elif menuzinho == 1:
        with open("sitesonion.txt", "w") as stream:
            for url in search(dork, stop=50 or 1):
                print(url, file=stream)
                print("Os URLS estão sendo salvos em um arquivo chamado: sitesonion.txt")
                print("Aguarde o script encerrar")
    else:
        print("Essa opção não existe, tente novamente!")
