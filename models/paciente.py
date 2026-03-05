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
    
if __name__ == "__main__":
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    pcd = input("Possui deficiência? (S/N): ")

    paciente = Paciente(nome, idade, pcd)

    print("\nDados do paciente:")
    print(paciente)
    print("É prioritário?", paciente.eh_prioritario())
    print("Tipo de atendimento:", paciente.tipo_atendimento())
    print("Dados completos:", paciente.dados())