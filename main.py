reclamacoes = []
elogios = []
sugestoes = []

opcao = 0
def mostrarMenu():
    print("Menu de Opções \n1. Listar Manifestações \n2. Listar Manifestação por Tipo \n3. Crie uma Manifestação"
          "\n4. Quantidade de Manifestações \n5. Pesquisar Manifestação por Código  \n6. Excluir Manifestação \n7. Sair")
def listarManifestaoces():
    if reclamacoes or elogios or sugestoes:
        print("Todas as Manifestações")
        if reclamacoes:
            print("Reclamações: ")
            for indice, reclamacao in enumerate(reclamacoes):
                print("Código: ",f"{indice+1}\nManifestação: {reclamacao}")
        if elogios:
            print("Elogios: ")
            for indice, elogio in enumerate(elogios):
                print("Código: ", f"{indice + 1}\nManifestação: {elogio}")
        if sugestoes:
            print("Sugestões: ")
            for indice, sugestao in enumerate(sugestoes):
                print("Código: ", f"{indice + 1}\nManifestação: {sugestao}")
    else:
        print("Não existe Manifestações")



def listarManPorTipo():
    print("Escolha a Manifestação \n1. Reclamação \n2. Elogio \n3. Sugestão")
    opcao = int(input("Digite uma opcao: "))
    if opcao == 1:
        if len(reclamacoes) > 0:
            print("Reclamações: ")
            for indice, reclamacao in enumerate(reclamacoes):
                print("Código: ", f"{indice + 1}\nManifestação: {reclamacao}")
        else:
            print("Não exite Reclamações")
    elif opcao == 2:
        if len(elogios) > 0:
            print("Elogios: ")
            for indice, elogio in enumerate(elogios):
                print("Código: ", f"{indice + 1}\nManifestação: {elogio}")
        else:
            print("Não existe Elogios")
    elif opcao == 3:
        if len(sugestoes) > 0:
            print("Sugestões: ")
            for indice, sugestao in enumerate(sugestoes):
                print("Código: ", f"{indice + 1}\nManifestação: {sugestao}")
        else:
            print("Não existe Sugestões")
    else:
        print("Opção inválida!")

def criarManifestacoes():
    print("Crie uma Manifestação \n1. Reclamação \n2. Elogio \n3. Sugestão")
    opcao = int(input("Digite uma opcao: "))
    if opcao == 1:
        reclamacao = input("Digite sua Reclamação: ")
        reclamacoes.append(reclamacao)
        print("Sua reclamação foi adicionada com sucesso!")
    elif opcao == 2:
        elogio = input("Digite seu Elogio: ")
        elogios.append(elogio)
        print("Seu elogio foi adicionado com sucesso!")
    elif opcao == 3:
        sugestao = input("Digite sua Sugestão: ")
        sugestoes.append(sugestao)
        print("Sua sugestão foi adicionada com sucesso!")
    else:
        print("Opção Inválida!")
def quantidadeDeManifestações():
    print("Quantidade de Manisfetações: ",soma(), "\nReclamações: ",len(reclamacoes),"\nElogios: ",len(elogios),"\nSugestões: ",len(sugestoes))
def pesquisarManisfestacoes():
    print("Pesquisar Manifestação \n1. Reclamação \n2. Elogio \n3. Sugestão")
    opcao = int(input("Digite uma opcao: "))
    if opcao == 1:
        reclamacao = int(input("Digite o Código da Reclamação que você deseja: "))
        if reclamacao > 0 and reclamacao <= len(reclamacoes):
            print("A Reclamação pesquisada foi: ",reclamacoes[reclamacao -1])

    elif opcao == 2:
        elogio = int(input("Digite o Código do Elogio que você deseja: "))
        if elogio > 0 and elogio <= len(elogios):
            print("O Elogio pesquisado foi: ",elogios[elogio -1])

    elif opcao == 3:
        sugestao = int(input("Digite o Código da Sugestão que você deseja: "))
        if sugestao > 0 and sugestao <= len(sugestoes):
            print("A Sugestão pesquisada foi: ",sugestoes[sugestao -1])
    else:
        print("Opção Inválida!")

def excluirManifestacoes():
    print("Excluir Manifestações \n1. Reclamação \n2. Elogio \n3. Sugestão")
    opcao = int(input("Digite uma opcao: "))
    if opcao == 1:
        removerReclamacao = int(input("Digite o Código da reclamação que você deseja remover: "))
        reclamacoes.pop(removerReclamacao -1)
        print("Reclamação removida com sucesso")
    elif opcao == 2:
        removerElogio = int(input("Digite o Código do elogio que você deseja remover: "))
        elogios.pop(removerElogio -1)
        print("Elogio removido com sucesso")
    elif opcao == 3:
        removerSugestão = int(input("Digite o Código da sugestão que você deseja remover: "))
        sugestoes.pop(removerSugestão -1)
        print("Sugestão removida com sucesso")
    else:
        print("Opção Inválida!")
def soma():
    return len(reclamacoes) + len(elogios) + len(sugestoes)



while opcao != 7:
    mostrarMenu()
    opcao = int(input("Insira uma Opção: "))

    if opcao == 1:
        listarManifestaoces()
    elif opcao == 2:
        listarManPorTipo()
    elif opcao == 3:
        criarManifestacoes()
    elif opcao == 4:
        quantidadeDeManifestações()
    elif opcao == 5:
        pesquisarManisfestacoes()
    elif opcao == 6:
        excluirManifestacoes()
    elif opcao != 7:
        pass
print("Obrigado por usar a Locadora!")
