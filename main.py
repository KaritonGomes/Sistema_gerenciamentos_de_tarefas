from datetime import datetime
import json
import os
class Tarefa:
    def __init__(self, descricao, prioridade, prazo):
        self.descricao = descricao
        self.concluida = False
        self.prioridade = prioridade
        self.data_criacao = datetime.now().strftime("%d/%m/%Y")
        try:
            self.prazo = datetime.strptime(prazo, "%d/%m/%Y").strftime("%d/%m/%Y")
        except ValueError:
            self.prazo = None

    def __str__(self):
        status = "Concluída" if self.concluida else "Pendente"
        prazo = self.prazo if self.prazo else "Sem prazo"
        return f"{self.descricao} [{status}] - Prioridade: {self.prioridade} - Data de Criação: {self.data_criacao} - Prazo: {prazo}"

class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = []
        self.carregar_tarefas()

    def adicionar_tarefa(self):
        descricao = input("Digite a tarefa: ")
        prioridade = input("Defina a prioridade da tarefa (Alta, Média, Baixa): ").capitalize()
        prazo = input("Digite o prazo (DD/MM/AAAA): ")
        tarefa = Tarefa(descricao, prioridade, prazo)
        self.tarefas.append(tarefa)
        print("Tarefa adicionada!")

    def visualizar_tarefas(self):
        self.ordenar_tarefas_por_prioridade()
        print("Tarefas:")
        for i, tarefa in enumerate(self.tarefas):
            print(f"{i + 1}. {tarefa}")

    def remover_tarefa(self):
        self.visualizar_tarefas()
        try:
            indice = int(input("Digite o número da tarefa que deseja remover: ")) - 1
            if 0 <= indice < len(self.tarefas):
                tarefa_removida = self.tarefas.pop(indice)
                print(f"Tarefa '{tarefa_removida.descricao}' removida com sucesso!")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Entrada inválida. Insira um número válido.")

    def editar_tarefa(self):
        self.visualizar_tarefas()
        try:
            indice = int(input("Insira o número da tarefa que deseja editar: ")) - 1
            if 0 <= indice < len(self.tarefas):
                nova_descricao = input("Digite a nova descrição: ")
                self.tarefas[indice].descricao = nova_descricao
                print("Tarefa atualizada com sucesso!")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

    def salvar_tarefas(self):
        with open('tarefas.json', 'w') as arquivo: 
            json.dump([tarefa.__dict__ for tarefa in self.tarefas], arquivo)
        print("Tarefas salvas com sucesso!")

    def carregar_tarefas(self):
        if os.path.exists('tarefas.json'): 
            with open('tarefas.json', 'r') as arquivo:
                self.tarefas = [Tarefa(**dados) for dados in json.load(arquivo)]
            print("Tarefas carregadas com sucesso!")

    def marcar_como_concluida(self):
        self.visualizar_tarefas()
        try:
            indice = int(input("Digite o número da tarefa que deseja marcar como concluída: ")) - 1
            if 0 <= indice < len(self.tarefas):
                self.tarefas[indice].concluida = True
                print("Tarefa marcada como concluída!")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Entrada inválida. Insira um número válido.")

    def marcar_como_pendente(self):
        self.visualizar_tarefas()
        try:
            indice = int(input("Digite o número da tarefa que deseja marcar como pendente: ")) - 1
            if 0 <= indice < len(self.tarefas):
                self.tarefas[indice].concluida = False
                print("Tarefa marcada como pendente!")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Entrada inválida. Insira um número válido.")

    def buscar_tarefa(self):
        try:
            palavra_chave = input("Digite a palavra-chave para buscar: ")
            print("Tarefas encontradas:")
            encontrou_tarefa = False
            for i, tarefa in enumerate(self.tarefas):
                if palavra_chave.lower() in tarefa.descricao.lower():
                    print(f"{i + 1}. {tarefa}")
                    encontrou_tarefa = True
            if not encontrou_tarefa:
                print("Nenhuma tarefa encontrada com a palavra-chave fornecida.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    def definir_prioridade(self):
        self.visualizar_tarefas()
        try:
            indice = int(input("Digite o número da tarefa para definir a prioridade: ")) - 1
            if 0 <= indice < len(self.tarefas):
                nova_prioridade = input("Defina a nova prioridade da tarefa (Alta, Média, Baixa): ").capitalize()
                self.tarefas[indice].prioridade = nova_prioridade
                print("Prioridade atualizada!")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Entrada inválida. Insira um número válido.")

    def ordenar_tarefas_por_prioridade(self):
        prioridades = {"Alta": 1, "Média": 2, "Baixa": 3}
        self.tarefas.sort(key=lambda x: prioridades.get(x.prioridade, 3))
        print("Tarefas ordenadas por prioridade!")

    def executar(self):
        while True:
            print("\n1 = Adicionar Tarefa")
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
                self.adicionar_tarefa()
            elif escolha == "2":
                self.visualizar_tarefas()
            elif escolha == "3":
                self.salvar_tarefas()
                print("Saindo...")
                break
            elif escolha == "4":
                self.remover_tarefa()
            elif escolha == "5":
                self.editar_tarefa()
            elif escolha == "6":
                self.marcar_como_concluida()
            elif escolha == "7":
                self.marcar_como_pendente()
            elif escolha == "8":
                self.buscar_tarefa()
            elif escolha == "9":
                self.definir_prioridade()
            else:
                print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    gerenciador = GerenciadorDeTarefas()
    gerenciador.executar()
