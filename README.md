# FreeLLM

Docker service exposing endpoint for free llm access

## Testing the API

Public backend endpoint: POST <http://localhost:8000/api/chat>

Request:

```bash
curl -X POST <http://localhost:8000/api/chat> \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Explain Docker Compose in simple terms",
    "temperature": 0.7,
    "max_tokens": 1000
  }'
```

## Docs

<http://localhost:8000/docs>

## Recommended free providers

* Google Gemini
* Groq
* OpenRouter
* OpenAI

## Future improvements

* Multiple providers
* Switch between Gemini, Groq, OpenRouter
* Fallback models
* Try another provider when one fails
* Rate limiting
* Prevent excessive API usage
* Track latency and errors
* Health endpoint
* Check gateway availability
* Streaming
* Return generated tokens progressively
