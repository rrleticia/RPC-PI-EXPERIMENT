# Exportação dos artefatos do experimento

Esta pasta contém os metadados leves da exportação do experimento.

A exportação foi feita no modo:

```text
zip_from_sources_no_intermediate_copy
```

Nesse modo, os artefatos originais não são copiados para dentro de `exports/`. O notebook apenas gera índices e manifestos leves aqui, e o arquivo `.zip` final é criado lendo diretamente os arquivos originais do projeto.

## Caminhos principais

- Projeto: `/workspace/pi-defense-exp`
- Metadados da exportação: `/workspace/pi-defense-exp/exports/experiment_artifacts/full`
- Arquivo compactado final: `/workspace/zip_files/experiment_artifacts_full.zip`

## Arquivos importantes

- `export_summary.json`: resumo geral da exportação.
- `export_manifest.json`: manifesto estruturado da exportação.
- `export_manifest.md`: manifesto legível em Markdown.
- `index/file_index.csv`: índice tabular dos arquivos incluídos no `.zip`.
- `index/file_index.json`: índice em JSON dos arquivos incluídos no `.zip`.
- `index/missing_optional_sources.json`: fontes opcionais que não existiam no projeto.
- `index/skipped_files.json`: arquivos ou pastas ignorados por política de exportação.

## Observação sobre espaço em disco

Como os arquivos originais não são copiados para `exports/`, esta pasta deve permanecer leve. O arquivo `.zip` final fica em uma pasta separada chamada `zip_files`.
