# app/api/lc_routes.py
from fastapi import APIRouter
from app.lc_components.lc_container import LCContainer

lcRou = APIRouter()
container = LCContainer()


@lcRou.post("/agent_basic", summary="Wage Agent 1.1")
async def agent_basic(payload: dict):
    prompt = payload["prompt"]
    return await container.basic_agent.invoke(prompt)


@lcRou.post("/agent_math", summary="Wage Agent 1.1")
async def agent_math(payload: dict):
    prompt = payload["prompt"]
    return await container.math_agent.invoke(prompt)


# @lcRou.post("/agent_rag", summary="Wage Agent 1.1")
# async def agent_rag(payload: dict):
#     prompt = payload["prompt"]
#     return await container.rag_agent.invoke(prompt)


# @lcRou.post("/agent_sql", summary="Wage Agent 1.1")
# async def agent_sql(payload: dict):
#     prompt = payload["prompt"]
#     return await container.sql_agent.invoke(prompt)
