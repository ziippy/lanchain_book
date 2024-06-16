from langchain.chains import LLMChain, LLMRequestsChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

chat = ChatOpenAI(
    model="gpt-4o"
)

prompt = PromptTemplate(
    input_variables = [
        "query",
        "requests_result"
    ],
    template="""아래 문장을 바탕으로 질문에 답해 주세요.
    문장: {requests_result}
    질문: {query}"""
)

llm_chain = LLMChain(
    llm=chat,
    prompt=prompt,
    verbose=True
)

chain = LLMRequestsChain(
    llm_chain=llm_chain,
)

result = chain({
    "query": "제주도의 날씨를 알려주세요",
    "url": "https://apis.data.go.kr/1360000/VilageFcstMsgService/getWthrSituation?serviceKey=ooM15u1T0bBgJJA7EXBZOxPoiHeX1lbjayGvT2OtK67lXaPTclhwUW1h6P56TvFvGM9LiXtyuv6xVXot3GIJQQ%3D%3D&pageNo=1&numOfRows=1&dataType=JSON&stnId=108"
})

print(result)