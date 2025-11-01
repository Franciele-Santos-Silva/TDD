import re

class ContatoManager:
    def __init__(self):
        self.contatos = {}

    def adicionar(self, nome, email, telefone):
        if not nome:
            raise ValueError("Nome não pode ser vazio.")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("E-mail inválido.")
        self.contatos[nome] = {"nome": nome, "email": email, "telefone": telefone}

    def listar(self):
        return list(self.contatos.values())

    def atualizar(self, nome, novo_email=None, novo_telefone=None):
        if nome not in self.contatos:
            raise KeyError("Contato não encontrado.")
        if novo_email:
            self.contatos[nome]["email"] = novo_email
        if novo_telefone:
            self.contatos[nome]["telefone"] = novo_telefone

    def remover(self, nome):
        if nome not in self.contatos:
            raise KeyError("Contato não encontrado.")
        del self.contatos[nome]
