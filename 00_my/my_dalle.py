from langchain.chains import LLMChain
from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI

llm = OpenAI(temperature=0.9)

from langchain.agents import initialize_agent, load_tools

tools = load_tools(["dalle-image-generator"])
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
# output = agent.run("Create an image of a halloween night at a haunted museum")
output = agent.run("Create an image of a \"한화시스템과 고려대 공과대학은 '인간 중심 인공지능 공동연구센터(HCAI)'를 설립하여 AI 기술과 인재 개발에 협력한다. 이 연구센터는 AI 연구 및 개발, 전문가 양성 프로그램, 학술 활동 등을 진행하며, 한화시스템의 AI 연구원들이 현장에 상주할 예정이다. 초대 센터장은 김성범 교수가 맡으며, 한화시스템은 이를 통해 AI 기술 개발과 사업화를 추진하고, 고려대는 특화된 AI 인재 양성을 목표로 한다. 또한, HCAI는 다양한 기관과의 개방형 협력을 통해 네트워크를 확장할 계획이다.\"")