import os
import sys
import json
from datetime import datetime

def menu():
    carregar_tarefas()
    while True:
        print("1 = Adicionar Tarefa")
        print("2 = Visualizar Tarefas")
        print("3 = Sair")
        print("4 = Remover Tarefa")
        print("5 = Editar Tarefa")
        print("6 = Marcar Tarefa como Concluída")
        print("7 = Marcar Tarefa como Pendente")
        print("8 = Buscar Tarefas")
        print("9 = Definir Prioridade")
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            adicionar_tarefa()
        elif escolha == "2":
            visualizar_tarefas()
        elif escolha == "3":
            salvar_tarefas()
            print("Saindo...")
            break
        elif escolha == "4":
            remover_tarefa()
        elif escolha == "5":
            editar_tarefa()
        elif escolha == "6":
            marcar_como_concluida()
        elif escolha == "7":
            marcar_como_pendente()
        elif escolha == "8":
            buscar_tarefa()
        elif escolha == "9":
            definir_prioridade()
        else:
            print("Opção inválida, tente novamente.")

tarefas = []

def adicionar_tarefa():
    descricao = input("Digite a tarefa: ")
    prioridade = input("Defina a prioridade da tarefa (Alta, Média, Baixa): ").capitalize()
    prazo = input("Digite o prazo (DD/MM/AAAA): ")
    data_criacao = datetime.now().strftime("%d/%m/%Y")
    try:
        data_prazo = datetime.strptime(prazo, "%d/%m/%Y").strftime("%d/%m/%Y")
    except ValueError:
        print("Formato de data inválido. Use DD/MM/AAAA.")
        return
    tarefas.append({"descricao": descricao, "concluida": False, "prioridade": prioridade, "data_criacao": data_criacao, "prazo": data_prazo})
    print("Tarefa adicionada!")

def visualizar_tarefas():
    ordenar_tarefas_por_prioridade()
    print("Tarefas:")
    for i, tarefa in enumerate(tarefas):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{i + 1}. {tarefa['descricao']} [{status}] - Prioridade: {tarefa['prioridade']} - Data de Criação: {tarefa['data_criacao']} - Prazo: {tarefa['prazo']}")


def remover_tarefa():
    visualizar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa que deseja remover: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefa_removida = tarefas.pop(indice)
            print(f"Tarefa '{tarefa_removida['descricao']}' removida com sucesso!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida. Insira um número válido.")

def editar_tarefa():
    visualizar_tarefas()
    try:
        indice = int(input("Insira o número da tarefa que deseja editar: ")) - 1
        if 0 <= indice < len(tarefas):
            nova_descricao = input("Digite a nova descrição: ")
            tarefas[indice]["descricao"] = nova_descricao
            print("Tarefa atualizada com sucesso!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")

def salvar_tarefas():
    with open('tarefas.json', 'w') as arquivo: 
        json.dump(tarefas, arquivo)
    print("Tarefas salvas com sucesso!")

def carregar_tarefas():
    global tarefas
    if os.path.exists('tarefas.json'): 
        with open('tarefas.json', 'r') as arquivo:
            tarefas = json.load(arquivo)
        print("Tarefas carregadas com sucesso!")
    else:
        tarefas = []

def marcar_como_concluida():
    visualizar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa que deseja marcar como concluída: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluida"] = True
            print("Tarefa marcada como concluída!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida. Insira um número válido.")

def marcar_como_pendente():
    visualizar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa que deseja marcar como pendente: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluida"] = False
            print("Tarefa marcada como pendente!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida. Insira um número válido.")

def buscar_tarefa():
    try:
        palavra_chave = input("Digite a palavra-chave para buscar: ")
        print("Tarefas encontradas:")
        encontrou_tarefa = False
        for i, tarefa in enumerate(tarefas):
            if palavra_chave.lower() in tarefa["descricao"].lower():
                status = "Concluída" if tarefa["concluida"] else "Pendente"
                print(f"{i + 1}. {tarefa['descricao']} [{status}]")
                encontrou_tarefa = True
        if not encontrou_tarefa:
            print("Nenhuma tarefa encontrada com a palavra-chave fornecida.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def definir_prioridade():
    visualizar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa para definir a prioridade: ")) - 1
        if 0 <= indice < len(tarefas):
            nova_prioridade = input("Defina a nova prioridade da tarefa (Alta, Média, Baixa): ").capitalize()
            tarefas[indice]["prioridade"] = nova_prioridade
            print("Prioridade atualizada!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida. Insira um número válido.")

def ordenar_tarefas_por_prioridade():
    prioridades = {"Alta": 1, "Media":2, "Baixa": 3}
    tarefas.sort(key=lambda x : prioridades.get(x.get ("prioridade", "Baixar"),3))
    print ("Tarefas Ordenadas por prioridade !")

menu()
