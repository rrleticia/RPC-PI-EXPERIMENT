# Avaliação Experimental de Defesas contra Prompt Injection em LLMs

Este repositório contém um pipeline experimental para avaliar defesas contra **prompt injection** em modelos de linguagem. O experimento compara diferentes estratégias de defesa em cenários controlados, usando tarefas de classificação textual e ataques inseridos como dados não confiáveis.

O objetivo principal é medir como diferentes abordagens preservam a utilidade do modelo em exemplos limpos e reduzem a influência de instruções maliciosas em exemplos contaminados.

---

## 1. Visão geral do experimento

O experimento compara cinco cenários:

| Cenário | Nome                           | Descrição                                                           |
| ------- | ------------------------------ | ------------------------------------------------------------------- |
| C0      | Base model                     | Modelo base sem defesa adicional                                    |
| C1      | StruQ format-only              | Uso apenas de formatação defensiva, sem treinamento                 |
| C2      | StruQ-like SFT                 | Modelo ajustado com supervised fine-tuning em prompts estruturados  |
| C3      | SecAlign-like DPO              | Modelo alinhado com DPO usando pares `chosen`/`rejected`            |
| C4      | Instruction-Hierarchy-like SFT | Modelo ajustado com estrutura inspirada em hierarquia de instruções |

Todos os cenários usam o mesmo modelo base:

```text
meta-llama/Llama-3.1-8B-Instruct
```

Os cenários C2, C3 e C4 usam adaptadores LoRA/QLoRA treinados com diferentes objetivos. Os cenários C0 e C1 não treinam adaptadores.

---

## 2. Objetivos

Este projeto busca responder perguntas como:

- Defesas baseadas em estrutura de prompt reduzem o sucesso de ataques de prompt injection?
- Fine-tuning supervisionado melhora a robustez em relação ao modelo base?
- Alinhamento por preferência reduz a tendência do modelo de seguir a instrução injetada?
- Defesas mais robustas prejudicam a utilidade em exemplos limpos?
- O desempenho é consistente entre diferentes seeds experimentais?
- Quais ataques e tarefas são mais difíceis para cada cenário?

---

## 3. Estrutura geral do pipeline

O pipeline é organizado em notebooks numerados:

| Notebook                                 | Função                                                                                |
| ---------------------------------------- | ------------------------------------------------------------------------------------- |
| `01_environment_setup.ipynb`             | Prepara ambiente, dependências leves, estrutura de diretórios e manifesto do ambiente |
| `02_dataset_creation.ipynb`              | Cria dataset canônico, exemplos atacados e views de treino/avaliação                  |
| `03_training_documentation.ipynb`        | Documenta o plano de treinamento, seeds, arquivos e estratégia de logging             |
| `04_run_training.ipynb`                  | Treina os adaptadores C2, C3 e C4                                                     |
| `05_run_inference.ipynb`                 | Gera respostas dos cenários C0–C4 nos arquivos de avaliação                           |
| `06_compute_metrics.ipynb`               | Calcula métricas diretamente computáveis                                              |
| `07_pairwise_and_injected_metrics.ipynb` | Calcula PNA-I, MR e Win Rate com judge open-source                                    |
| `08_statistical_analysis.ipynb`          | Consolida métricas por cenário, seed e intervalo de confiança                         |
| `09_error_analysis.ipynb`                | Faz análise qualitativa de erros e casos representativos                              |
| `10_export_experiment_artifacts.ipynb`   | Exporta artefatos do experimento em um pacote `.zip`                                  |

---

## 4. Estrutura esperada do projeto

A estrutura principal esperada é:

```text
pi-defense-exp/
  configs/
    experiment.yaml
    training_plan.yaml

  data/
    canonical/
    views/
    cache/

  notebooks/
    01_environment_setup.ipynb
    02_dataset_creation.ipynb
    03_training_documentation.ipynb
    04_run_training.ipynb
    05_run_inference.ipynb
    06_compute_metrics.ipynb
    07_pairwise_and_injected_metrics.ipynb
    08_statistical_analysis.ipynb
    09_error_analysis.ipynb
    10_export_experiment_artifacts.ipynb

  adapters/
    struq/
    secalign/
    ih/

  results/
    inference/
    injected_only/
    metrics/
    pairwise_metrics/
    statistical_analysis/
    error_analysis/

  logs/
    training/
    inference/
    metrics/
    pairwise_metrics/
    statistical_analysis/
    error_analysis/

  manifests/
    environment/
    data/
    training/
    inference/
    metrics/
    pairwise_metrics/
    statistical_analysis/
    error_analysis/

  exports/
    experiment_artifacts/

  requirements-data.txt
  requirements-train.txt
  README.md
```

Algumas pastas são criadas apenas depois da execução dos notebooks correspondentes.

---

## 5. Ambiente

O projeto foi planejado para execução em ambiente Linux, especialmente em uma instância com GPU, como RunPod.

A raiz esperada do projeto é:

```text
/workspace/pi-defense-exp
```

O ambiente virtual esperado é:

```text
/workspace/pi-defense-exp/.venv
```

O kernel Jupyter esperado é:

```text
Python (pi-defense-exp)
```

O Python esperado é:

```text
/workspace/pi-defense-exp/.venv/bin/python
```

---

## 6. Instalação

### 6.1. Criar ambiente virtual

Na raiz do projeto:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

### 6.2. Instalar dependências de dados

```bash
python -m pip install -r requirements-data.txt
```

### 6.3. Registrar kernel Jupyter

```bash
python -m ipykernel install \
  --user \
  --name pi-defense-exp \
  --display-name "Python (pi-defense-exp)"
```

### 6.4. Instalar dependências de treinamento

As dependências de treinamento são instaladas no notebook `04_run_training.ipynb`, mas também podem ser instaladas manualmente:

```bash
python -m pip install -r requirements-train.txt
```

Em ambientes RunPod, recomenda-se cuidado ao reinstalar `torch`, pois a imagem base pode já conter uma versão compatível com CUDA.

---

## 7. Autenticação no Hugging Face

O modelo base usado no experimento é:

```text
meta-llama/Llama-3.1-8B-Instruct
```

Esse modelo possui acesso controlado no Hugging Face. Antes de rodar treinamento ou inferência, é necessário garantir que o ambiente esteja autenticado com uma conta que tenha acesso ao modelo.

Opção via terminal:

```bash
huggingface-cli login
```

Ou usando variável de ambiente:

```bash
export HF_TOKEN="seu_token_huggingface"
```

O token não deve ser salvo no repositório, impresso em logs ou incluído em arquivos exportados.

---

## 8. Datasets e tarefas

O experimento usa tarefas de classificação textual. As tasks consideradas são:

| Task       | Tipo                                 |
| ---------- | ------------------------------------ |
| `mrpc`     | Paraphrase detection                 |
| `rte`      | Recognizing textual entailment       |
| `cola`     | Grammatical acceptability            |
| `qqp`      | Duplicate question detection         |
| `sst2`     | Sentiment classification             |
| `sms_spam` | SMS spam classification              |
| `hsol`     | Hate/offensive speech classification |

Todos os dados são normalizados para um formato canônico comum com campos como:

```json
{
  "id": "...",
  "task_name": "...",
  "split": "...",
  "trusted_instruction": "...",
  "clean_input": "...",
  "expected_answer": "...",
  "label_space": ["..."]
}
```

---

## 9. Ataques

O experimento usa ataques vistos e não vistos/adaptativos.

Ataques vistos durante treino/validação:

```text
naive
ignore
escape
fake_comp
combine
```

Ataques não vistos/adaptativos usados no teste:

```text
combine_adaptive
gcg
gcg_adaptive
```

Nesta versão, `gcg` e `gcg_adaptive` são tratados como templates GCG-like, não como sufixos adversariais otimizados por busca.

---

## 10. Splits do dataset

Por task, a divisão limpa é:

| Split      | Exemplos por task |
| ---------- | ----------------: |
| Train      |               300 |
| Validation |                50 |
| Test       |               268 |

Como há 7 tasks, os totais limpos são:

| Split            | Total |
| ---------------- | ----: |
| Train clean      | 2.100 |
| Validation clean |   350 |
| Test clean       | 1.876 |

Os exemplos atacados de teste incluem todos os ataques:

| Arquivo                      |  Total |
| ---------------------------- | -----: |
| `test_attacked_seen.jsonl`   |  9.380 |
| `test_attacked_unseen.jsonl` |  5.628 |
| Total atacado de teste       | 15.008 |

---

## 11. Views de treinamento

O notebook `02_dataset_creation.ipynb` gera views específicas para cada estratégia.

### StruQ-like SFT

```text
data/views/struq/train_sft.jsonl
data/views/struq/validation_sft.jsonl
```

Usa exemplos limpos e atacados vistos.

### SecAlign-like DPO

```text
data/views/secalign/train_dpo.jsonl
data/views/secalign/validation_dpo.jsonl
```

Usa apenas exemplos atacados vistos, pois DPO precisa de pares:

```text
chosen = expected_answer
rejected = attack_target
```

### Instruction-Hierarchy-like SFT

```text
data/views/ih/train_sft.jsonl
data/views/ih/validation_sft.jsonl
```

Usa exemplos limpos e atacados vistos em formato com papéis de mensagem.

---

## 12. Seeds experimentais

O projeto separa seed de dataset e seeds experimentais.

A seed de dataset é:

```python
DATASET_SEED = 42
```

Ela controla criação dos splits, amostragem e geração dos ataques.

As seeds de treinamento são:

```python
EXPERIMENT_SEEDS = [42, 123, 2026]
```

C2, C3 e C4 são treinados uma vez para cada seed:

```text
C2 seed 42
C2 seed 123
C2 seed 2026

C3 seed 42
C3 seed 123
C3 seed 2026

C4 seed 42
C4 seed 123
C4 seed 2026
```

Total de treinamentos de adaptadores:

```text
3 cenários × 3 seeds = 9 runs
```

---

## 13. Treinamento

O notebook `04_run_training.ipynb` executa os treinamentos:

| Cenário | Método | Saída                            |
| ------- | ------ | -------------------------------- |
| C2      | SFT    | `adapters/struq/seed_<seed>/`    |
| C3      | DPO    | `adapters/secalign/seed_<seed>/` |
| C4      | SFT    | `adapters/ih/seed_<seed>/`       |

O treinamento usa LoRA/QLoRA para evitar fine-tuning completo do modelo base.

Os logs do treinamento ficam em:

```text
logs/training/
```

A estrutura inclui logs globais e logs por run:

```text
logs/training/04_run_training_events.jsonl
logs/training/runs/<scenario_id>/seed_<seed>/run_metadata.json
logs/training/runs/<scenario_id>/seed_<seed>/error.txt
```

---

## 14. Inferência

O notebook `05_run_inference.ipynb` gera respostas para os cenários C0–C4 nos arquivos comuns de avaliação.

Arquivos avaliados:

```text
test_clean
test_attacked_seen
test_attacked_unseen
```

Resultados são salvos em:

```text
results/inference/full/
```

Cada linha de resultado registra, entre outros campos:

```text
scenario_id
seed
eval_split
task_name
attack_type
expected_answer
attack_target
model_output_raw
normalized_output
is_correct
followed_attack
```

A inferência é determinística, com geração curta e temperatura zero.

---

## 15. Métricas diretamente computáveis

O notebook `06_compute_metrics.ipynb` calcula métricas que podem ser obtidas diretamente a partir de:

```text
expected_answer
attack_target
normalized_output
label_space
```

Métricas calculadas:

```text
Clean Accuracy
Benign Utility
PNA-T
Clean Effectiveness
Utility Drop
Task Success Rate
Utility Under Attack
Robust Accuracy
Untargeted ASR
Targeted ASR
Attack Success Rate
Injection Following Rate
Binary ASV
Valid Output Rate
Invalid Output Rate
Utility Drop Under Attack
Robust Accuracy Delta vs C0
```

Resultados são salvos em:

```text
results/metrics/full/
```

---

## 16. Métricas pairwise e injected-only

O notebook `07_pairwise_and_injected_metrics.ipynb` calcula métricas complementares.

### Injected-only

Para PNA-I e MR, o notebook cria uma avaliação injected-only. Nesse caso, a instrução injetada é avaliada isoladamente, sem a tarefa legítima original competindo com ela.

Métricas:

```text
PNA-I
MR
MR targeted
```

### Win Rate

O Win Rate é calculado por comparação pareada usando um judge open-source.

O judge configurado é:

```text
Qwen/Qwen3-8B
```

O judge compara:

```text
Resposta A = C0
Resposta B = cenário defendido
```

E retorna:

```text
A
B
TIE
```

A partir disso são calculados:

```text
win_rate
loss_rate
tie_rate
adjusted_win_rate
```

Por padrão, o Win Rate pode ser estimado por amostragem estratificada para reduzir custo computacional.

---

## 17. Análise estatística

O notebook `08_statistical_analysis.ipynb` consolida os resultados do 06 e do 07.

Ele calcula:

```text
média
desvio padrão
erro padrão
intervalo de confiança aproximado
deltas contra C0
deltas contra C1
rankings por métrica
estabilidade entre seeds
score exploratório de trade-off
```

A análise estatística deve ser interpretada com cuidado, pois o número de seeds é pequeno.

---

## 18. Análise qualitativa de erros

O notebook `09_error_analysis.ipynb` faz uma análise qualitativa dos outputs.

Ele busca padrões como:

```text
defesa acerta e C0 erra
C0 acerta e defesa erra
todos os cenários falham
saídas inválidas
ataques mais difíceis
tasks mais sensíveis
diferenças entre seen e unseen/adaptive
```

O objetivo é complementar as métricas agregadas com exemplos e interpretações qualitativas.

Por segurança, inspeções envolvendo `hsol` devem evitar expor texto bruto ofensivo desnecessariamente.

---

## 19. Exportação dos artefatos

O notebook `10_export_experiment_artifacts.ipynb` cria um pacote de exportação do experimento.

A versão atual usa uma lógica sem cópia intermediária pesada:

```text
1. Não copia results/, logs/ ou data/ para exports/
2. Cria apenas metadados leves em exports/
3. Indexa os arquivos originais
4. Cria um .zip lendo diretamente dos caminhos originais
5. Salva o .zip fora de exports/
```

Metadados leves ficam em:

```text
exports/experiment_artifacts/full/
```

O zip final fica em:

```text
/workspace/zip_files/
```

Por padrão, o notebook não exporta:

```text
.venv/
data/cache/
adapters/
pesos de modelos
cache Hugging Face
```

Para incluir adaptadores LoRA/QLoRA no zip, altere:

```python
EXPORT_MODEL_ADAPTERS = True
```

---

## 20. Ordem recomendada de execução

Execute os notebooks nesta ordem:

```text
01_environment_setup.ipynb
02_dataset_creation.ipynb
03_training_documentation.ipynb
04_run_training.ipynb
05_run_inference.ipynb
06_compute_metrics.ipynb
07_pairwise_and_injected_metrics.ipynb
08_statistical_analysis.ipynb
09_error_analysis.ipynb
10_export_experiment_artifacts.ipynb
```

Antes de rodar notebooks de treino ou inferência, confira:

```text
- kernel correto selecionado;
- Hugging Face login configurado;
- GPU disponível;
- modelo base acessível;
- manifestos anteriores gerados;
- espaço em disco suficiente.
```

---

## 21. Artefatos grandes e GitHub

Este repositório foi pensado para ser versionado no GitHub, mas alguns artefatos não devem ser commitados.

Não incluir no GitHub:

```text
.venv/
data/cache/
adapters/
outputs/
resultados muito grandes
arquivos .zip grandes
tokens ou credenciais
```

Arquivos recomendados para versionamento:

```text
notebooks/
configs/
requirements-data.txt
requirements-train.txt
README.md
.gitignore
scripts/, se existirem
manifestos leves, se desejado
```

Os resultados completos podem ser disponibilizados separadamente como release, artifact externo ou arquivo compactado.

---

## 22. Segurança e conteúdo sensível

Alguns datasets usados no experimento podem conter conteúdo ofensivo real, especialmente `hsol`.

Por isso:

- não imprimir exemplos brutos de `hsol` sem necessidade;
- preferir visualizações com metadados;
- usar amostras seguras na análise qualitativa;
- evitar incluir texto ofensivo desnecessário no relatório ou README;
- manter logs e exports auditáveis, mas sem expor conteúdo sensível quando não for necessário.

---

## 23. Limitações

Este experimento possui algumas limitações importantes:

- os ataques GCG são representados como templates GCG-like, não como sufixos otimizados;
- o experimento usa tasks de classificação, o que facilita a avaliação automática, mas limita generalização para tarefas abertas;
- Win Rate depende de um judge open-source, que pode introduzir viés;
- algumas métricas são estimadas por amostragem, não necessariamente sobre todos os exemplos;
- AUC não foi calculada porque o experimento não inclui detector com score contínuo;
- FPR e FNR não são métricas centrais dos cenários C0–C4, pois esses cenários são preventivos, não detectores binários;
- os intervalos de confiança devem ser interpretados com cautela devido ao número reduzido de seeds.

---

## 24. Possíveis trabalhos futuros

Extensões possíveis:

```text
- adicionar detector binário para calcular FPR e FNR;
- adicionar detector com score contínuo para calcular AUC;
- usar ataques GCG realmente otimizados;
- avaliar tarefas generativas abertas;
- testar modelos base maiores;
- comparar diferentes judges para Win Rate;
- avaliar robustez com ataques adaptativos mais fortes;
- transformar funções estáveis dos notebooks em scripts reutilizáveis;
- automatizar execução completa via CLI ou workflow.
```

---

## 25. Reprodutibilidade

A reprodutibilidade é apoiada por:

```text
- seeds fixas;
- manifestos por etapa;
- logs incrementais;
- arquivos JSONL intermediários;
- configuração explícita do modelo base;
- exportação consolidada dos artefatos;
- separação entre dados limpos, atacados e injected-only.
```

Cada notebook gera seus próprios registros em `logs/`, `manifests/` ou `results/`.

---

## 26. Licença e uso

Verifique as licenças dos datasets, modelos e bibliotecas usados antes de redistribuir pesos, adaptadores ou dados derivados.

Este repositório tem finalidade acadêmica e experimental.

---

## 27. Resumo rápido

```text
01 cria ambiente
02 cria dataset
03 documenta treinamento
04 treina adaptadores
05 gera respostas
06 calcula métricas diretas
07 calcula métricas pairwise/injected-only
08 consolida estatísticas
09 analisa erros
10 exporta artefatos
```

O pipeline completo permite avaliar utilidade, robustez e comportamento comparativo de diferentes defesas contra prompt injection.
