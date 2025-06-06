from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/invoke")
async def proxy_call():
    # backend_url = "http://localhost:5137/api/invoke"
    backend_url = "http://google.com/"
    async with httpx.AsyncClient() as client:
        response = await client.get(backend_url, timeout=20.0)
    return response.status_code.