# BUGLOG - Registro do Ciclo de Vida de Erros

| ID | Função Afetada | Descrição do Erro | Estado Atual | Responsável | Decisão/Motivo | Tempo (min) |
|----|----------------|-------------------|--------------|-------------|----------------|-------------|
| 1 | `adicionar()` | Sistema aceitava emails sem formato válido (falta de @ ou .) | Fechado | Desenvolvedor | Implementada função `validar_email()` com expressão regular | 25 |
| 2 | `adicionar()` | Permitia cadastro com nome vazio ou apenas espaços | Fechado | Desenvolvedor | Adicionada verificação `if not nome:` para validar nome | 15 |
| 3 | `atualizar()` | Atualização permitia alterar para email inválido | Fechado | Desenvolvedor | Aplicada mesma validação de email na função de atualização | 20 |
| 4 | `remover()` | Mensagem de erro genérica ao tentar remover contato inexistente | Fechado | Desenvolvedor | Especificada mensagem "Contato não encontrado." para melhor UX | 10 |

## Ciclo de Vida dos Erros - Exemplo (ID 1)

1. **NOVO** (00:00) → Erro identificado durante teste `test_nao_permitir_email_invalido`
2. **ABERTO** (00:05) → Confirmado como defeito real pelo desenvolvedor
3. **ATRIBUIDO** (00:10) → Designado para correção pelo próprio desenvolvedor
4. **CORRIGIDO** (00:25) → Implementada função `validar_email()` com regex
5. **FECHADO** (00:30) → Teste `test_nao_permitir_email_invalido` passou com sucesso

## Métricas do Projeto

- **Total de erros encontrados:** 4
- **Taxa de reabertura:** 0% (nenhum erro reaberto)
- **Tempo médio por correção:** 17.5 minutos
- **Tempo total em correções:** 70 minutos
