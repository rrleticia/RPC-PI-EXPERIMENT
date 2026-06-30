# Manifesto de documentação do treinamento — Notebook 03

## Identificação

- Notebook: `03_training_documentation`
- Gerado em UTC: `2026-06-29T11:48:46.537029+00:00`
- Diretório raiz do projeto: `/workspace/pi-defense-exp`
- Kernel esperado: `Python (pi-defense-exp)`
- Python esperado: `/workspace/pi-defense-exp/.venv/bin/python`
- Python atual: `/workspace/pi-defense-exp/.venv/bin/python`

## Manifestos anteriores

- Ambiente: `/workspace/pi-defense-exp/manifests/environment/01_environment_setup_manifest.json` — existe: `True`
- Dataset: `/workspace/pi-defense-exp/manifests/data/02_dataset_creation_manifest.json` — existe: `True`

## Modelo base

- Modelo base: `Qwen/Qwen2.5-1.5B-Instruct`
- Mesmo modelo base para todos os cenários: `True`

## Seeds experimentais

- Seed do dataset: `42`
- Seeds de treinamento: `42`, `123`, `2026`
- Scenario IDs treináveis: `c2_struq_sft`, `c3_secalign_dpo`, `c4_ih_sft`
- Réplicas por cenário treinável: `3`
- Total de execuções de treinamento de adaptadores: `9`

A seed do dataset controla a criação da base experimental e deve permanecer fixa. As seeds de treinamento controlam as réplicas dos cenários `c2_struq_sft`, `c3_secalign_dpo` e `c4_ih_sft`, permitindo calcular médias, desvios padrão e intervalos de confiança na avaliação final.

## Cenários com treinamento

| Scenario ID | Label | Method | Split | Lines | Path |
| --- | --- | --- | --- | --- | --- |
| c2_struq_sft | C2 | sft | train | 4200 | `/workspace/pi-defense-exp/data/views/struq/train_sft.jsonl` |
| c2_struq_sft | C2 | sft | validation | 700 | `/workspace/pi-defense-exp/data/views/struq/validation_sft.jsonl` |
| c3_secalign_dpo | C3 | dpo | train | 2100 | `/workspace/pi-defense-exp/data/views/secalign/train_dpo.jsonl` |
| c3_secalign_dpo | C3 | dpo | validation | 350 | `/workspace/pi-defense-exp/data/views/secalign/validation_dpo.jsonl` |
| c4_ih_sft | C4 | sft | train | 4200 | `/workspace/pi-defense-exp/data/views/ih/train_sft.jsonl` |
| c4_ih_sft | C4 | sft | validation | 700 | `/workspace/pi-defense-exp/data/views/ih/validation_sft.jsonl` |

## Arquivos comuns de avaliação

| Name | Lines | Path |
| --- | --- | --- |
| test_clean | 1876 | `/workspace/pi-defense-exp/data/views/evaluation/test_clean.jsonl` |
| test_attacked_seen | 9380 | `/workspace/pi-defense-exp/data/views/evaluation/test_attacked_seen.jsonl` |
| test_attacked_unseen | 5628 | `/workspace/pi-defense-exp/data/views/evaluation/test_attacked_unseen.jsonl` |

## Diretórios de adaptadores por seed

| Scenario ID | Label | Method | Seed | Path |
| --- | --- | --- | --- | --- |
| c2_struq_sft | C2 | sft | 42 | `/workspace/pi-defense-exp/adapters/struq/seed_42` |
| c2_struq_sft | C2 | sft | 123 | `/workspace/pi-defense-exp/adapters/struq/seed_123` |
| c2_struq_sft | C2 | sft | 2026 | `/workspace/pi-defense-exp/adapters/struq/seed_2026` |
| c3_secalign_dpo | C3 | dpo | 42 | `/workspace/pi-defense-exp/adapters/secalign/seed_42` |
| c3_secalign_dpo | C3 | dpo | 123 | `/workspace/pi-defense-exp/adapters/secalign/seed_123` |
| c3_secalign_dpo | C3 | dpo | 2026 | `/workspace/pi-defense-exp/adapters/secalign/seed_2026` |
| c4_ih_sft | C4 | sft | 42 | `/workspace/pi-defense-exp/adapters/ih/seed_42` |
| c4_ih_sft | C4 | sft | 123 | `/workspace/pi-defense-exp/adapters/ih/seed_123` |
| c4_ih_sft | C4 | sft | 2026 | `/workspace/pi-defense-exp/adapters/ih/seed_2026` |

## Plano de logs incrementais

- Log global de eventos: `/workspace/pi-defense-exp/logs/training/04_run_training_events.jsonl`
- Resumo global de treinamento: `/workspace/pi-defense-exp/logs/training/04_run_training_summary.json`
- Diretório-base de logs por run: `/workspace/pi-defense-exp/logs/training/runs`

Cada run deve registrar eventos incrementais de início, conclusão e falha. Em caso de erro, o traceback deve ser salvo em `error.txt` dentro do diretório específico da combinação `scenario_id`/seed.

| Scenario ID | Label | Method | Seed | Run log dir | Metadata | Error file |
| --- | --- | --- | --- | --- | --- | --- |
| c2_struq_sft | C2 | sft | 42 | `/workspace/pi-defense-exp/logs/training/runs/c2_struq_sft/seed_42` | `/workspace/pi-defense-exp/logs/training/runs/c2_struq_sft/seed_42/run_metadata.json` | `/workspace/pi-defense-exp/logs/training/runs/c2_struq_sft/seed_42/error.txt` |
| c2_struq_sft | C2 | sft | 123 | `/workspace/pi-defense-exp/logs/training/runs/c2_struq_sft/seed_123` | `/workspace/pi-defense-exp/logs/training/runs/c2_struq_sft/seed_123/run_metadata.json` | `/workspace/pi-defense-exp/logs/training/runs/c2_struq_sft/seed_123/error.txt` |
| c2_struq_sft | C2 | sft | 2026 | `/workspace/pi-defense-exp/logs/training/runs/c2_struq_sft/seed_2026` | `/workspace/pi-defense-exp/logs/training/runs/c2_struq_sft/seed_2026/run_metadata.json` | `/workspace/pi-defense-exp/logs/training/runs/c2_struq_sft/seed_2026/error.txt` |
| c3_secalign_dpo | C3 | dpo | 42 | `/workspace/pi-defense-exp/logs/training/runs/c3_secalign_dpo/seed_42` | `/workspace/pi-defense-exp/logs/training/runs/c3_secalign_dpo/seed_42/run_metadata.json` | `/workspace/pi-defense-exp/logs/training/runs/c3_secalign_dpo/seed_42/error.txt` |
| c3_secalign_dpo | C3 | dpo | 123 | `/workspace/pi-defense-exp/logs/training/runs/c3_secalign_dpo/seed_123` | `/workspace/pi-defense-exp/logs/training/runs/c3_secalign_dpo/seed_123/run_metadata.json` | `/workspace/pi-defense-exp/logs/training/runs/c3_secalign_dpo/seed_123/error.txt` |
| c3_secalign_dpo | C3 | dpo | 2026 | `/workspace/pi-defense-exp/logs/training/runs/c3_secalign_dpo/seed_2026` | `/workspace/pi-defense-exp/logs/training/runs/c3_secalign_dpo/seed_2026/run_metadata.json` | `/workspace/pi-defense-exp/logs/training/runs/c3_secalign_dpo/seed_2026/error.txt` |
| c4_ih_sft | C4 | sft | 42 | `/workspace/pi-defense-exp/logs/training/runs/c4_ih_sft/seed_42` | `/workspace/pi-defense-exp/logs/training/runs/c4_ih_sft/seed_42/run_metadata.json` | `/workspace/pi-defense-exp/logs/training/runs/c4_ih_sft/seed_42/error.txt` |
| c4_ih_sft | C4 | sft | 123 | `/workspace/pi-defense-exp/logs/training/runs/c4_ih_sft/seed_123` | `/workspace/pi-defense-exp/logs/training/runs/c4_ih_sft/seed_123/run_metadata.json` | `/workspace/pi-defense-exp/logs/training/runs/c4_ih_sft/seed_123/error.txt` |
| c4_ih_sft | C4 | sft | 2026 | `/workspace/pi-defense-exp/logs/training/runs/c4_ih_sft/seed_2026` | `/workspace/pi-defense-exp/logs/training/runs/c4_ih_sft/seed_2026/run_metadata.json` | `/workspace/pi-defense-exp/logs/training/runs/c4_ih_sft/seed_2026/error.txt` |

## Configuração LoRA/QLoRA

```yaml
load_in_4bit: true
bnb_4bit_quant_type: nf4
bnb_4bit_compute_dtype: bfloat16
bnb_4bit_use_double_quant: true
lora_r: 16
lora_alpha: 32
lora_dropout: 0.05
bias: none
task_type: CAUSAL_LM
target_modules:
- q_proj
- k_proj
- v_proj
- o_proj
- gate_proj
- up_proj
- down_proj

```

## Configuração SFT

```yaml
num_train_epochs: 1
learning_rate: 0.0002
per_device_train_batch_size: 1
per_device_eval_batch_size: 1
gradient_accumulation_steps: 8
max_seq_length: 1024
logging_steps: 10
save_strategy: epoch
eval_strategy: epoch
warmup_ratio: 0.03
lr_scheduler_type: cosine
fp16: false
bf16: true

```

## Configuração DPO

```yaml
num_train_epochs: 1
learning_rate: 5.0e-05
per_device_train_batch_size: 1
per_device_eval_batch_size: 1
gradient_accumulation_steps: 8
max_prompt_length: 1024
max_length: 1280
beta: 0.1
logging_steps: 10
save_strategy: epoch
eval_strategy: epoch
warmup_ratio: 0.03
lr_scheduler_type: cosine
fp16: false
bf16: true

```

## Checklist

| Check | Status |
| --- | --- |
| current_python_matches_expected | True |
| dataset_manifest_exists | True |
| training_plan_exists | True |
| all_training_files_exist | True |
| all_evaluation_files_exist | True |
| adapter_dirs_exist | True |
| experiment_seeds_defined | True |
| scenario_ids_match_training_notebook | True |
| total_adapter_runs_expected | True |

## Observações e limitações

- Os cenários de treinamento são aproximações controladas de StruQ, SecAlign e Instruction Hierarchy.
- C2 e C4 usam SFT.
- C3 usa DPO.
- C0 e C1 não treinam adaptadores.
- Todos os cenários devem partir do mesmo modelo base.
- Todos os cenários devem ser avaliados nos mesmos arquivos comuns de avaliação.
- `c2_struq_sft`, `c3_secalign_dpo` e `c4_ih_sft` devem ser treinados uma vez para cada seed experimental.
- Os logs de treinamento devem ser incrementais e separados por `scenario_id`/seed.
- A seed do dataset é fixa e separada das seeds das réplicas de treinamento.
- Ataques `gcg` e `gcg_adaptive` são templates GCG-like nesta versão, não sufixos adversariais otimizados.
- O ambiente RunPod com uma GPU pode exigir redução de sequência, batch, quantidade de exemplos ou tamanho do modelo.
