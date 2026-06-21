import os
import argparse
import inspect
import torch
import trl

from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, set_seed
from peft import LoraConfig, TaskType
from trl import DPOTrainer, DPOConfig


def filter_supported_kwargs(cls, kwargs):
    signature = inspect.signature(cls.__init__)
    valid_params = set(signature.parameters.keys())

    filtered = {}
    dropped = {}

    for key, value in kwargs.items():
        if key in valid_params:
            filtered[key] = value
        else:
            dropped[key] = value

    if dropped:
        print(f"[INFO] Argumentos ignorados por incompatibilidade com esta versão de {cls.__name__}:")
        for key in dropped:
            print(f"  - {key}")

    return filtered


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--train_file", required=True)
    parser.add_argument("--output_dir", required=True)
    parser.add_argument("--max_length", type=int, default=1024)
    parser.add_argument("--max_prompt_length", type=int, default=512)
    parser.add_argument("--epochs", type=float, default=1.0)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    set_seed(args.seed)

    print(f"[INFO] TRL version: {trl.__version__}")
    print(f"[INFO] Seed de treino: {args.seed}")

    model_id = os.environ.get("MODEL_ID", "meta-llama/Meta-Llama-3-8B-Instruct")

    print(f"[INFO] Modelo base: {model_id}")
    print(f"[INFO] Arquivo de treino: {args.train_file}")
    print(f"[INFO] Diretório de saída: {args.output_dir}")

    tokenizer = AutoTokenizer.from_pretrained(model_id)

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    tokenizer.padding_side = "right"

    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        dtype=torch.float16,
        device_map="auto",
        low_cpu_mem_usage=True,
    )

    model.gradient_checkpointing_enable()
    model.config.use_cache = False

    peft_config = LoraConfig(
        r=16,
        lora_alpha=32,
        lora_dropout=0.05,
        bias="none",
        task_type=TaskType.CAUSAL_LM,
        target_modules=[
            "q_proj", "k_proj", "v_proj", "o_proj",
            "gate_proj", "up_proj", "down_proj"
        ],
    )

    dataset = load_dataset("json", data_files=args.train_file, split="train")

    print("[INFO] Colunas do dataset:", dataset.column_names)
    print("[INFO] Exemplo 0:", dataset[0])

    dpo_config_kwargs = {
        "output_dir": args.output_dir,
        "seed": args.seed,
        "data_seed": args.seed,
        "per_device_train_batch_size": 1,
        "gradient_accumulation_steps": 8,
        "num_train_epochs": args.epochs,
        "learning_rate": 5e-5,
        "fp16": True,
        "logging_steps": 10,
        "save_strategy": "epoch",
        "save_total_limit": 2,
        "report_to": "none",
        "beta": 0.1,
        "max_length": args.max_length,
        "max_prompt_length": args.max_prompt_length,
        "gradient_checkpointing": True,
        "remove_unused_columns": False,
    }

    dpo_args = DPOConfig(
        **filter_supported_kwargs(DPOConfig, dpo_config_kwargs)
    )

    trainer_kwargs = {
        "model": model,
        "ref_model": None,
        "args": dpo_args,
        "train_dataset": dataset,
        "processing_class": tokenizer,
        "tokenizer": tokenizer,
        "peft_config": peft_config,
    }

    trainer = DPOTrainer(
        **filter_supported_kwargs(DPOTrainer, trainer_kwargs)
    )

    trainer.train()
    trainer.save_model(args.output_dir)
    tokenizer.save_pretrained(args.output_dir)

    print(f"[OK] Adapter DPO salvo em: {args.output_dir}")


if __name__ == "__main__":
    main()
