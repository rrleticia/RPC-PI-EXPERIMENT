# Manifesto da reprodução rápida

- Criado em UTC: `2026-07-02T14:24:06.932452+00:00`
- Pasta da reprodução: `/workspace/pi-defense-rpdct`
- Ambiente virtual: `/workspace/pi-defense-rpdct/.venv`
- Requirements: `/workspace/pi-defense-rpdct/requirements-rpdct.txt`
- Dataset repo: `leinha/pi-defense-experiment-dataset`
- Adapter repo: `leinha/pi-defense-adapters`
- Modelo base: `meta-llama/Llama-3.1-8B-Instruct`
- Judge WR: `Qwen/Qwen3-8B`
- Amostra por split: `20`
- Seeds: `[42]`

## Artefatos principais

- Métricas rápidas: `/workspace/pi-defense-rpdct/results/quick/quick_metrics.csv`
- Win Rate judgments: `/workspace/pi-defense-rpdct/results/quick/win_rate_judgments.jsonl`
- Win Rate summary: `/workspace/pi-defense-rpdct/results/quick/win_rate_summary.csv`
- Resumo final: `/workspace/pi-defense-rpdct/results/quick/reproduction_summary.csv`
- Log de eventos: `/workspace/pi-defense-rpdct/logs/quick/01_reproduce_from_huggingface_events.jsonl`

## Observação

Esta reprodução é um smoke test pequeno. Ela valida o carregamento dos artefatos publicados no Hugging Face e calcula métricas em uma amostra reduzida. Os resultados completos devem ser obtidos pelos notebooks principais do experimento.
