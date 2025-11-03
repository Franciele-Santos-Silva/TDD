# Gerenciador de Contatos - Atividade TDD

## Sobre o Projeto

Sistema de gerenciamento de contatos desenvolvido seguindo a metodologia **TDD (Test-Driven Development)**. O projeto implementa operações CRUD (Create, Read, Update, Delete) com validações robustas para garantir a integridade dos dados.

## Tecnologias e Bibliotecas

### **Linguagem e Ferramentas**

- **Python 3.10+** - Linguagem de programação principal
- **pytest** - Framework de testes automatizados
- **re** - Biblioteca nativa para expressões regulares

## Funcionalidades Implementadas

### Operações CRUD

- **Create** - Adicionar novos contatos
- **Read** - Listar todos os contatos  
- **Update** - Atualizar contatos existentes
- **Delete** - Remover contatos

### Validações

- **Nome**: Não permite nome vazio ou apenas espaços
- **Email**: Valida formato com expressão regular (deve conter @ e .)
- **Existência**: Verifica se contato existe antes de operações

## Como Executar

### Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes do Python)

### Instalação

1. Clone o repositório:

   ```bash
   git clone [URL do repositório]
   cd TDD

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   venv\Scripts\activate

3. Instale as dependências do requirements.txt:

   ```bash
   pip install -r requirements.txt

4. Executar Testes TDD:

   Executa testes mostrando os prints

    ```bash
    pytest -v -s
