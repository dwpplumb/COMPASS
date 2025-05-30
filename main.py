from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.post("/analyse")
async def analyse_input(request: Request):
    data = await request.json()
    user_input = data.get("input", "")
    # Simpler Dummy-Output (hier später Analyse einfügen!)
    result = f"COMPASS-Auswertung: {user_input}"
    return JSONResponse({"output": result})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
