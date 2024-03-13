
# This code is to check the model path and name at huggingface
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/quantized-gemma-2b-it")
prompt = """<s>[INST] Hello world! [/INST]"""
response = generate(model, tokenizer, prompt=prompt)

print(response)