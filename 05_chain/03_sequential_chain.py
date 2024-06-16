from langchain.chains import LLMChain, SimpleSequentialChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

chat = ChatOpenAI(
    model="gpt-4o"
)

write_article_chain = LLMChain(
    llm=chat,
    prompt=PromptTemplate(
        template="{input}에 관한 기사를 써주세요.",
        input_variables=["input"]
    ),
    verbose=True,
)

translate_chain = LLMChain(
    llm=chat,
    prompt=PromptTemplate(
        template="다음 문장을 영어로 번역해 주세요.\n{input}",
        input_variables=["input"]
    ),
    verbose=True
)

sequential_chain = SimpleSequentialChain(
    chains=[
        write_article_chain,
        translate_chain
    ],
    verbose=True
)

result = sequential_chain.run("일렉트릭 기타 선택 방법")

print(result)