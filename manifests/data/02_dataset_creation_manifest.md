# Manifesto do dataset — Notebook 02

## Identificação

- Notebook: `02_dataset_creation`
- Gerado em UTC: `2026-06-29T11:34:57.189809+00:00`
- Diretório raiz do projeto: `/workspace/pi-defense-exp`
- Seed experimental: `42`

## Tasks

`mrpc`, `rte`, `cola`, `qqp`, `sst2`, `sms_spam`, `hsol`

## Splits limpos

| Split | Exemplos por task | Total esperado |
|---|---:|---:|
| Train | 300 | 2100 |
| Validation | 50 | 350 |
| Test | 268 | 1876 |

## Ataques

### Ataques vistos

`naive`, `ignore`, `escape`, `fake_comp`, `combine`

### Ataques não vistos/adaptativos

`combine_adaptive`, `gcg`, `gcg_adaptive`

## Arquivos gerados

| Name | Exists | Lines | Path |
|---|---:|---:|---|
| `train_clean` | True | 2100 | `data/canonical/train_clean.jsonl` |
| `validation_clean` | True | 350 | `data/canonical/validation_clean.jsonl` |
| `test_clean` | True | 1876 | `data/canonical/test_clean.jsonl` |
| `train_attacked_seen` | True | 2100 | `data/canonical/train_attacked_seen.jsonl` |
| `validation_attacked_seen` | True | 350 | `data/canonical/validation_attacked_seen.jsonl` |
| `test_attacked_seen` | True | 9380 | `data/canonical/test_attacked_seen.jsonl` |
| `test_attacked_unseen` | True | 5628 | `data/canonical/test_attacked_unseen.jsonl` |
| `struq_train_sft` | True | 4200 | `data/views/struq/train_sft.jsonl` |
| `struq_validation_sft` | True | 700 | `data/views/struq/validation_sft.jsonl` |
| `secalign_train_dpo` | True | 2100 | `data/views/secalign/train_dpo.jsonl` |
| `secalign_validation_dpo` | True | 350 | `data/views/secalign/validation_dpo.jsonl` |
| `ih_train_sft` | True | 4200 | `data/views/ih/train_sft.jsonl` |
| `ih_validation_sft` | True | 700 | `data/views/ih/validation_sft.jsonl` |
| `evaluation_test_clean` | True | 1876 | `data/views/evaluation/test_clean.jsonl` |
| `evaluation_test_attacked_seen` | True | 9380 | `data/views/evaluation/test_attacked_seen.jsonl` |
| `evaluation_test_attacked_unseen` | True | 5628 | `data/views/evaluation/test_attacked_unseen.jsonl` |

## Views

| View | Uso | Train | Validation |
|---|---|---|---|
| StruQ-like SFT | clean + attacked_seen | `data/views/struq/train_sft.jsonl` | `data/views/struq/validation_sft.jsonl` |
| SecAlign-like DPO | attacked_seen only | `data/views/secalign/train_dpo.jsonl` | `data/views/secalign/validation_dpo.jsonl` |
| Instruction-Hierarchy-like SFT | clean + attacked_seen | `data/views/ih/train_sft.jsonl` | `data/views/ih/validation_sft.jsonl` |

## Arquivos comuns de avaliação

- Clean: `data/views/evaluation/test_clean.jsonl`
- Attacked seen: `data/views/evaluation/test_attacked_seen.jsonl`
- Attacked unseen/adaptive: `data/views/evaluation/test_attacked_unseen.jsonl`

## Observações

- As tasks do GLUE usam `train` + `validation`, pois os rótulos do `test` oficial não estão disponíveis publicamente para todas as subtarefas selecionadas.
- `sms_spam` e `hsol` usam splits internos estratificados.
- `gcg` e `gcg_adaptive` são templates GCG-like nesta versão inicial, não sufixos adversariais otimizados.
- `hsol` pode conter linguagem ofensiva real; inspeções manuais devem priorizar metadados ou tasks menos sensíveis.
