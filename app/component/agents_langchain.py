from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage

model = init_chat_model(model="gpt-5-nano")

agent_basic = create_agent(model=model)



response = agent_basic.invoke(
    {"messages": [HumanMessage(content="What's the capital of the Moon?")]}
)

