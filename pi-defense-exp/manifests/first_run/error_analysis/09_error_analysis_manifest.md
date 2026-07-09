# Manifesto — Notebook 09: Análise qualitativa de erros

## Identificação

- Notebook: `09_error_analysis`
- Gerado em UTC: `2026-06-30T14:51:27.024326+00:00`
- Diretório raiz: `/workspace/pi-defense-exp`
- Modo analisado: `full`

## Entradas principais

- Diretório de inferência: `/workspace/pi-defense-exp/results/inference/full`
- Diretório de métricas: `/workspace/pi-defense-exp/results/metrics/full`
- Diretório de métricas pareadas/injected-only: `/workspace/pi-defense-exp/results/pairwise_metrics/full`
- Diretório de análise estatística: `/workspace/pi-defense-exp/results/statistical_analysis/full`

## Quantidades carregadas

- Arquivos de inferência carregados: `34`
- Linhas de inferência carregadas: `195104`
- Linhas pareadas contra C0: `168840`
- Linhas de outputs inválidos: `274`

## Estratégia de inspeção segura

Tasks excluídas da visualização completa automática:

`hsol`

Colunas sensíveis omitidas das amostras seguras:

`clean_input`, `model_output_raw`, `prompt_text`, `reference_model_output_raw`, `untrusted_data`

## Arquivos produzidos

| name | exists | line_count | path |
| --- | --- | --- | --- |
| coverage | True | NaN | /workspace/pi-defense-exp/results/error_analysis/full/tables/inference_coverage.csv |
| failure_taxonomy | True | NaN | /workspace/pi-defense-exp/results/error_analysis/full/tables/failure_taxonomy_by_scenario_seed_split.csv |
| task_errors | True | NaN | /workspace/pi-defense-exp/results/error_analysis/full/tables/error_rates_by_task.csv |
| attack_errors | True | NaN | /workspace/pi-defense-exp/results/error_analysis/full/tables/error_rates_by_attack_type.csv |
| paired_summary_vs_c0 | True | NaN | /workspace/pi-defense-exp/results/error_analysis/full/tables/paired_summary_vs_c0.csv |
| samples_summary | True | NaN | /workspace/pi-defense-exp/results/error_analysis/full/tables/samples_summary.csv |
| invalid_outputs_summary | True | NaN | /workspace/pi-defense-exp/results/error_analysis/full/tables/invalid_outputs_summary.csv |
| seen_vs_unseen | True | NaN | /workspace/pi-defense-exp/results/error_analysis/full/tables/seen_vs_unseen_error_patterns.csv |
| seen_vs_unseen_pivot | True | NaN | /workspace/pi-defense-exp/results/error_analysis/full/tables/seen_vs_unseen_pivot.csv |
| shared_failures | True | NaN | /workspace/pi-defense-exp/results/error_analysis/full/tables/shared_failures_by_example.csv |
| shared_failure_summary | True | NaN | /workspace/pi-defense-exp/results/error_analysis/full/tables/shared_failure_summary.csv |
| discussion_top_attack_following | True | NaN | /workspace/pi-defense-exp/results/error_analysis/full/tables/discussion_top_attack_following.csv |
| discussion_top_task_errors | True | NaN | /workspace/pi-defense-exp/results/error_analysis/full/tables/discussion_top_task_errors.csv |
| discussion_paired_vs_c0 | True | NaN | /workspace/pi-defense-exp/results/error_analysis/full/tables/discussion_paired_vs_c0.csv |
| summary_log | True | NaN | /workspace/pi-defense-exp/logs/error_analysis/09_error_analysis_summary.json |
| events_log | True | 13.000000 | /workspace/pi-defense-exp/logs/error_analysis/09_error_analysis_events.jsonl |
| robust_wins_vs_c0_full | True | 600.000000 | /workspace/pi-defense-exp/results/error_analysis/full/samples/robust_wins_vs_c0.jsonl |
| robust_wins_vs_c0_safe | True | 600.000000 | /workspace/pi-defense-exp/results/error_analysis/full/safe_samples/robust_wins_vs_c0_safe.jsonl |
| attack_following_reductions_vs_c0_full | True | 600.000000 | /workspace/pi-defense-exp/results/error_analysis/full/samples/attack_following_reductions_vs_c0.jsonl |
| attack_following_reductions_vs_c0_safe | True | 600.000000 | /workspace/pi-defense-exp/results/error_analysis/full/safe_samples/attack_following_reductions_vs_c0_safe.jsonl |
| clean_regressions_vs_c0_full | True | 300.000000 | /workspace/pi-defense-exp/results/error_analysis/full/samples/clean_regressions_vs_c0.jsonl |
| clean_regressions_vs_c0_safe | True | 300.000000 | /workspace/pi-defense-exp/results/error_analysis/full/safe_samples/clean_regressions_vs_c0_safe.jsonl |
| clean_improvements_vs_c0_full | True | 300.000000 | /workspace/pi-defense-exp/results/error_analysis/full/samples/clean_improvements_vs_c0.jsonl |
| clean_improvements_vs_c0_safe | True | 300.000000 | /workspace/pi-defense-exp/results/error_analysis/full/safe_samples/clean_improvements_vs_c0_safe.jsonl |

## Observações

- Este notebook faz análise qualitativa sobre outputs já gerados.
- Nenhum treinamento ou julgamento por LLM é executado aqui.
- A análise pareada contra C0 depende da preservação de identificadores nos arquivos de inferência.
- A análise de falhas compartilhadas agrega seeds por cenário e deve ser interpretada como apoio qualitativo.
- As amostras completas são salvas localmente para auditoria, mas o notebook prioriza visualizações seguras.