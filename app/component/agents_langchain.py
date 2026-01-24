from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage


class BasicAgent:
    def __init__(self, model_name: str = "gpt-5-nano"):
        self.model = init_chat_model(model=model_name)
        self.agent = create_agent(model=self.model)

    async def invoke(self, prompt: str):
        return await self.agent.ainvoke(
            {"messages": [HumanMessage(content=prompt)]}
        )
