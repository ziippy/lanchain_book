from langchain.llms import OpenAI
# from langchain.llms import GPT4All

llm = OpenAI(
    model="gpt-3.5-turbo-instruct"
)

# llm = GPT4All()

result = llm(
    "맛있는 라면을",
    stop="."
)
print(result)



# from langchain_openai import OpenAI
#
# llm = OpenAI(
#     model="gpt-3.5-turbo-instruct"
# )