"""Loading a model from a file."""

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model = AutoModelForSeq2SeqLM.from_pretrained("/home/coder/model/summarizeApp")
tokenizer = AutoTokenizer.from_pretrained("/home/coder/model/summarizeApp")
with open("text.txt", encoding="utf-8") as f:
    text = f.read()

input_ids = tokenizer.encode(text, return_tensors="pt")
outputs = model.generate(input_ids)
decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(decoded)
