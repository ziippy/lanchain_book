from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import DatetimeOutputParser
from langchain.schema import HumanMessage

output_parser = DatetimeOutputParser()

chat = ChatOpenAI(
    model="gpt-4-turbo",
)

prompt = PromptTemplate.from_template("{product}의 출시일을 알려주세요")

result = chat(
    [
        HumanMessage(content=prompt.format(product="아이폰8")),
        HumanMessage(content=output_parser.get_format_instructions()),
    ]
)

output = output_parser.parse(result.content)

print(output)
