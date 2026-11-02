import os

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from litellm import acompletion

app = FastAPI(
    title="Free LLM Gateway",
    description="REST API for accessing free LLM providers",
    version="1.0.0",
)

MODEL = os.getenv("LLM_MODEL", "free-model")
LITELLM_API_BASE = os.getenv(
    "LITELLM_API_BASE",
    "http://localhost:4000",
)
LITELLM_MASTER_KEY = os.getenv("LITELLM_MASTER_KEY")


class ChatRequest(BaseModel):
    prompt: str = Field(min_length=1)
    model: str | None = None
    temperature: float = Field(default=0.7, ge=0, le=2)
    max_tokens: int = Field(default=1000, ge=1, le=8192)


class ChatResponse(BaseModel):
    answer: str
    model: str


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        response = await acompletion(
            model=request.model or MODEL,
            api_base=LITELLM_API_BASE,
            api_key=LITELLM_MASTER_KEY,
            messages=[
                {
                    "role": "user",
                    "content": request.prompt,
                }
            ],
            temperature=request.temperature,
            max_tokens=request.max_tokens,
        )

        answer = response.choices[0].message.content

        return ChatResponse(
            answer=answer or "",
            model=response.model,
        )

    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail=f"LLM provider error: {str(exc)}",
        )
