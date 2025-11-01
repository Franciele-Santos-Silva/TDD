import re

def validar_email(email):
    """Verifica se o e-mail tem formato válido."""
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

class ContatoManager:
    def __init__(self):
        self.contatos = {}

    def adicionar(self, nome, email, telefone):
        """Adiciona um novo contato após validar os dados."""
        if not nome:
            raise ValueError("Nome não pode ser vazio.")
        if not validar_email(email):
            raise ValueError("E-mail inválido.")
        self.contatos[nome] = {"nome": nome, "email": email, "telefone": telefone}

    def listar(self):
        """Retorna a lista de contatos."""
        return list(self.contatos.values())

    def atualizar(self, nome, novo_email=None, novo_telefone=None):
        """Atualiza dados de um contato existente."""
        if nome not in self.contatos:
            raise KeyError("Contato não encontrado.")
        if novo_email and not validar_email(novo_email):
            raise ValueError("E-mail inválido.")
        if novo_email:
            self.contatos[nome]["email"] = novo_email
        if novo_telefone:
            self.contatos[nome]["telefone"] = novo_telefone

    def remover(self, nome):
        """Remove um contato pelo nome."""
        if nome not in self.contatos:
            raise KeyError("Contato não encontrado.")
        del self.contatos[nome]
