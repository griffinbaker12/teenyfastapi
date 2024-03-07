from fastapi import FastAPI
import asyncio
import uvicorn

app = FastAPI()


@app.get("/hi")
async def greet():
    await asyncio.sleep(2)
    return "Hello, world!"


if __name__ == "__main__":
    uvicorn.run("greet_async:app")
