from langchain.prompts import load_prompt

loaded_prompt = load_prompt("prompt.json")

print(loaded_prompt.format(product="아이폰"))
