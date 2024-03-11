
from mlx_lm import load, generate

#model_path = "[gemma model path and name at huggingface]"
model_path = "mlx-community/quantized-gemma-2b-it"
# mlx-community/quantized-gemma-2b-it | mlx-community/quantized-gemma-7b-it

prompt = """
<start_of_turn>user
Write a python function to download Mistral ai.<end_of_turn>
<start_of_turn>model
"""

print(model_path)
print("~~~~~~~~~~~")

model, tokenizer = load(model_path)
response = generate(model, tokenizer, prompt=prompt, max_tokens=1000, verbose=True)