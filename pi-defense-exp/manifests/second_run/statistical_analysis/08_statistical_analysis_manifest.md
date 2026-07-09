# Manifesto — Notebook 08 Statistical Analysis

## Identificação

- Notebook: `08_statistical_analysis`
- Gerado em UTC: `2026-07-09T17:50:42.653041+00:00`
- Run mode: `full`
- Diretório raiz do projeto: `/workspace/pi-defense-exp`

## Entradas

- Métricas do notebook 06: `/workspace/pi-defense-exp/results/metrics/full`
- Métricas do notebook 07: `/workspace/pi-defense-exp/results/pairwise_metrics/full`
- Manifesto do notebook 06: `/workspace/pi-defense-exp/manifests/metrics/06_compute_metrics_manifest.json`
- Manifesto do notebook 07: `/workspace/pi-defense-exp/manifests/pairwise_metrics/07_pairwise_and_injected_metrics_manifest.json`

## Métricas consolidadas

`clean_accuracy`, `utility_drop`, `robust_accuracy_seen`, `robust_accuracy_unseen`, `robust_accuracy_all_attacks`, `targeted_asr_seen`, `targeted_asr_unseen`, `targeted_asr_all_attacks`, `untargeted_asr_all_attacks`, `invalid_output_rate_all_attacks`, `pna_i_seen`, `pna_i_unseen`, `mr_seen`, `mr_unseen`, `mr_targeted_seen`, `mr_targeted_unseen`, `adjusted_win_rate_clean_vs_c0`

## Arquivos gerados

| name | path | exists | rows |
| --- | --- | --- | --- |
| unified_run_metrics_csv | /workspace/pi-defense-exp/results/statistical_analysis/full/unified_run_metrics.csv | True | 14.000000 |
| scenario_metric_summary_csv | /workspace/pi-defense-exp/results/statistical_analysis/full/scenario_metric_summary.csv | True | 85.000000 |
| scenario_compact_summary_csv | /workspace/pi-defense-exp/results/statistical_analysis/full/scenario_compact_summary.csv | True | 5.000000 |
| deltas_vs_reference_csv | /workspace/pi-defense-exp/results/statistical_analysis/full/deltas_vs_reference.csv | True | 136.000000 |
| metric_rankings_csv | /workspace/pi-defense-exp/results/statistical_analysis/full/metric_rankings.csv | True | 73.000000 |
| tradeoff_components_csv | /workspace/pi-defense-exp/results/statistical_analysis/full/tradeoff_components.csv | True | 35.000000 |
| tradeoff_score_csv | /workspace/pi-defense-exp/results/statistical_analysis/full/tradeoff_score.csv | True | 5.000000 |
| seed_stability_csv | /workspace/pi-defense-exp/results/statistical_analysis/full/seed_stability.csv | True | 85.000000 |
| discussion_table_csv | /workspace/pi-defense-exp/results/statistical_analysis/full/discussion_table.csv | True | 5.000000 |
| discussion_table_md | /workspace/pi-defense-exp/results/statistical_analysis/full/discussion_table.md | True |  |
| metric_catalog_csv | /workspace/pi-defense-exp/results/statistical_analysis/full/metric_catalog_08.csv | True | 17.000000 |

## Tabela de discussão

| scenario_id | scenario_label | clean_accuracy | clean_accuracy_n | utility_drop | utility_drop_n | robust_accuracy_all_attacks | robust_accuracy_all_attacks_n | targeted_asr_all_attacks | targeted_asr_all_attacks_n | untargeted_asr_all_attacks | untargeted_asr_all_attacks_n | invalid_output_rate_all_attacks | invalid_output_rate_all_attacks_n | mr_targeted_seen | mr_targeted_seen_n | mr_targeted_unseen | mr_targeted_unseen_n | adjusted_win_rate_clean_vs_c0 | adjusted_win_rate_clean_vs_c0_n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| c0_base | C0 — Base model | 0.7729 | 1 | 0.0000 | 1 | 0.2129 | 1 | 0.7818 | 1 | 0.7871 | 1 | 0.0001 | 1 | 0.8050 | 1 | 0.5874 | 1 |  | 0 |
| c1_struq_format_only | C1 — StruQ format-only | 0.7735 | 1 | -0.0005 | 1 | 0.2098 | 1 | 0.7852 | 1 | 0.7902 | 1 | 0.0004 | 1 | 0.5855 | 1 | 0.5737 | 1 |  | 0 |
| c2_struq_sft | C2 — StruQ-like SFT | 0.8602 ± 0.0071 | 4 | -0.0873 ± 0.0071 | 4 | 0.9833 ± 0.0019 | 4 | 0.0050 ± 0.0024 | 4 | 0.0167 ± 0.0019 | 4 | 0.0000 ± 0.0000 | 4 | 0.0000 ± 0.0000 | 4 | 0.0000 ± 0.0000 | 4 | 0.4292 ± 0.0166 | 4 |
| c3_secalign_dpo | C3 — SecAlign-like DPO | 0.7768 ± 0.0341 | 4 | -0.0039 ± 0.0341 | 4 | 0.9281 ± 0.0384 | 4 | 0.0536 ± 0.0411 | 4 | 0.0719 ± 0.0384 | 4 | 0.0037 ± 0.0048 | 4 | 0.0246 ± 0.0255 | 4 | 0.0486 ± 0.0393 | 4 | 0.4150 ± 0.0190 | 4 |
| c4_ih_sft | C4 — Instruction-Hierarchy-like SFT | 0.8439 ± 0.0085 | 4 | -0.0710 ± 0.0085 | 4 | 0.9854 ± 0.0012 | 4 | 0.0003 ± 0.0002 | 4 | 0.0146 ± 0.0012 | 4 | 0.0000 ± 0.0000 | 4 | 0.0000 ± 0.0000 | 4 | 0.0001 ± 0.0003 | 4 | 0.4317 ± 0.0123 | 4 |

## Score exploratório de trade-off

| scenario_id | scenario_label | tradeoff_score | available_components | rank |
| --- | --- | --- | --- | --- |
| c2_struq_sft | C2 — StruQ-like SFT | 0.977339 | 7 | 1.000000 |
| c4_ih_sft | C4 — Instruction-Hierarchy-like SFT | 0.973359 | 7 | 2.000000 |
| c3_secalign_dpo | C3 — SecAlign-like DPO | 0.541339 | 7 | 3.000000 |
| c1_struq_format_only | C1 — StruQ format-only | 0.198913 | 6 | 4.000000 |
| c0_base | C0 — Base model | 0.165031 | 6 | 5.000000 |

## Observações metodológicas

- Este notebook realiza consolidação estatística descritiva.
- Os intervalos de confiança são calculados a partir das seeds disponíveis e devem ser interpretados com cautela.
- O score de trade-off é exploratório e não substitui as métricas originais.
- Métricas como `pna_i` são tratadas como diagnósticas, não como ranking automático de melhor/pior defesa.
