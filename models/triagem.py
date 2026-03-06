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