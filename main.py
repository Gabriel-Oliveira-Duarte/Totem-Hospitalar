from datetime import datetime


class Paciente:
    def __init__(self, nome: str, idade: int, pcd: str):
        self.nome = nome.strip()
        self.idade = int(idade)
        self.pcd = pcd.strip().upper() == "S"

    def eh_prioritario(self):
        return self.idade >= 60 or self.pcd

    def tipo_atendimento(self):
        if self.eh_prioritario():
            return "PRIORITÁRIO (Lei 10.048)"
        return "Geral"

    def dados(self):
        return {
            "nome": self.nome,
            "idade": self.idade,
            "pcd": self.pcd
        }

    def __str__(self):
        return f"Paciente: {self.nome} | Idade: {self.idade} | PCD: {'Sim' if self.pcd else 'Não'}"


class Classificador:
    def classificar(self, paciente):
        if paciente.idade >= 60 or paciente.pcd:
            return "PRIORITÁRIO"
        else:
            return "Geral"


class GeradorSenha:
    def __init__(self):
        self.senhas_gerais = 0  
        self.senhas_prioridade = 0  

    def gerar_senha(self, tipo: str) -> str:
        if tipo == 'G':
            self.senhas_gerais += 1
            return f"G-{self.senhas_gerais:03d}"
        elif tipo == 'P':
            self.senhas_prioridade += 1
            return f"P-{self.senhas_prioridade:03d}"
        else:
            raise ValueError("Tipo inválido! Use 'G' para geral ou 'P' para prioridade.")


class Impressora:
    def imprimir_ticket(self, paciente, tipo, servico, senha):
        data = datetime.now().strftime("%d/%m/%Y %H:%M")
        print("\n------------------------------------------")
        print("            TICKET DE ATENDIMENTO")
        print("------------------------------------------")
      
        if isinstance(paciente, str):
            nome_paciente = paciente
        else:
            nome_paciente = paciente.nome  

        print("PACIENTE:", nome_paciente)
        print("TIPO:", tipo)
        print("SERVIÇO:", servico)
        print("SENHA:", senha)
        print("DATA:", data)
        print("------------------------------------------")
        print("Aguarde ser chamado no painel central.")
        print("------------------------------------------")


class Hospital:
    def menu(self):
        print("HOSPITAL VIVER BEM AUTOATENDIMENTO")
        print("Menu de serviços")
        print("1 - Consulta médica")
        print("2 - Exames")
        print("3 - Emergência")

        opcao = input("Escolha uma opção: ")
        print("Serviço escolhido:", opcao)
        return int(opcao)

class Triagem:
    def verificar(self, opcao_servico, paciente):
        if opcao_servico == 3:
            print("\n------------------------------------------")
            print("          ALERTA DE EMERGÊNCIA")
            print("------------------------------------------")
            print("PACIENTE:", paciente.nome)
            print("STATUS: RISCO IMEDIATO")
            print(">>> ENCAMINHAR IMEDIATAMENTE AO BOX MÉDICO")
            print("------------------------------------------")
            return True
        return False


def main():
    impressora = Impressora()
    gerador_senha = GeradorSenha()
    classificador = Classificador()
    hospital = Hospital()
    triagem = Triagem()

    while True:
        print("\nBem-vindo ao sistema de autoatendimento do Hospital Viver Bem!")
        
        nome = input("Digite o nome do paciente: ")
        idade = input("Digite a idade do paciente: ")
        pcd = input("O paciente é PCD? (S/N): ")

        paciente = Paciente(nome, idade, pcd)
        
        tipo_atendimento = paciente.tipo_atendimento()
        tipo = "P" if tipo_atendimento == "PRIORITÁRIO (Lei 10.048)" else "G"
        

        opcao_servico = hospital.menu()
        

        if triagem.verificar(opcao_servico, paciente):
            tipo_atendimento = "EMERGÊNCIA"


        senha = gerador_senha.gerar_senha(tipo)
        

        servico = "Consulta médica" if opcao_servico == 1 else "Exames" if opcao_servico == 2 else "Emergência"
        impressora.imprimir_ticket(paciente, tipo_atendimento, servico, senha)
        

        continuar = input("\nDeseja cadastrar outro paciente? (S/N): ").strip().upper()
        if continuar != "S":
            print("Sistema encerrado. Até logo!")
            break


if __name__ == "__main__":
    main()