import httpx
import os

OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://host.docker.internal:11434"
)
OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "llama3.1:8b"
)


async def run_agent(user_message: str) -> str:
    prompt = f"""
You are a Mutual Fund AI Assistant.

Answer the user's question clearly and professionally.

User:
{user_message}
"""

    async with httpx.AsyncClient(timeout=120) as client:
        response = await client.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False
            }
        )

        response.raise_for_status()
        data = response.json()

        return data.get("response", "No response generated.")