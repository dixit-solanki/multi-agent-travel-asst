from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from backend.travel_planner import user_proxy, travel_planner_manager

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class TravelRequest(BaseModel):
    user_input: str

@app.post("/plan-trip")
def plan_trip(req: TravelRequest):
    try:
        chat_result = user_proxy.initiate_chat(
            travel_planner_manager,
            message=req.user_input,
            summary_method="last_msg",
        )

        report = next(
            msg["content"]
            for msg in chat_result.chat_history
            if msg.get("name") == "Report_Writer_Agent"
        )
        return {"report": report}

    except Exception as e:
        return {"error": str(e)}

