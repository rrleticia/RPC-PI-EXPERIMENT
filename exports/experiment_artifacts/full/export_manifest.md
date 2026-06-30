# Manifesto da exportação

## Identificação

- Notebook: `10_export_experiment_artifacts`
- Criado em UTC: `2026-06-30T16:03:11.380385+00:00`
- Projeto: `/workspace/pi-defense-exp`
- Modo da execução: `full`
- Modo da exportação: `zip_from_sources_no_intermediate_copy`

## Escopo

A exportação indexa os artefatos originais do projeto e cria um `.zip` diretamente a partir desses caminhos, sem cópia intermediária dos diretórios grandes para `exports/`.

## Totais planejados

- Arquivos indexados: `603`
- Tamanho total estimado: `6188.83 MB`
- Fontes opcionais ausentes: `5`
- Itens ignorados por política: `22`

## Arquivo compactado final

O arquivo compactado será gerado em:

```text
/workspace/zip_files/experiment_artifacts_full.zip
```

## Itens excluídos por padrão

Por padrão, não são incluídos caches, ambiente virtual, checkpoints automáticos, `__pycache__` e adaptadores de modelo, a menos que a configuração correspondente seja habilitada.
