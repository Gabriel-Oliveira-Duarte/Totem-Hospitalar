from datetime import datetime

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


impressora = Impressora()

