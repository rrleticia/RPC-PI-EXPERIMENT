# Manifesto — Upload dos adaptadores para Hugging Face

## Identificação

- Notebook: `11_upload_adapters_to_huggingface`
- Gerado em UTC: `2026-07-09T02:23:18.827788+00:00`
- Repositório alvo: `leinha/pi-defense-adapters`
- Repositório privado: `True`
- Usuário autenticado: `leinha`
- Dry-run: `False`

## Modelo base

```text
meta-llama/Llama-3.1-8B-Instruct
```

O modelo base não foi enviado por este notebook. Apenas os adaptadores LoRA/QLoRA são considerados para upload.

## Arquivos auxiliares

| Arquivo | Caminho |
|---|---|
| README/model card | `/workspace/pi-defense-exp/exports/huggingface_upload/README.md` |
| Manifesto dos adaptadores | `/workspace/pi-defense-exp/exports/huggingface_upload/experiment_adapters_manifest.json` |
| Exemplos de carregamento | `/workspace/pi-defense-exp/exports/huggingface_upload/adapter_loading_examples.json` |
| Log de eventos | `/workspace/pi-defense-exp/logs/huggingface_upload/11_upload_adapters_to_huggingface_events.jsonl` |

## Metadados enviados

| description | path_in_repo | status |
| --- | --- | --- |
| Repository model card | README.md | uploaded |
| Adapter manifest | experiment_adapters_manifest.json | uploaded |

## Adaptadores

| scenario_id | seed | path_in_repo | status | size_mb |
| --- | --- | --- | --- | --- |
| c2_struq_sft | 42 | c2_struq_sft/seed_42 | uploaded | 610.235897 |
| c2_struq_sft | 123 | c2_struq_sft/seed_123 | uploaded | 610.236034 |
| c2_struq_sft | 2026 | c2_struq_sft/seed_2026 | uploaded | 610.235914 |
| c3_secalign_dpo | 42 | c3_secalign_dpo/seed_42 | uploaded | 610.238959 |
| c3_secalign_dpo | 123 | c3_secalign_dpo/seed_123 | uploaded | 610.238979 |
| c3_secalign_dpo | 2026 | c3_secalign_dpo/seed_2026 | uploaded | 610.238911 |
| c4_ih_sft | 42 | c4_ih_sft/seed_42 | uploaded | 610.235907 |
| c4_ih_sft | 123 | c4_ih_sft/seed_123 | uploaded | 610.236018 |
| c4_ih_sft | 2026 | c4_ih_sft/seed_2026 | uploaded | 610.235898 |

## Verificação remota

- Verificação remota executada: `True`
- Total de arquivos remotos listados: `57`

## Observações

- Em modo `DRY_RUN=True`, nenhum repositório é criado e nenhum arquivo é enviado.
- Checkpoints intermediários são ignorados pelos padrões definidos em `UPLOAD_IGNORE_PATTERNS`.
- O repositório deve ser revisado antes de ser tornado público.
- Tokens Hugging Face não são registrados nos manifestos.
