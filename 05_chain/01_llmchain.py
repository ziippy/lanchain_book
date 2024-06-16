from langchain import LLMChain, PromptTemplate
from langchain.chat_models import ChatOpenAI

chat = ChatOpenAI(
    model="gpt-4o"
)

prompt = PromptTemplate(
    template="{product}는 어느 회사에서 개발한 제품인가요?",
    input_variables=[
        "product"
    ]
)

chain = LLMChain(
    llm=chat,
    prompt=prompt,
    verbose=True
)

result = chain.predict(product="아이폰")

print(result)