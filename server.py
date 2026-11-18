# server.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from orchestrator import AgentOrchestrator
import custom_tools  # registers tools

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GoalRequest(BaseModel):
    goal: str

@app.post("/run-agent")
def run_agent(request: GoalRequest):
    agent = AgentOrchestrator(system_prompt="You are an autonomous automation assistant.")
    result = agent.run(user_goal=request.goal)
    return {"output": result}
