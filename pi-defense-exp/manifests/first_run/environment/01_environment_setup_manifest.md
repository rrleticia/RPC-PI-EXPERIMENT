# Manifesto do ambiente — Notebook 01

## Identificação

- Notebook: `01_environment_setup`
- Gerado em UTC: `2026-06-29T11:32:35.445593+00:00`
- Diretório raiz do projeto: `/workspace/pi-defense-exp`

## Kernel e Python

- Kernel esperado: `Python (pi-defense-exp)`
- Python esperado: `/workspace/pi-defense-exp/.venv/bin/python`
- Python atual: `/workspace/pi-defense-exp/.venv/bin/python`
- Python atual corresponde ao esperado: `True`

## Sistema

- Plataforma: `Linux-6.8.0-40-generic-x86_64-with-glibc2.39`
- Máquina: `x86_64`
- Processador: `x86_64`

## GPU

- `nvidia-smi` disponível: `True`
- Código de retorno: `0`

## Pacotes principais

| Package | Distribution | Version | Import available | Status |
|---|---|---:|---:|---|
| torch | torch | 2.8.0+cu128 | True | ok |
| transformers | transformers | None | False | missing |
| accelerate | accelerate | None | False | missing |
| peft | peft | None | False | missing |
| trl | trl | None | False | missing |
| datasets | datasets | 5.0.0 | True | ok |
| huggingface_hub | huggingface-hub | 1.21.0 | True | ok |
| pandas | pandas | 3.0.4 | True | ok |
| numpy | numpy | 2.1.2 | True | ok |

## Arquivos de dependências

- `requirements-data.txt`: `True`
- `requirements-train.txt`: `True`

## Arquivos de configuração

- `configs/experiment.yaml`: `True`

## Diretórios esperados

| Path | Exists |
|---|---:|
| `configs` | True |
| `data/raw` | True |
| `data/cache` | True |
| `data/canonical` | True |
| `data/views/struq` | True |
| `data/views/secalign` | True |
| `data/views/ih` | True |
| `data/views/evaluation` | True |
| `notebooks` | True |
| `scripts` | True |
| `adapters/struq` | True |
| `adapters/secalign` | True |
| `adapters/ih` | True |
| `results/generations` | True |
| `results/metrics` | True |
| `results/tables` | True |
| `results/reports` | True |
| `logs/environment` | True |
| `logs/notebooks` | True |
| `logs/data` | True |
| `logs/training` | True |
| `logs/evaluation` | True |
| `manifests/environment` | True |
| `manifests/notebooks` | True |
| `manifests/data` | True |
| `manifests/training` | True |
| `manifests/evaluation` | True |
