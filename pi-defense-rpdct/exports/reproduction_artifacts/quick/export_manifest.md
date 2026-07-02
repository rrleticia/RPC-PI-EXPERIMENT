# Manifesto da exportação da reprodução rápida

## Identificação

- Notebook: `02_export_reproduction_artifacts`
- Gerado em UTC: `2026-07-02T15:26:44.913544+00:00`
- Raiz da reprodução: `/workspace/pi-defense-rpdct`
- Modo de execução: `quick`

## Política

A exportação usa uma estratégia sem cópia intermediária pesada. O diretório `exports/` contém apenas metadados leves, enquanto o arquivo `.zip` é criado lendo diretamente os arquivos originais.

## Resumo

| Campo | Valor |
|---|---:|
| Arquivos selecionados | 36 |
| Tamanho selecionado MB | 1.12 |
| Fontes opcionais ausentes | 0 |
| Itens ignorados por política | 5 |

## Arquivo compactado esperado

```text
/workspace/zip_files/pi_defense_rpdct_artifacts_quick.zip
```

## Observações

- `.venv/` não é exportado.
- `hf_cache/` não é exportado por padrão.
- `adapter_cache/` não é exportado por padrão.
- Arquivos ausentes em `missing_optional_sources.json` não indicam necessariamente erro; eles podem representar artefatos ainda não gerados.
