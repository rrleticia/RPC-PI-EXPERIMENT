# Manifesto de inferência — Notebook 05

## Identificação

- Notebook: `05_run_inference`
- Gerado em UTC: `2026-06-29T23:30:18.916455+00:00`
- Diretório raiz do projeto: `/workspace/pi-defense-exp`
- Modelo base: `meta-llama/Llama-3.1-8B-Instruct`
- Modo de execução: `full`

## Seeds

- Seed do dataset: `42`
- Seeds experimentais de adaptadores: `[42, 123, 2026]`

## Cenários executados

| Scenario | Label | Uses adapter | Prompt strategy | Seeds |
|---|---|---:|---|---|
| `c0_base` | C0 — Base model | False | `plain` | `[42]` |
| `c1_struq_format_only` | C1 — StruQ format-only | False | `struq` | `[42]` |
| `c2_struq_sft` | C2 — StruQ-like SFT | True | `struq` | `[42, 123, 2026]` |
| `c3_secalign_dpo` | C3 — SecAlign-like DPO | True | `secalign` | `[42, 123, 2026]` |
| `c4_ih_sft` | C4 — Instruction-Hierarchy-like SFT | True | `instruction_hierarchy` | `[42, 123, 2026]` |

## Arquivos comuns de avaliação

- `test_clean`: `/workspace/pi-defense-exp/data/views/evaluation/test_clean.jsonl`
- `test_attacked_seen`: `/workspace/pi-defense-exp/data/views/evaluation/test_attacked_seen.jsonl`
- `test_attacked_unseen`: `/workspace/pi-defense-exp/data/views/evaluation/test_attacked_unseen.jsonl`

## Parâmetros de geração

- `max_input_length`: `1536`
- `max_new_tokens`: `8`
- `generation_batch_size`: `4`
- `do_sample`: `False`
- `num_beams`: `1`
- `use_4bit`: `True`

## Logs

- Log global de eventos: `/workspace/pi-defense-exp/logs/inference/05_run_inference_events.jsonl`
- Resumo JSON: `/workspace/pi-defense-exp/logs/inference/05_run_inference_summary.json`
- Diretório de logs por run: `/workspace/pi-defense-exp/logs/inference/runs`

## Arquivos de resultados

| Scenario | Seed | Split | Rows | Exists | Path |
|---|---:|---|---:|---:|---|
| `c0_base` | 42 | `test_clean` | 1876 | True | `/workspace/pi-defense-exp/results/inference/full/c0_base/seed_42/test_clean.jsonl` |
| `c0_base` | 42 | `test_attacked_seen` | 9380 | True | `/workspace/pi-defense-exp/results/inference/full/c0_base/seed_42/test_attacked_seen.jsonl` |
| `c0_base` | 42 | `test_attacked_unseen` | 5628 | True | `/workspace/pi-defense-exp/results/inference/full/c0_base/seed_42/test_attacked_unseen.jsonl` |
| `c1_struq_format_only` | 42 | `test_clean` | 1876 | True | `/workspace/pi-defense-exp/results/inference/full/c1_struq_format_only/seed_42/test_clean.jsonl` |
| `c1_struq_format_only` | 42 | `test_attacked_seen` | 9380 | True | `/workspace/pi-defense-exp/results/inference/full/c1_struq_format_only/seed_42/test_attacked_seen.jsonl` |
| `c1_struq_format_only` | 42 | `test_attacked_unseen` | 5628 | True | `/workspace/pi-defense-exp/results/inference/full/c1_struq_format_only/seed_42/test_attacked_unseen.jsonl` |
| `c2_struq_sft` | 42 | `test_clean` | 1876 | True | `/workspace/pi-defense-exp/results/inference/full/c2_struq_sft/seed_42/test_clean.jsonl` |
| `c2_struq_sft` | 42 | `test_attacked_seen` | 9380 | True | `/workspace/pi-defense-exp/results/inference/full/c2_struq_sft/seed_42/test_attacked_seen.jsonl` |
| `c2_struq_sft` | 42 | `test_attacked_unseen` | 5628 | True | `/workspace/pi-defense-exp/results/inference/full/c2_struq_sft/seed_42/test_attacked_unseen.jsonl` |
| `c2_struq_sft` | 123 | `test_clean` | 1876 | True | `/workspace/pi-defense-exp/results/inference/full/c2_struq_sft/seed_123/test_clean.jsonl` |
| `c2_struq_sft` | 123 | `test_attacked_seen` | 9380 | True | `/workspace/pi-defense-exp/results/inference/full/c2_struq_sft/seed_123/test_attacked_seen.jsonl` |
| `c2_struq_sft` | 123 | `test_attacked_unseen` | 5628 | True | `/workspace/pi-defense-exp/results/inference/full/c2_struq_sft/seed_123/test_attacked_unseen.jsonl` |
| `c2_struq_sft` | 2026 | `test_clean` | 1876 | True | `/workspace/pi-defense-exp/results/inference/full/c2_struq_sft/seed_2026/test_clean.jsonl` |
| `c2_struq_sft` | 2026 | `test_attacked_seen` | 9380 | True | `/workspace/pi-defense-exp/results/inference/full/c2_struq_sft/seed_2026/test_attacked_seen.jsonl` |
| `c2_struq_sft` | 2026 | `test_attacked_unseen` | 5628 | True | `/workspace/pi-defense-exp/results/inference/full/c2_struq_sft/seed_2026/test_attacked_unseen.jsonl` |
| `c3_secalign_dpo` | 42 | `test_clean` | 1876 | True | `/workspace/pi-defense-exp/results/inference/full/c3_secalign_dpo/seed_42/test_clean.jsonl` |
| `c3_secalign_dpo` | 42 | `test_attacked_seen` | 9380 | True | `/workspace/pi-defense-exp/results/inference/full/c3_secalign_dpo/seed_42/test_attacked_seen.jsonl` |
| `c3_secalign_dpo` | 42 | `test_attacked_unseen` | 5628 | True | `/workspace/pi-defense-exp/results/inference/full/c3_secalign_dpo/seed_42/test_attacked_unseen.jsonl` |
| `c3_secalign_dpo` | 123 | `test_clean` | 1876 | True | `/workspace/pi-defense-exp/results/inference/full/c3_secalign_dpo/seed_123/test_clean.jsonl` |
| `c3_secalign_dpo` | 123 | `test_attacked_seen` | 9380 | True | `/workspace/pi-defense-exp/results/inference/full/c3_secalign_dpo/seed_123/test_attacked_seen.jsonl` |
| `c3_secalign_dpo` | 123 | `test_attacked_unseen` | 5628 | True | `/workspace/pi-defense-exp/results/inference/full/c3_secalign_dpo/seed_123/test_attacked_unseen.jsonl` |
| `c3_secalign_dpo` | 2026 | `test_clean` | 1876 | True | `/workspace/pi-defense-exp/results/inference/full/c3_secalign_dpo/seed_2026/test_clean.jsonl` |
| `c3_secalign_dpo` | 2026 | `test_attacked_seen` | 9380 | True | `/workspace/pi-defense-exp/results/inference/full/c3_secalign_dpo/seed_2026/test_attacked_seen.jsonl` |
| `c3_secalign_dpo` | 2026 | `test_attacked_unseen` | 5628 | True | `/workspace/pi-defense-exp/results/inference/full/c3_secalign_dpo/seed_2026/test_attacked_unseen.jsonl` |
| `c4_ih_sft` | 42 | `test_clean` | 1876 | True | `/workspace/pi-defense-exp/results/inference/full/c4_ih_sft/seed_42/test_clean.jsonl` |
| `c4_ih_sft` | 42 | `test_attacked_seen` | 9380 | True | `/workspace/pi-defense-exp/results/inference/full/c4_ih_sft/seed_42/test_attacked_seen.jsonl` |
| `c4_ih_sft` | 42 | `test_attacked_unseen` | 5628 | True | `/workspace/pi-defense-exp/results/inference/full/c4_ih_sft/seed_42/test_attacked_unseen.jsonl` |
| `c4_ih_sft` | 123 | `test_clean` | 1876 | True | `/workspace/pi-defense-exp/results/inference/full/c4_ih_sft/seed_123/test_clean.jsonl` |
| `c4_ih_sft` | 123 | `test_attacked_seen` | 9380 | True | `/workspace/pi-defense-exp/results/inference/full/c4_ih_sft/seed_123/test_attacked_seen.jsonl` |
| `c4_ih_sft` | 123 | `test_attacked_unseen` | 5628 | True | `/workspace/pi-defense-exp/results/inference/full/c4_ih_sft/seed_123/test_attacked_unseen.jsonl` |
| `c4_ih_sft` | 2026 | `test_clean` | 1876 | True | `/workspace/pi-defense-exp/results/inference/full/c4_ih_sft/seed_2026/test_clean.jsonl` |
| `c4_ih_sft` | 2026 | `test_attacked_seen` | 9380 | True | `/workspace/pi-defense-exp/results/inference/full/c4_ih_sft/seed_2026/test_attacked_seen.jsonl` |
| `c4_ih_sft` | 2026 | `test_attacked_unseen` | 5628 | True | `/workspace/pi-defense-exp/results/inference/full/c4_ih_sft/seed_2026/test_attacked_unseen.jsonl` |

## Observações

- Este notebook gera saídas de modelo, mas não calcula métricas agregadas finais.
- Os arquivos JSONL produzidos aqui serão consumidos pelo notebook de métricas.
- `model_output_raw` preserva a saída textual do modelo.
- `normalized_output` contém a tentativa de mapear a saída para um rótulo válido.
- `is_correct` e `followed_attack` são campos auxiliares por exemplo; as métricas finais serão consolidadas separadamente.
- O texto completo do prompt não é salvo por padrão.
