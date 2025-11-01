# import sys, os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import pytest
# from src.contato import ContatoManager

# def test_adicionar_contato_valido():
#     manager = ContatoManager()
#     manager.adicionar("João", "joao@email.com", "999999999")
#     assert len(manager.listar()) == 1
#     assert manager.listar()[0]["nome"] == "João"

# def test_nao_permitir_nome_vazio():
#     manager = ContatoManager()
#     with pytest.raises(ValueError):
#         manager.adicionar("", "joao@email.com", "999999999")

# def test_nao_permitir_email_invalido():
#     manager = ContatoManager()
#     with pytest.raises(ValueError):
#         manager.adicionar("João", "email_invalido", "999999999")

# def test_atualizar_contato_existente():
#     manager = ContatoManager()
#     manager.adicionar("Maria", "maria@email.com", "888888888")
#     manager.atualizar("Maria", novo_telefone="777777777")
#     contato = manager.listar()[0]
#     assert contato["telefone"] == "777777777"

# def test_remover_contato_inexistente():
#     manager = ContatoManager()
#     with pytest.raises(KeyError):
#         manager.remover("Carlos")

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.contato import ContatoManager

def test_adicionar_contato_valido():
    manager = ContatoManager()
    manager.adicionar("João", "joao@email.com", "999999999")
    
    # 👇 ADICIONE ESTES PRINTS:
    print(f"\n=== TESTE: Adicionar Contato Válido ===")
    print(f"📞 Contatos após adição: {manager.listar()}")
    print(f"📊 Total de contatos: {len(manager.listar())}")
    print("========================================\n")
    
    assert len(manager.listar()) == 1
    assert manager.listar()[0]["nome"] == "João"

def test_nao_permitir_nome_vazio():
    manager = ContatoManager()
    
    # 👇 ADICIONE ESTES PRINTS:
    print(f"\n=== TESTE: Nome Vazio ===")
    print("🚫 Tentando adicionar contato com nome vazio...")
    
    with pytest.raises(ValueError):
        manager.adicionar("", "joao@email.com", "999999999")
    
    print("✅ Corretamente impediu nome vazio!")
    print("==================================\n")

def test_nao_permitir_email_invalido():
    manager = ContatoManager()
    
    # 👇 ADICIONE ESTES PRINTS:
    print(f"\n=== TESTE: Email Inválido ===")
    print("🚫 Tentando adicionar com email inválido...")
    
    with pytest.raises(ValueError):
        manager.adicionar("João", "email_invalido", "999999999")
    
    print("✅ Corretamente impediu email inválido!")
    print("======================================\n")

def test_atualizar_contato_existente():
    manager = ContatoManager()
    manager.adicionar("Maria", "maria@email.com", "888888888")
    
    # 👇 ADICIONE ESTES PRINTS:
    print(f"\n=== TESTE: Atualizar Contato ===")
    print(f"📝 Contato ANTES da atualização: {manager.listar()}")
    
    manager.atualizar("Maria", novo_telefone="777777777")
    
    print(f"🔄 Contato DEPOIS da atualização: {manager.listar()}")
    print("==================================\n")
    
    contato = manager.listar()[0]
    assert contato["telefone"] == "777777777"

def test_remover_contato_inexistente():
    manager = ContatoManager()
    
    # 👇 ADICIONE ESTES PRINTS:
    print(f"\n=== TESTE: Remover Contato Inexistente ===")
    print("🚫 Tentando remover contato que não existe...")
    
    with pytest.raises(KeyError):
        manager.remover("Carlos")
    
    print("✅ Corretamente gerou erro para contato inexistente!")
    print("==================================================\n")