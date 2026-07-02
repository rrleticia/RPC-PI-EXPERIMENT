# RPC-PI-EXPERIMENT

Experimental evaluation pipeline for **prompt-injection defenses in instruction-following LLMs**.

This repository contains the full experimental workflow, a lightweight reproduction package, and exported artifacts for evaluating prevention-based defenses against prompt injection attacks.

The experiment compares prompt formatting, supervised fine-tuning, preference optimization, and instruction-hierarchy-inspired training strategies under clean and attacked evaluation settings.

---

## Repository structure

```text
RPC-PI-EXPERIMENT/
  pi-defense-exp/
    Full experimental pipeline.

  pi-defense-rpdct/
    Lightweight reproduction package using Hugging Face artifacts.

  zip-files/
    Compressed exported artifacts.

  .gitattributes
    Git LFS tracking rules for large files.

  README.md
```

---

## Hugging Face artifacts

The trained adapters and dataset artifacts are also available on Hugging Face.

### Model adapters

```text
leinha/pi-defense-adapters
```

This repository contains the LoRA/QLoRA adapters trained for the defended scenarios.

### Dataset

```text
leinha/pi-defense-experiment-dataset
```

This repository contains the experimental dataset artifacts used for prompt-injection defense evaluation.

---

## Experiment overview

The experiment evaluates five scenarios:

| Scenario | Name                           | Description                                                     |
| -------- | ------------------------------ | --------------------------------------------------------------- |
| C0       | Base model                     | Base LLM without additional defense                             |
| C1       | StruQ format-only              | Defensive formatting only, without training                     |
| C2       | StruQ-like SFT                 | Supervised fine-tuning using structured prompt format           |
| C3       | SecAlign-like DPO              | Preference optimization using `chosen` and `rejected` responses |
| C4       | Instruction-Hierarchy-like SFT | Supervised fine-tuning inspired by instruction hierarchy        |

The base model used in the full experiment is:

```text
meta-llama/Llama-3.1-8B-Instruct
```

The trained defended scenarios are stored as adapters, not as full merged model checkpoints.

---

## Main goals

This project investigates questions such as:

```text
- Do prompt-injection defenses reduce attack success?
- Do defended models preserve clean-task utility?
- Which attacks are more difficult for each defense?
- Do defenses generalize to unseen or adaptive attacks?
- How stable are the results across different training seeds?
- What qualitative failure patterns appear across scenarios?
```

---

## Full experiment pipeline

The full pipeline is located in:

```text
pi-defense-exp/
```

It is organized as a sequence of notebooks:

| Notebook                                       | Purpose                                                                    |
| ---------------------------------------------- | -------------------------------------------------------------------------- |
| `01_environment_setup.ipynb`                   | Prepare environment, dependencies, folders, and environment manifest       |
| `02_dataset_creation.ipynb`                    | Build canonical datasets, attacked examples, and training/evaluation views |
| `03_training_documentation.ipynb`              | Document training plan, seeds, files, and logging strategy                 |
| `04_run_training.ipynb`                        | Train adapters for C2, C3, and C4                                          |
| `05_run_inference.ipynb`                       | Generate model outputs for C0–C4                                           |
| `06_compute_metrics.ipynb`                     | Compute directly available metrics                                         |
| `07_pairwise_and_injected_metrics.ipynb`       | Compute injected-only metrics and judge-based Win Rate                     |
| `08_statistical_analysis.ipynb`                | Aggregate results across scenarios and seeds                               |
| `09_error_analysis.ipynb`                      | Inspect qualitative failure patterns                                       |
| `10_export_experiment_artifacts.ipynb`         | Export experiment artifacts without heavy intermediate copying             |
| `11_upload_adapters_to_huggingface.ipynb`      | Upload trained adapters to Hugging Face                                    |
| `12_upload_dataset_to_huggingface.ipynb`       | Upload dataset artifacts to Hugging Face                                   |
| `13_export_huggingface_upload_artifacts.ipynb` | Export upload-related manifests/logs                                       |

---

## Quick reproduction package

A smaller reproduction package is available in:

```text
pi-defense-rpdct/
```

This package starts from Hugging Face artifacts instead of rebuilding the full experiment.

It downloads:

```text
leinha/pi-defense-adapters
leinha/pi-defense-experiment-dataset
```

Then it runs a small evaluation sample and computes a compact set of metrics.

Expected structure:

```text
pi-defense-rpdct/
  README.md
  requirements-rpdct.txt

  notebook/
    01_reproduce_from_huggingface.ipynb
    02_export_reproduction_artifacts.ipynb

  data/
  results/
  logs/
  manifests/
```

The reproduction package is useful for checking that:

```text
- the Hugging Face dataset can be downloaded;
- the adapters can be downloaded;
- the base model can load;
- the adapters can be applied;
- small evaluation views can run;
- core metrics can be recomputed quickly.
```

---

## Environment setup for the full experiment

The full experiment was designed for a Linux GPU environment, such as RunPod.

Expected root:

```text
/workspace/pi-defense-exp
```

Create the environment:

```bash
cd /workspace/pi-defense-exp

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -r requirements-data.txt
```

Register the Jupyter kernel:

```bash
python -m ipykernel install \
  --user \
  --name pi-defense-exp \
  --display-name "Python (pi-defense-exp)"
```

Training dependencies can be installed with:

```bash
python -m pip install -r requirements-train.txt
```

In GPU environments, be careful when reinstalling `torch`, because the base image may already include a CUDA-compatible PyTorch build.

---

## Environment setup for quick reproduction

The reproduction package has its own environment.

Expected root:

```text
/workspace/pi-defense-rpdct
```

Create the environment:

```bash
cd /workspace/pi-defense-rpdct

python3 -m venv --system-site-packages .venv
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -r requirements-rpdct.txt
```

Register the Jupyter kernel:

```bash
python -m ipykernel install \
  --user \
  --name pi-defense-rpdct \
  --display-name "Python (pi-defense-rpdct)"
```

Use this kernel for the notebooks inside:

```text
pi-defense-rpdct/notebook/
```

---

## Hugging Face authentication

The base model is gated:

```text
meta-llama/Llama-3.1-8B-Instruct
```

Before running training, inference, or reproduction, authenticate with Hugging Face:

```bash
huggingface-cli login
```

Or set:

```bash
export HF_TOKEN="your_huggingface_token"
```

The token must belong to an account that has access to the Llama 3.1 model.

Do not commit tokens or credentials to GitHub.

---

## Dataset

The experiment uses classification tasks from multiple sources, normalized into a common schema.

Tasks include:

| Task       | Type                                 |
| ---------- | ------------------------------------ |
| `mrpc`     | Paraphrase detection                 |
| `rte`      | Textual entailment                   |
| `cola`     | Grammatical acceptability            |
| `qqp`      | Duplicate question detection         |
| `sst2`     | Sentiment classification             |
| `sms_spam` | SMS spam classification              |
| `hsol`     | Hate/offensive speech classification |

The canonical examples include fields such as:

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

## Prompt-injection attacks

The experiment includes seen and unseen/adaptive attacks.

Seen attacks:

```text
naive
ignore
escape
fake_comp
combine
```

Unseen/adaptive attacks:

```text
combine_adaptive
gcg
gcg_adaptive
```

In this version, `gcg` and `gcg_adaptive` are represented as GCG-like templates, not fully optimized adversarial suffixes.

---

## Metrics

The project computes metrics for clean utility, robustness under attack, attack success, injected-only behavior, and pairwise response quality.

Directly computed metrics include:

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

Injected-only and pairwise metrics include:

```text
PNA-I
MR
MR targeted
Win Rate
Adjusted Win Rate
```

Win Rate is computed with an open-source judge model:

```text
Qwen/Qwen3-8B
```

The judge compares C0 against a defended scenario and returns:

```text
A
B
TIE
```

where:

```text
A   = C0 response is better
B   = defended scenario response is better
TIE = both responses are comparable
```

---

## Outputs and artifacts

The full experiment produces artifacts under:

```text
pi-defense-exp/results/
pi-defense-exp/logs/
pi-defense-exp/manifests/
pi-defense-exp/exports/
```

The reproduction package produces artifacts under:

```text
pi-defense-rpdct/results/
pi-defense-rpdct/logs/
pi-defense-rpdct/manifests/
pi-defense-rpdct/exports/
```

Compressed exports are stored in:

```text
zip-files/
```

or, in the original RunPod layout:

```text
/workspace/zip_files/
```

---

## Git LFS and large files

Some experiment outputs can be large. This repository uses Git LFS tracking rules through `.gitattributes`.

Before cloning or pulling large artifacts, install Git LFS:

```bash
git lfs install
```

Large files that should generally not be committed directly include:

```text
.venv/
data/cache/
model caches
raw Hugging Face cache
large intermediate checkpoints
temporary files
```

Adapter weights and large exports should be handled intentionally through Git LFS, Hugging Face, or external artifact storage.

---

## What is not stored here

The repository should not contain:

```text
Hugging Face tokens
private credentials
full base model weights
unnecessary cache folders
virtual environments
temporary notebook checkpoints
```

The trained adapters are available through Hugging Face:

```text
leinha/pi-defense-adapters
```

The dataset artifacts are available through Hugging Face:

```text
leinha/pi-defense-experiment-dataset
```

---

## Safe inspection note

Some datasets, especially `hsol`, may contain offensive language.

For this reason, several notebooks include safe inspection steps that prefer metadata-only views or avoid printing raw sensitive text unnecessarily.

When sharing results publicly, avoid exposing harmful or offensive examples unless strictly necessary for analysis.

---

## Recommended execution order

For the full experiment:

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
11_upload_adapters_to_huggingface.ipynb
12_upload_dataset_to_huggingface.ipynb
13_export_huggingface_upload_artifacts.ipynb
```

For quick reproduction:

```text
pi-defense-rpdct/notebook/01_reproduce_from_huggingface.ipynb
pi-defense-rpdct/notebook/02_export_reproduction_artifacts.ipynb
```

---

## Limitations

Important limitations:

```text
- GCG attacks are approximated with GCG-like templates.
- The benchmark focuses on classification tasks.
- Win Rate depends on an open-source judge and may introduce judge bias.
- Some Win Rate results may be estimated from stratified samples.
- AUC is not computed because the experiment does not include a calibrated continuous detector score.
- FPR and FNR are not central metrics for C0–C4 because these scenarios are prevention-based, not binary detectors.
- Statistical confidence intervals should be interpreted cautiously due to the small number of seeds.
```

---

## Future work

Possible extensions:

```text
- Add a binary detector for FPR and FNR.
- Add a detector with continuous scores for AUC.
- Use optimized adversarial suffixes instead of GCG-like templates.
- Evaluate open-ended generation tasks.
- Compare larger base models.
- Compare multiple judge models for Win Rate.
- Move stable notebook functions into reusable scripts.
- Add automated CLI execution for the full pipeline.
```

---

## License and model usage

The adapters depend on:

```text
meta-llama/Llama-3.1-8B-Instruct
```

Users must comply with the Llama 3.1 license terms and must have access to the base model to use the adapters.

The dataset is a derived experimental benchmark built from multiple upstream datasets. Users are responsible for checking and complying with the licenses and terms of the original datasets.

This project is intended for academic and experimental use.

---

## Summary

This repository contains:

```text
pi-defense-exp/     full prompt-injection defense experiment
pi-defense-rpdct/   lightweight reproduction from Hugging Face artifacts
zip-files/          exported compressed artifacts
```

It provides a complete experimental workflow for evaluating prompt-injection defenses, from dataset construction and adapter training to inference, metrics, pairwise judging, statistical analysis, qualitative error analysis, Hugging Face upload, and quick reproduction.
