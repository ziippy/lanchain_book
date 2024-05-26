from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage

chat = ChatOpenAI(
    model="gpt-4o"
)

result = chat(
    [
        HumanMessage(content="계란찜을 만드는 재료를 알려주세요"),
        AIMessage(
            content="""계란찜을 만드는 재료는 다음과 같습니다.
            
            계란찜은 간단하고 맛있는 한국 요리로, 기본 재료는 다음과 같습니다:

1. 계란
2. 물 또는 육수 (멸치 육수나 다시마 육수를 사용하면 더욱 맛있습니다)
3. 소금
4. 참기름 (선택 사항)
5. 다진 파 (선택 사항)
6. 다진 당근 (선택 사항)
7. 다진 양파 (선택 사항)
8. 새우나 조개살 등 해산물 (선택 사항)

기본적인 계란찜을 만들기 위해서는 계란과 물, 소금만 있으면 충분하지만, 원하는 재료를 추가하여 더 풍부한 맛을 낼 수 있습니다."""
        ),
        HumanMessage(content="위 대답을 영어로 번역하세요")
    ]
)
print(result.content)