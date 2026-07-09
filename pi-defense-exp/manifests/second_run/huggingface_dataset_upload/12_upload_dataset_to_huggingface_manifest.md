# Manifesto — Upload do dataset para Hugging Face

## Identificação

- Notebook: `12_upload_dataset_to_huggingface`
- Gerado em UTC: `2026-07-09T02:22:31.651134+00:00`
- Dataset repo: `leinha/pi-defense-experiment-dataset`
- Repo type: `dataset`
- Dry run: `False`
- Private repo: `True`
- Sem cópia intermediária pesada: `True`

## Fontes incluídas

| Source | Target in repo | Required | Description |
|---|---|---:|---|
| `/workspace/pi-defense-exp/data/canonical` | `data/canonical` | True | Canonical clean and attacked JSONL files. |
| `/workspace/pi-defense-exp/data/views` | `data/views` | True | Training and evaluation views used by the scenarios. |
| `/workspace/pi-defense-exp/configs` | `configs` | False | Experiment and training configuration files. |
| `/workspace/pi-defense-exp/manifests/data` | `manifests/data` | False | Dataset creation manifests. |
| `/workspace/pi-defense-exp/manifests/environment` | `manifests/environment` | False | Environment setup manifests. |

## Fontes opcionais ausentes

| Source | Target in repo | Required | Reason |
|---|---|---:|---|
| _None_ | _None_ |  | _None_ |

## Resumo

- Arquivos candidatos: `22`
- Tamanho total estimado: `36.66 MB`
- Diretório local de metadados leves: `/workspace/pi-defense-exp/exports/huggingface_dataset_upload`
- Diretório de logs: `/workspace/pi-defense-exp/logs/huggingface_dataset_upload`

## Observações

- Este notebook não copia os dados para `exports/` antes do upload.
- Os arquivos são enviados diretamente dos diretórios originais do projeto.
- `data/cache/`, `.venv/`, adaptadores, logs e resultados não fazem parte deste upload de dataset.
- O dataset pode conter conteúdo sensível de HSOL e templates de prompt injection.
- Recomenda-se revisar o dataset card antes de tornar o repositório público.
