
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

2. **Abra o projeto no Visual Studio Code (VSCode)** (opcional):

   * Se estiver utilizando o **VSCode**, abra o diretório do projeto com o comando abaixo:

```bash
code .
```

3. **Execute o sistema**:

   * No **VSCode**, você pode rodar o sistema diretamente no terminal integrado, ou usar **CMD** ou qualquer terminal para rodar o arquivo `main.py`.

   * Para rodar o sistema, basta executar o arquivo `main.py` com o seguinte comando:

```bash
python main.py
```

* Isso pode ser feito tanto no **VSCode** quanto em um terminal como o **CMD** ou **PowerShell**.

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

Agora, o **README.md** está claro sobre como executar o sistema em diversos ambientes, seja no **VSCode**, **CMD**, ou outros terminais.
```
