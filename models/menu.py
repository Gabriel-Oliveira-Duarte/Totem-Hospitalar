class Hospital:

    def __init__(self):
        self.nome_paciente = ""
        self.deficiencia = ""

    def menu(self):
        print("HOSPITAL VIVER BEM AUTOATENDIMENTO")
        print("[Cadastro Do Paciente] - Cadastrar paciente")

        self.nome_paciente = input("Digite o nome do paciente: ")
        self.deficiencia = input("Tem alguma deficiência? (s/n): ")

        print("Menu de serviços")
        print("1 - Consulta médica")
        print("2 - Exames")
        print("3 - Emergência")

        opcao = input("Escolha uma opção: ")

        print("Paciente:", self.nome_paciente)
        print("Deficiência:", self.deficiencia)
        print("Serviço escolhido:", opcao)


hospital = Hospital()
hospital.menu()