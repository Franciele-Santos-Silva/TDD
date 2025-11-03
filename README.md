# Gerenciador de Contatos - Atividade TDD

## Sobre o Projeto

Sistema de gerenciamento de contatos desenvolvido seguindo a metodologia **TDD (Test-Driven Development)**. O projeto implementa operações CRUD (Create, Read, Update, Delete) com validações robustas para garantir a integridade dos dados.

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

1. **Clone o repositório:**

```bash
git clone [URL do repositório]
cd TDD
