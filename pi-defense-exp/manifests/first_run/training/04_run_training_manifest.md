# Manifesto de treinamento — Notebook 04

## Identificação

- Notebook: `04_run_training`
- Gerado em UTC: `2026-06-29T19:14:00.248047+00:00`
- Diretório raiz do projeto: `/workspace/pi-defense-exp`
- Modelo base: `meta-llama/Llama-3.1-8B-Instruct`

## Seeds

- Seed do dataset: `42`
- Seeds experimentais de treinamento: `[42, 123, 2026]`
- Réplicas por cenário treinável: `3`
- Total esperado de execuções de adaptadores: `9`

A seed do dataset identifica a base experimental criada no notebook `02_dataset_creation.ipynb`. Ela deve permanecer fixa para preservar os mesmos splits, amostras e ataques.

As seeds experimentais de treinamento representam réplicas independentes para os cenários C2, C3 e C4. Cada adaptador salvo neste notebook deve estar associado a uma seed específica.

## Ambiente

- Python atual: `/workspace/pi-defense-exp/.venv/bin/python`
- Python esperado: `/workspace/pi-defense-exp/.venv/bin/python`
- Plataforma: `Linux-6.8.0-40-generic-x86_64-with-glibc2.39`

## GPU

- GPU: `NVIDIA GeForce RTX 5090`
- Memória total aproximada: `31.37 GB`
- CUDA no PyTorch: `12.8`
- Precisão usada: `bf16`

## Cenários executados

`c2_struq_sft`, `c3_secalign_dpo`, `c4_ih_sft`

## Resultados de treinamento

| Scenario | Seed | Method | Train rows | Validation rows | Adapter dir | Elapsed seconds |
|---|---:|---|---:|---:|---|---:|
| `c2_struq_sft` | 42 | `sft` | 4200 | 700 | `/workspace/pi-defense-exp/adapters/struq/seed_42` | 1348.08 |
| `c2_struq_sft` | 123 | `sft` | 4200 | 700 | `/workspace/pi-defense-exp/adapters/struq/seed_123` | 1342.44 |
| `c2_struq_sft` | 2026 | `sft` | 4200 | 700 | `/workspace/pi-defense-exp/adapters/struq/seed_2026` | 1360.71 |
| `c3_secalign_dpo` | 42 | `dpo` | 2100 | 350 | `/workspace/pi-defense-exp/adapters/secalign/seed_42` | 841.04 |
| `c3_secalign_dpo` | 123 | `dpo` | 2100 | 350 | `/workspace/pi-defense-exp/adapters/secalign/seed_123` | 842.09 |
| `c3_secalign_dpo` | 2026 | `dpo` | 2100 | 350 | `/workspace/pi-defense-exp/adapters/secalign/seed_2026` | 842.80 |
| `c4_ih_sft` | 42 | `sft` | 4200 | 700 | `/workspace/pi-defense-exp/adapters/ih/seed_42` | 1368.24 |
| `c4_ih_sft` | 123 | `sft` | 4200 | 700 | `/workspace/pi-defense-exp/adapters/ih/seed_123` | 1358.05 |
| `c4_ih_sft` | 2026 | `sft` | 4200 | 700 | `/workspace/pi-defense-exp/adapters/ih/seed_2026` | 1335.56 |

## Adaptadores

| Scenario | Seed | Exists | Number of files | Output dir |
|---|---:|---:|---:|---|
| `c2_struq_sft` | 42 | True | 29 | `/workspace/pi-defense-exp/adapters/struq/seed_42` |
| `c2_struq_sft` | 123 | True | 29 | `/workspace/pi-defense-exp/adapters/struq/seed_123` |
| `c2_struq_sft` | 2026 | True | 29 | `/workspace/pi-defense-exp/adapters/struq/seed_2026` |
| `c3_secalign_dpo` | 42 | True | 29 | `/workspace/pi-defense-exp/adapters/secalign/seed_42` |
| `c3_secalign_dpo` | 123 | True | 29 | `/workspace/pi-defense-exp/adapters/secalign/seed_123` |
| `c3_secalign_dpo` | 2026 | True | 29 | `/workspace/pi-defense-exp/adapters/secalign/seed_2026` |
| `c4_ih_sft` | 42 | True | 29 | `/workspace/pi-defense-exp/adapters/ih/seed_42` |
| `c4_ih_sft` | 123 | True | 29 | `/workspace/pi-defense-exp/adapters/ih/seed_123` |
| `c4_ih_sft` | 2026 | True | 29 | `/workspace/pi-defense-exp/adapters/ih/seed_2026` |

## Configuração LoRA/QLoRA

- r: `16`
- lora_alpha: `32`
- lora_dropout: `0.05`
- target_modules: `{'gate_proj', 'down_proj', 'up_proj', 'k_proj', 'q_proj', 'v_proj', 'o_proj'}`
- quantização: `4-bit nf4`
- compute dtype: `bf16`

## Logs

- Log resumido textual: `/workspace/pi-defense-exp/logs/training/04_run_training.log`
- Log resumido JSON: `/workspace/pi-defense-exp/logs/training/04_run_training_summary.json`
- Log incremental de eventos: `/workspace/pi-defense-exp/logs/training/04_run_training_events.jsonl`
- Diretório de logs por run: `/workspace/pi-defense-exp/logs/training/runs`

O log incremental de eventos registra início, conclusão e falha de cada combinação cenário-seed. Os diretórios individuais de run armazenam metadados específicos e, em caso de erro, um arquivo `error.txt` com o traceback.

## Observações

- C0 e C1 não treinam adaptadores e não são executados neste notebook.
- C2 e C4 usam SFT com exemplos limpos e atacados vistos.
- C3 usa DPO apenas com exemplos atacados vistos.
- Todos os cenários treinados partem do mesmo checkpoint base.
- Cada cenário treinável é executado uma vez para cada seed experimental.
- Os adaptadores são salvos em subdiretórios específicos por seed.
- A qualidade dos adaptadores será medida posteriormente no notebook de avaliação.
