
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
            raise ValueError("Tipo inválido!. Use 'G' para geral ou 'P' para prioridade.")