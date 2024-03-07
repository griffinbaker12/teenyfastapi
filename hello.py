from fastapi import FastAPI, Body

app = FastAPI()


# you can change the status code in case of success
@app.get("/happy", status_code=201)
def happy():
    return ":)"


# named params are nice...
@app.post("/hi")
def greet(who: str = Body(embed=True)):
    return f"Hello {who}!"
