def adicionarTarefa(tarefas, nome_tarefa):
    # Dicionário e os status da tarefa
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa '{nome_tarefa}' foi adicionada com sucesso!")
    
def verTarefa(tarefas):
    print("\n Lista de tarefas: ")
    
    if not tarefas:  # Verifica se a lista de tarefas está vazia
        print("Nenhuma tarefa na lista.")
        return
    
    for indice, tarefa in enumerate(tarefas, start=1):
        # Verifica se a estrutura da tarefa está correta
        status = "✔" if tarefa["completada"] else " "  # Checa o status de completada
        print(f"{indice}. [{status}] {tarefa['tarefa']}")

def atualizarNome(tarefas, indice_tarefa, novo_nome):
    indice_ajustado = int(indice_tarefa) - 1
    tarefas [indice_ajustado] ["tarefa"] = novo_nome
    print(f"Tarefa {indice_tarefa} Atualizada para {novo_nome} ")
    
        
def completarTarefa(tarefas,indice_tarefa):
    indice_ajustado = int(indice_tarefa) - 1
    tarefas[indice_ajustado] ["completada"] = True
    print(f"Tarefa {indice_tarefa} marcada como completada")
    return

def deletarTarefa(tarefas):
    for tarefa in tarefas:
        if tarefa["completada"]:
            tarefas.remove(tarefa)
        print("Tarefas completadas foram deletadas")
    return
    
tarefas = []

while True:
    print("\nLista de tarefas automatizada")
    print("1. Adicionar Tarefas")
    print("2. Ver Tarefas")
    print("3. Atualizar Tarefas")
    print("4. Completar Tarefa")
    print("5. Remover Tarefa completada")    
    print("6. Sair")

    escolha = input("Escolha um número: ")

    # Menu 
    if escolha == "1":
        nome_tarefa = input("Qual o nome da tarefa?: ")
        adicionarTarefa(tarefas, nome_tarefa)

    elif escolha == "2":
        verTarefa(tarefas)
        
    
    elif escolha == "3":
       verTarefa(tarefas)
       indice_tarefa = input("Digite o número da tarefa que você deseja atualizar: ")
       novo_nome = input("Digite o novo nome da tarefa: ")
       atualizarNome(tarefas, indice_tarefa, novo_nome)
       
    elif escolha == "4":
         verTarefa(tarefas)  # Passa a lista de tarefas para verTarefa()
         indice_tarefa = input("Escolha o número da tarefa que você quer completar: ")
         completarTarefa(tarefas, indice_tarefa)

    elif escolha == "5":
        deletarTarefa(tarefas)
        verTarefa(tarefas)

    elif escolha == "6":
        print("Saindo do programa...")
        break




    