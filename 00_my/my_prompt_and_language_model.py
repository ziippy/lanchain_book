from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
# from langchain_core.prompts import PromptTemplate
# from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

chat = ChatOpenAI(
    model="gpt-4-turbo"
)

prompt = PromptTemplate(
    template="{sentence}에 대해서 요약해줘",
    input_variables=[
        "sentence"
    ]
)

with open('my_article.txt', 'r', encoding="utf-8") as file:
    article_content = file.read()
    # print(article_content)

result = chat(
    [
        SystemMessage(content="당신은 기자입니다. 존댓말을 쓰지말고 Abstract 를 쓰듯이 500글자 이내로 작성해 주세요."),
        HumanMessage(
            content=prompt.format(sentence=article_content)
        ),
    ]
)

print(result.content)
# print(result)

# from langchain.chains import LLMChain
# from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper
# from langchain_core.prompts import PromptTemplate
# from langchain_openai import OpenAI
#
# llm = OpenAI(temperature=0.9)
# prompt = PromptTemplate(
#     input_variables=["image_desc"],
#     template="주어진 문장을 표현할 수 있는 이미지를 그려주세요.: {image_desc}",
# )
# chain = LLMChain(llm=llm, prompt=prompt.format(image_desc="인공지능 연구센터 설립"))
#
# # image_url = DallEAPIWrapper().run(chain.run(result.content))
# image_url = DallEAPIWrapper().run(chain.run("인공지능 연구센터 설립"))
#
# print(image_url)
#
# from langchain.agents import initialize_agent, load_tools
#
# tools = load_tools(["dalle-image-generator"])
# agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
# output = agent.run('"인공지능 연구센터 설립" 이라는 문장을 표현할 수 있는 이미지 그려줘')