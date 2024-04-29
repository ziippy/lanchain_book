from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.schema import HumanMessage

output_parser = CommaSeparatedListOutputParser()

chat = ChatOpenAI(
    model="gpt-4-turbo"
)

result = chat(
    [
        HumanMessage(content="삼성이 개발한 대표적인 제품 3개를 알려주세요"),
        HumanMessage(content=output_parser.get_format_instructions())
    ]
)

print(result.content)

output = output_parser.parse(result.content)

for item in output:
    print("대표 상품: " + item)