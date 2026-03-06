class Classificador:
    def classificar(self, paciente):
        if paciente.idade >= 60 or paciente.pcd:
            return "PRIORITÁRIO"
        else:
            return "Geral"
