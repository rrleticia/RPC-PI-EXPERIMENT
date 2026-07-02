---
base_model: meta-llama/Llama-3.1-8B-Instruct
library_name: peft
tags:
- peft
- lora
- qlora
- prompt-injection
- safety
- instruction-following
- experimental
---

# Prompt-Injection Defense Adapters

This repository contains LoRA/QLoRA adapters trained for an experimental evaluation of prompt-injection defenses.

The base model is:

```text
meta-llama/Llama-3.1-8B-Instruct
```

The base model is not included in this repository. Users must have access to the base model in order to load these adapters.

## Available adapters

The repository contains adapters for three trained scenarios:

| Scenario | Method | Seeds |
|---|---|---|
| C2 — StruQ-like SFT | Supervised fine-tuning | 42, 123, 2026 |
| C3 — SecAlign-like DPO | Preference optimization | 42, 123, 2026 |
| C4 — Instruction-Hierarchy-like SFT | Supervised fine-tuning | 42, 123, 2026 |

Repository layout:

```text
c2_struq_sft/
  seed_42/
  seed_123/
  seed_2026/

c3_secalign_dpo/
  seed_42/
  seed_123/
  seed_2026/

c4_ih_sft/
  seed_42/
  seed_123/
  seed_2026/
```

## Loading an adapter

Example:

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftModel

BASE_MODEL_ID = "meta-llama/Llama-3.1-8B-Instruct"
ADAPTER_REPO_ID = "leinha/pi-defense-adapters"
ADAPTER_SUBFOLDER = "c2_struq_sft/seed_42"

tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL_ID)

quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
)

base_model = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL_ID,
    quantization_config=quantization_config,
    device_map="auto",
)

model = PeftModel.from_pretrained(
    base_model,
    ADAPTER_REPO_ID,
    subfolder=ADAPTER_SUBFOLDER,
)
```

## Experimental context

These adapters were produced for an academic experiment comparing preventive defenses against prompt injection in classification-style tasks.

The evaluated scenarios were:

```text
C0 — base model, no defense
C1 — StruQ format-only, no training
C2 — StruQ-like SFT
C3 — SecAlign-like DPO
C4 — Instruction-Hierarchy-like SFT
```

Only C2, C3, and C4 have adapters.

## Limitations

- These adapters are experimental research artifacts.
- They were trained and evaluated on classification-style tasks.
- The adapters do not include the base model weights.
- The base model may require separate access approval.
- The training data and evaluation setup are specific to prompt-injection defense experiments.
- These adapters should not be interpreted as a general-purpose safety solution.

## Reproducibility

The experiment used three training seeds:

```text
42, 123, 2026
```

Each trained scenario has one adapter per seed.
