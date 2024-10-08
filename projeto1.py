def adicionarTarefa(tarefas, nome_tarefa):
    #Dicionário e os status da tarefa
    tarefa = {"nome": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")

def verTarefa(tarefas):
    print("\n lista de tarefas")
    print(tarefas)



tarefas = []
while True:
    print("\n Lista de tarefas automatizada")
    print("1. Adicionar Tarefas")
    print("2. Ver Tarefas")
    print("3. Atualizar Tarefas")
    print("4. Completar Tarefa")
    print("5. Remover Tarefa completada")    
    print("6. Sair")

    escolha = input("Escolha um número: ")

    #Menu 
    if escolha == "1":
        nome_tarefa = input("Qual o nome da tarefa?: ")
        adicionarTarefa(tarefas, nome_tarefa)

    elif escolha == "2":
        verTarefa(tarefas)

    elif escolha == "6": 
        break
    





    