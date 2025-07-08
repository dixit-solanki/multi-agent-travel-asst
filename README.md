# 🧠 Multi-Agent Travel Assistant using AutoGen

A hands-on project exploring Agentic AI by building a **multi-agent travel assistant**.  
Given a **location** and a **budget**, the agents collaborate to generate a custom travel plan — showing how LLM-powered agents can reason, communicate, and solve real-world problems together.

---

## 📌 Use Case

Plan a **3-day trip to Rajasthan** with a budget of **₹25,000**.

---

## 🛠️ Tech Stack

- AI & Agents: `AutoGen`, `pyautogen`, GPT-4o-mini  
- Backend: `FastAPI`, `Uvicorn`  
- Frontend: `Next.js`  
- Optional UI: `AutoGen Studio`

---

## 📁 Project Structure

multi-agent-travel-asst/
├── backend/ # FastAPI backend
│ └── api.py
├── frontend/ # Next.js frontend
├── myapp/ # AutoGen Studio agent configs
│ └── agents.json
├── .env # API keys
├── requirements.txt
└── README.md


---

## 🔐 Environment Setup

1. Clone the repository:

```bash
git clone https://github.com/dixit-solanki/multi-agent-travel-asst.git
cd multi-agent-travel-asst

OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

conda create -n travel-asst python=3.10
conda activate travel-asst

pip install -r requirements.txt

pip install pyautogen autogen-agentchat openai fastapi uvicorn "autogenstudio[ui]"

 How to Start the App
 Step 1: Start AutoGen Studio UI
 autogenstudio ui --port 8080 --appdir ./myapp
 Open in browser: http://localhost:8080


 Step 2: Start FastAPI Backend
 >uvicorn backend.api:app --reload --port 8000
 Test in browser: http://localhost:8000/docs


 Step 3: Start Next.js Frontend
 cd frontend
npm install
pnpm run dev


I’m planning a 3-day trip to Rajasthan with a budget of ₹25,000.
Suggest a detailed travel plan.