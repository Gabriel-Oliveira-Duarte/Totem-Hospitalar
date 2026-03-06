
````markdown
# Totem Hospitalar - Sistema de Atendimento

Este projeto é um sistema de atendimento automatizado para um hospital, onde pacientes podem se cadastrar e escolher o
tipo de serviço desejado. O sistema gera senhas e imprime tickets de atendimento.

## Funcionalidades

- Cadastro de pacientes com nome, idade e se é PCD.
- Classificação do paciente como **Prioritário** ou **Geral**.
- Geração de senhas (prioritário ou geral).
- Triagem para casos de emergência.
- Impressão de tickets com dados do paciente.

## Como Executar

### Pré-requisitos

- **Python 3.x** instalado em sua máquina.
- **Visual Studio Code (VSCode)** instalado (opcional, mas recomendado).
- Ou qualquer terminal (CMD, PowerShell, Terminal do VSCode, etc.)

### Passos

1. **Clone o repositório**:

```bash
git clone https://github.com/SEU_USUARIO/totem-hospitalar.git
````

2. **Abra o terminal e execute o sistema**:

   **Se estiver usando o VSCode**:

   * O **VSCode** possui um terminal integrado que você pode usar para rodar o sistema. Para abrir o terminal, vá até a opção **Terminal → New Terminal**.
   * Depois de abrir o terminal integrado, você pode executar o código com o comando:

   ```bash
   python main.py
   ```

   **Alternativa no VSCode**:

   * Se preferir uma forma mais simples, você pode usar a opção **Run Python File in Terminal**, que executa automaticamente o arquivo `main.py` no terminal integrado.
   * Basta clicar no botão de **play** no canto superior direito do **VSCode**, ou usar o atalho **Ctrl+Shift+P** (Windows) ou **Cmd+Shift+P** (Mac) e buscar por "Run Python File in Terminal".

   **Se estiver usando o CMD ou PowerShell**:

   * Abra o **CMD** ou **PowerShell**, navegue até a pasta do projeto usando o comando `cd` e então execute o sistema com:

   ```bash
   python main.py
   ```

### Interação com o sistema

O sistema pedirá os dados do paciente, selecionará o serviço desejado e gerará a senha, imprimindo o ticket correspondente. Você pode continuar cadastrando novos pacientes ou encerrar o sistema.

## Estrutura de Pastas

```plaintext
/totem-hospitalar
│
├── main.py           # Arquivo principal com o loop do sistema
├── /models           # Pasta com as classes do sistema
│ ├── paciente.py     # Classe Paciente
│ ├── classificador.py # Classe Classificador
│ ├── triagem.py      # Classe Triagem
│ ├── menu.py         # Classe Hospital (Menu de serviços)
│ ├── gerador_senha.py # Classe GeradorSenha
│ └── impressora.py   # Classe Impressora
└── README.md         # Este arquivo
```
