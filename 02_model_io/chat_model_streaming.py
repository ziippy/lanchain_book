from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

chat = ChatOpenAI(
    model="gpt-4-turbo",
    streaming=True,
    callbacks=[
        StreamingStdOutCallbackHandler(),
    ]
)

resp = chat(
    [
        HumanMessage(content="라면 맛있게 끓이는 방법을 알려주세요.")
    ]
)

response_text = resp.content
print("=================")
print(response_text)