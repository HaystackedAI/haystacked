# app/component/lc_container.py
from .lc_agents import BasicAgent,MathToolAgent,AgentFactory
from .lc_model_provider import ModelProvider
from .lc_tools import tool1

class LCContainer:
    def __init__(self):
        model_provider = ModelProvider("gpt-5-nano")
        factory = AgentFactory(model_provider.get())

        self.basic_agent = BasicAgent(factory)
        self.math_agent = MathToolAgent(factory, tools=[tool1])

        # placeholders for future agents
        # self.rag_agent = RagAgent(...)
        # self.sql_agent = SqlAgent(...)
