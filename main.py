from models import Paciente, Classificador, GeradorSenha, Hospital, Triagem, Impressora

def testar_integração():
    paciente1 = Paciente("João", 65, "S")
    paciente2 = Paciente("Maria", 30, "N")

    classificador = Classificador()

    resultado1 = classificador.classificar(paciente1)
    resultado2 = classificador.classificar(paciente2)

    gerador = GeradorSenha()
    senha1 = gerador.gerar_senha('P')
    senha2 = gerador.gerar_senha('G')

    print(f"Paciente: {paciente1.nome} - Atendimento: {resultado1} - Senha: {senha1}")
    print(f"Paciente: {paciente2.nome} - Atendimento: {resultado2} - Senha: {senha2}")

def testar_hospital():
    hospital = Hospital()
    hospital.menu()

def fluxo_emergencia():
    paciente3 = Paciente("Woody Batista", 25, "S")
    triagem = Triagem()
    opcao_servico = 3
    if triagem.verificar(opcao_servico, paciente3):
        print("Atendimento de emergência iniciado.")
    else:
        print("Atendimento geral.")

def gerar_ticket():
    paciente = Paciente("João Guimarães", 72, "N")
    tipo = "PRIORITÁRIO (Lei 10.048)"
    servico = "Exame"
    senha = "P-001"

    impressora = Impressora()
    impressora.imprimir_ticket(paciente, tipo, servico, senha)

if __name__ == "__main__":
    testar_integração()
    testar_hospital()
    fluxo_emergencia()
    gerar_ticket()