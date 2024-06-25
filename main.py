from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from pydantic import BaseModel
from typing import Dict, Tuple
import re
import fitz
import json

app = FastAPI()

class PatternRequest(BaseModel):
    patterns: Dict[str, Tuple[str, str]]

@app.post("/process/pdf/regex")
async def upload_pdf(file: UploadFile = File(...), patterns: str = Form(...)):
    try:
        content = await file.read()
        pdf_document = fitz.open(stream=content, filetype="pdf")
        text = ""
        
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            text += page.get_text()

        pattern_dict = json.loads(patterns) 
        matches = {}
        for key, (pattern, unit) in pattern_dict["patterns"].items():
            matches[key] = re.findall(pattern, text)

        return {"matches": matches}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"An error occurred: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    import logging
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting server...")
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )



