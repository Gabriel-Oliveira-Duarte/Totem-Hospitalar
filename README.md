# Totem-Hospitalar


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

### Passos

1. **Clone o repositório**:

```bash
git clone https://github.com/SEU_USUARIO/totem-hospitalar.git
````

2. **Entre no diretório do projeto**:

```bash
cd totem-hospitalar
```

3. **Crie um ambiente virtual (opcional, mas recomendado)**

Se estiver usando **Windows**:

```bash
python -m venv venv
```

Se estiver usando **Linux/macOS**:

```bash
python3 -m venv venv
```

4. **Ative o ambiente virtual**

No **Windows**:

```bash
venv\Scripts\activate
```

No **Linux/macOS**:

```bash
source venv/bin/activate
```

5. **Instale as dependências**

Execute o comando abaixo para instalar as dependências necessárias:

```bash
pip install -r requirements.txt
```

6. **Execute o sistema**

Para rodar o sistema, basta executar o arquivo `main.py`:

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

```

Agora o **README.md** está mais direto ao ponto, sem a parte de contribuições ou licença. Se precisar de mais alguma coisa, é só me avisar!
```
