from fastapi import FastAPI, UploadFile, File
import uvicorn

from textract import detect_file_text


app = FastAPI()



@app.get("/test")
async def test():
    return {"message": "Hello World"}

@app.post("/upload")
def recommnedation(image: UploadFile= File(...)):
    response = detect_file_text(image)
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)