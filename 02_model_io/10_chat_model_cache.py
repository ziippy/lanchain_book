import time
import langchain
from langchain.cache import InMemoryCache
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

langchain.llm_cache = InMemoryCache()

chat = ChatOpenAI()
start_time = time.time()
result = chat(
    [
        HumanMessage(content="안녕하세요!")
    ]
)
end_time = time.time()
print(result.content)
print(f"실행 시간 #1: {end_time - start_time}초")

start_time = time.time()
result = chat(
    [
        HumanMessage(content="안녕하세요!")
    ]
)
end_time = time.time()
print(result.content)
print(f"실행 시간 #2: {end_time - start_time}초")
