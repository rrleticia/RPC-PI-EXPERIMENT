---
license: other
language:
- en
task_categories:
- text-classification
tags:
- prompt-injection
- llm-safety
- adversarial-evaluation
- instruction-following
- text-classification
size_categories:
- 10K<n<100K
pretty_name: Prompt Injection Defense Experiment Dataset
configs:
- config_name: canonical
  data_files:
  - split: train_clean
    path: data/canonical/train_clean.jsonl
  - split: validation_clean
    path: data/canonical/validation_clean.jsonl
  - split: test_clean
    path: data/canonical/test_clean.jsonl
  - split: train_attacked_seen
    path: data/canonical/train_attacked_seen.jsonl
  - split: validation_attacked_seen
    path: data/canonical/validation_attacked_seen.jsonl
  - split: test_attacked_seen
    path: data/canonical/test_attacked_seen.jsonl
  - split: test_attacked_unseen
    path: data/canonical/test_attacked_unseen.jsonl
- config_name: evaluation
  data_files:
  - split: test_clean
    path: data/views/evaluation/test_clean.jsonl
  - split: test_attacked_seen
    path: data/views/evaluation/test_attacked_seen.jsonl
  - split: test_attacked_unseen
    path: data/views/evaluation/test_attacked_unseen.jsonl
- config_name: struq
  data_files:
  - split: train
    path: data/views/struq/train_sft.jsonl
  - split: validation
    path: data/views/struq/validation_sft.jsonl
- config_name: secalign
  data_files:
  - split: train
    path: data/views/secalign/train_dpo.jsonl
  - split: validation
    path: data/views/secalign/validation_dpo.jsonl
- config_name: ih
  data_files:
  - split: train
    path: data/views/ih/train_sft.jsonl
  - split: validation
    path: data/views/ih/validation_sft.jsonl
---

# Prompt Injection Defense Experiment Dataset

This dataset contains the processed data used in an experimental evaluation of prompt-injection defenses for instruction-following language models.

The dataset is organized around classification tasks, clean examples, attacked examples, and scenario-specific training/evaluation views.

## Intended Use

This dataset is intended for academic and experimental evaluation of prompt-injection defenses. It can be used to reproduce the data stage of the experiment and to train/evaluate defense scenarios such as:

- StruQ-like supervised fine-tuning
- SecAlign-like DPO preference optimization
- Instruction-Hierarchy-like supervised fine-tuning

## Content Warning

This dataset may contain offensive or sensitive text because it includes examples derived from hate/offensive language classification data. It also contains synthetic prompt-injection templates inserted into untrusted data fields.

The dataset should be used only for research, evaluation, and defensive analysis.

## Loading

Because the repository contains files with different purposes and schemas, the dataset card declares separate Hugging Face configurations.

```python
from datasets import load_dataset

canonical = load_dataset("leinha/pi-defense-experiment-dataset", name="canonical")
evaluation = load_dataset("leinha/pi-defense-experiment-dataset", name="evaluation")
struq = load_dataset("leinha/pi-defense-experiment-dataset", name="struq")
secalign = load_dataset("leinha/pi-defense-experiment-dataset", name="secalign")
ih = load_dataset("leinha/pi-defense-experiment-dataset", name="ih")
```

## Tasks

| Task | Description |
|---|---|
| `mrpc` | Paraphrase classification |
| `rte` | Textual entailment classification |
| `cola` | Grammatical acceptability classification |
| `qqp` | Duplicate question classification |
| `sst2` | Sentiment classification |
| `sms_spam` | SMS spam classification |
| `hsol` | Hate/offensive/neutral classification |

## Dataset Structure

```text
data/canonical/
data/views/
```

### Canonical files

```text
data/canonical/train_clean.jsonl
data/canonical/validation_clean.jsonl
data/canonical/test_clean.jsonl
data/canonical/train_attacked_seen.jsonl
data/canonical/validation_attacked_seen.jsonl
data/canonical/test_attacked_seen.jsonl
data/canonical/test_attacked_unseen.jsonl
```

### Training and evaluation views

```text
data/views/struq/train_sft.jsonl
data/views/struq/validation_sft.jsonl

data/views/secalign/train_dpo.jsonl
data/views/secalign/validation_dpo.jsonl

data/views/ih/train_sft.jsonl
data/views/ih/validation_sft.jsonl

data/views/evaluation/test_clean.jsonl
data/views/evaluation/test_attacked_seen.jsonl
data/views/evaluation/test_attacked_unseen.jsonl
```

## Attacks

Seen attacks used in training/validation:

```text
naive
ignore
escape
fake_comp
combine
```

Unseen/adaptive attacks used in testing:

```text
combine_adaptive
gcg
gcg_adaptive
```

In this version, `gcg` and `gcg_adaptive` are represented as GCG-like templates, not optimized adversarial suffixes.

## Splits and Counts

| File | Rows |
|---|---:|
| `train_clean.jsonl` | 2,100 |
| `validation_clean.jsonl` | 350 |
| `test_clean.jsonl` | 1,876 |
| `train_attacked_seen.jsonl` | 2,100 |
| `validation_attacked_seen.jsonl` | 350 |
| `test_attacked_seen.jsonl` | 9,380 |
| `test_attacked_unseen.jsonl` | 5,628 |

## Canonical and Evaluation Schema

The canonical and evaluation files are normalized before upload with this schema:

```json
{
  "id": "string",
  "source_split": "string",
  "source_index": "int64",
  "base_id": "string",
  "task_name": "string",
  "task_family": "string",
  "split": "string",
  "trusted_instruction": "string",
  "clean_input": "string",
  "untrusted_data": "string",
  "expected_answer": "string",
  "attack_target": "string",
  "attack_type": "string",
  "seen_in_training": "bool",
  "label_space": ["string"]
}
```

For clean examples, attack-specific fields are kept with neutral values such as `attack_type="clean"` and `seen_in_training=false`. This keeps the Hugging Face Dataset Viewer from failing with schema mismatches between clean and attacked files.

## Limitations

- The GCG attacks are GCG-like templates, not fully optimized adversarial suffixes.
- The dataset focuses on classification tasks and may not generalize to open-ended generation tasks.
- The dataset is designed for defensive prompt-injection evaluation, not for deploying attacks.
- Some source datasets may have their own license and usage constraints; users should review original dataset licenses before redistribution or public release.

## Generated by

This dataset card was generated by `12_upload_dataset_to_huggingface.ipynb`.

Upload mode:

```text
JSONL files are prepared in exports/huggingface_dataset_prepared/ before upload so that each Hugging Face configuration has a consistent schema. Original files under data/ are not modified.
```
