class Hospital:
    def menu(self):
        print("HOSPITAL VIVER BEM AUTOATENDIMENTO")
        print("Menu de serviços")
        print("1 - Consulta médica")
        print("2 - Exames")
        print("3 - Emergência")

        opcao = input("Escolha uma opção: ")

        print("Serviço escolhido:", opcao)

 
hospital = Hospital()
hospital.menu()