import pytest
from src.contato import ContatoManager

def test_adicionar_contato_valido():
    manager = ContatoManager()
    manager.adicionar("João", "joao@email.com", "999999999")
    assert len(manager.listar()) == 1
    assert manager.listar()[0]["nome"] == "João"

def test_nao_permitir_nome_vazio():
    manager = ContatoManager()
    with pytest.raises(ValueError):
        manager.adicionar("", "joao@email.com", "999999999")

def test_nao_permitir_email_invalido():
    manager = ContatoManager()
    with pytest.raises(ValueError):
        manager.adicionar("João", "email_invalido", "999999999")

def test_atualizar_contato_existente():
    manager = ContatoManager()
    manager.adicionar("Maria", "maria@email.com", "888888888")
    manager.atualizar("Maria", novo_telefone="777777777")
    contato = manager.listar()[0]
    assert contato["telefone"] == "777777777"

def test_remover_contato_inexistente():
    manager = ContatoManager()
    with pytest.raises(KeyError):
        manager.remover("Carlos")
