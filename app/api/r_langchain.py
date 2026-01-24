from fastapi import APIRouter
from app.component.agents_langchain import BasicAgent
from app.db.repo.repo_wage_embedding import WageEmbeddingRepository

lcRou = APIRouter()

agent = BasicAgent()  # singleton (recommended)


@lcRou.post("/agent_simple", summary="Wage Agent 1.1")
async def agent_simple():

    response = await agent.invoke(
        f"What's the capital of the Moon?"
    )

    return {
        "agent_response": response,
    }
