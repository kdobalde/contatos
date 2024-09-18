def adicionar_contato(contatos, nome_contato, email_contato, telefone_contato):
    contato = {"Nome": nome_contato, "email": email_contato, "telefone": telefone_contato, "favorito": False}
    contatos.append(contato)
    print(f"O contato foi adicionado com sucesso.")

def ver_contatos(contatos):
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        status = "★" if contato["favorito"] else ""
        nome_contato = contato["Nome"]
        print(f"{indice}. {nome_contato} {status}")
    
def ver_info(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        print(f"\nInformações de {contatos[indice_contato_ajustado]['Nome']}:")
        print(f"Telefone: {contatos[indice_contato_ajustado]['telefone']}")
        print(f"E-mail: {contatos[indice_contato_ajustado]['email']}")
        if contatos[indice_contato_ajustado]["favorito"] == False:
            print("Contado não marcado como favorito.")
        elif contatos[indice_contato_ajustado]["favorito"] == True:
            print("★ Contato marcado como favorito.")
        else:
            print("Índice inválido.")


def editar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        print("1. Nome")
        print("2. E-mail")
        print("3. Telefone")
        if contatos[indice_contato_ajustado]["favorito"] == False:
            print("4. Marcar como favorito")
        else:
            print("4. Desmarcar como favorito")
        escolha_editar = input("Insira o número do item que deseja editar: ")
        if escolha_editar == "1":
            contatos[indice_contato_ajustado]["Nome"] = input("Insira um novo nome: ")
            print("O nome do contato foi editado.")
        elif escolha_editar == "2":
            contatos[indice_contato_ajustado]["email"] = input("Insira o novo e-mail: ")
            print("O e-mail do contato foi alterado.")
        elif escolha_editar == "3":
            contatos[indice_contato_ajustado]["telefone"] = input("Insira o novo telefone: ")
            print("O telefone do contato foi alterado.")
        elif escolha_editar == "4":
            if contatos[indice_contato_ajustado]["favorito"] == False:
                contatos[indice_contato_ajustado]["favorito"] = True
                print("Contato marcado como favorito.")
            elif contatos[indice_contato_ajustado]["favorito"] == True:
                contatos[indice_contato_ajustado]["favorito"] = False
                print("Contato desmarcado como favorito.")
        else:
            print("índice inválido.")

def marcar_favorito(contatos):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
         contatos[indice_contato_ajustado]["favorito"] = not contatos[indice_contato_ajustado]["favorito"]
         if contatos[indice_contato_ajustado]["favorito"]:
            print("Contato marcado como favorito.")
         else:
            print("Contato desmarcado como favorito.")
    else:
        print("índice inválido.")

def ver_favoritos(contatos):
    print("\nContatos marcados como favorito:")
    indice_favorito = 1  
    for contato in contatos:
        if contato.get("favorito", False):
            print(f"{indice_favorito}. {contato['Nome']} ★")
            indice_favorito += 1  

def excluir_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contato_removido = contatos[indice_contato_ajustado] 
        del contatos[indice_contato_ajustado]  # Remove o contato pelo índice
        print(f"O contato de {contato_removido['Nome']} foi removido.")
    else:
        print("Índice inválido.")

contatos = []

while True:
    print("\nGerenciador de contatos")
    print("1. Ver contatos")
    print("2. Adicionar contato")
    print("3. Editar contato")
    print("4. Marcar/Desmarcar contato como favorito")
    print("5. Ver apenas contatos favoritos")
    print("6. Apagar contato")
    print("7. Sair")

    escolha = input("Digite o número desejado: ")

    if escolha == "1":
        ver_contatos(contatos)
        indice_contato = input("Insira o número do contato que deseja ver informações: ")
        ver_info(contatos, indice_contato)

    elif escolha == "2":
        nome_contato = input("Nome do contato: ")
        email_contato = input("E-mail do contato: ")
        telefone_contato = input("Número do contato: ")
        adicionar_contato(contatos, nome_contato, email_contato, telefone_contato)
    elif escolha == "3":
        ver_contatos(contatos)
        indice_contato = input("Insira o número do contato que você deseja editar: ")
        editar_contato(contatos, indice_contato)
    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("Insira o número do contato que você deseja marcar/desmarcar como favorito: ")
        marcar_favorito(contatos)
    elif escolha == "5":
        ver_favoritos(contatos)
    elif escolha == "6":
        ver_contatos(contatos)
        indice_contato = input("Insira o contato que deseja excluir: ")
        excluir_contato(contatos, indice_contato)
    elif escolha == "7":
        break
    else:
        print("Índice inválido.")

print("Programa Encerrado.")
