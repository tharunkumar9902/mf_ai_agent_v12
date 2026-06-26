# Mutual Fund AI Agent v1.2

Standalone AI agent + Streamlit frontend for Indian mutual fund analysis.

## Features
- Ask natural language mutual fund questions
- Compare two funds
- Lookup a fund and inspect metrics
- Save and view chat history
- Generate comparison reports (Markdown + PDF)

## Stack
- OpenAI Agents SDK
- FastAPI
- Streamlit
- PostgreSQL
- Redis
- MFAPI
- Docker Compose

## Endpoints
- GET /health
- POST /chat
- POST /compare
- GET /fund/{query}
- GET /history/{user_id}
- POST /report/compare

## Frontend pages
- Chat
- Compare Funds
- Fund Lookup
- History

## Run
1. Copy `.env.example` to `.env`
2. Add your OpenAI API key
3. Run:
```bash
docker-compose up --build
```

## Open
- API docs: http://localhost:8000/docs
- Frontend: http://localhost:8501
