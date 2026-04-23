chamados = []

while True:
    print("\n=== SISTEMA DE CHAMADOS ===")
    print("1 - Abrir chamado")
    print("2 - Listar chamados")
    print("3 - Resolver chamado")
    print("4 - Excluir chamado")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Título do problema: ")
        chamados.append({"titulo": titulo, "status": "Aberto"})
        print("Chamado aberto com sucesso!")

    elif opcao == "2":
        if not chamados:
            print("Nenhum chamado registrado.")
        else:
            for i, c in enumerate(chamados):
                print(f"{i} - {c['titulo']} [{c['status']}]")

    elif opcao == "3":
        indice = int(input("Número do chamado: "))
        if 0 <= indice < len(chamados):
            chamados[indice]["status"] = "Resolvido"
            print("Chamado resolvido!")
        else:
            print("Chamado inválido.")

    elif opcao == "4":
        indice = int(input("Número do chamado: "))
        if 0 <= indice < len(chamados):
            chamados.pop(indice)
            print("Chamado removido.")
        else:
            print("Chamado inválido.")

    elif opcao == "5":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")