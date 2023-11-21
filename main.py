from fastapi import FastAPI, File, UploadFile
import shutil
import os

# 디렉토리 이름
directory = "uploads"

# uploads 디렉토리가 존재하지 않으면 생성
if not os.path.exists(directory):
    os.makedirs(directory)

app = FastAPI()

@app.post("/uploadfile")
async def create_upload_file(file: UploadFile = File(...)):
    with open(f"uploads/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}



