import chainlit as cl
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage

chat = ChatOpenAI(model="gpt-4o")

memory = ConversationBufferMemory(
    return_messages = True
)

@cl.on_chat_start #← 채팅이 시작될 때 실행할 함수를 정의
async def on_chat_start():
    await cl.Message(content="저는 대화의 맥락을 고려해 답변할 수 있는 채팅봇입니다. 메시지를 입력하세요!").send() #← 초기에 표시할 메시지를 보냄

@cl.on_message #← 메시지를 보낼 때 실행할 함수를 정의
async def on_message(input_message):
    print("입력된 메시지: " + input_message)
    # await cl.Message(content="안녕하세요!").send() #← 챗봇의 답변을 보냄

    memory_message_result = memory.load_memory_variables({})    # 메모리 내용을 로드

    messages = memory_message_result['history']     # 메모리 내용에서 메시지만 얻음
    print("history => ")
    print(messages)

    messages.append(HumanMessage(content=input_message))

    result = chat(
        messages
    )

    memory.save_context(
        {
            "input": input_message,
        },
        {
            "output": result.content,
        }
    )
    await cl.Message(content=result.content).send()  # ← 챗봇의 답변을 보냄


# 실행은
# chainlit run chat.py
# 이런식으로 해야 한다.