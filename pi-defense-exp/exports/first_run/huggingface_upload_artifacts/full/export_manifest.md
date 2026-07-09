# Manifesto — Hugging Face Upload Artifacts Export

## Identificação

- Notebook: `13_export_huggingface_upload_artifacts`
- Gerado em UTC: `2026-07-02T04:04:01.632032+00:00`
- Projeto: `/workspace/pi-defense-exp`
- Export root: `/workspace/pi-defense-exp/exports/huggingface_upload_artifacts/full`
- Zip final: `/workspace/zip_files/huggingface_upload_artifacts_full.zip`

## Política

Este notebook não copia adaptadores, datasets, caches ou pesos de modelo para `exports/`.

O zip final é criado lendo diretamente os arquivos leves de logs, manifestos e metadados produzidos pelos notebooks 11 e 12.

## Fontes consideradas

| source_name | source_path | exists | archive_root | required |
| --- | --- | --- | --- | --- |
| model_upload_exports | /workspace/pi-defense-exp/exports/huggingface_upload | True | huggingface_upload_artifacts/model_upload/exports | False |
| model_upload_logs | /workspace/pi-defense-exp/logs/huggingface_upload | True | huggingface_upload_artifacts/model_upload/logs | False |
| model_upload_manifests | /workspace/pi-defense-exp/manifests/huggingface_upload | True | huggingface_upload_artifacts/model_upload/manifests | False |
| dataset_upload_exports | /workspace/pi-defense-exp/exports/huggingface_dataset_upload | True | huggingface_upload_artifacts/dataset_upload/exports | False |
| dataset_upload_logs | /workspace/pi-defense-exp/logs/huggingface_dataset_upload | True | huggingface_upload_artifacts/dataset_upload/logs | False |
| dataset_upload_manifests | /workspace/pi-defense-exp/manifests/huggingface_dataset_upload | True | huggingface_upload_artifacts/dataset_upload/manifests | False |

## Resumo

| Campo | Valor |
|---|---:|
| Arquivos indexados | 16 |
| Tamanho total indexado MB | 0.0741 |
| Fontes opcionais ausentes | 0 |
| Arquivos ignorados por política | 0 |

## Arquivos de índice

- `index/file_index.csv`
- `index/file_index.json`
- `index/missing_optional_sources.json`
- `index/skipped_files.json`

## Observação

Fontes opcionais ausentes não indicam necessariamente erro. Elas indicam apenas que o notebook procurou artefatos esperados, mas eles ainda não foram gerados ou foram salvos em outro local.
