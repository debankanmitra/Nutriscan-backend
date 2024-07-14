from fastapi import FastAPI, UploadFile, File
import uvicorn

from Gemini import Llm_result
from textract import detect_file_text


app = FastAPI()



@app.get("/test")
async def test():
    return {"message": "Hello World"}

@app.post("/upload")
def recommnedation(image: UploadFile= File(...)):
    ingredients = detect_file_text(image)
    health_history = "Diabetes, Gluten intolerance"
    result = Llm_result(ingredients, health_history)
    return {"response": result}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)