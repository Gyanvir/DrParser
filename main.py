import easyocr
from fastapi import FastAPI, File, UploadFile
from PIL import Image
import io
import shutil
import os
from extract_parameters import clean_ocr_text, extract_parameters, classify_parameters
from ocr_extraction import extract_text_from_image  # Import our functions

# ✅ Load EasyOCR model ONCE (reduces memory load)
reader = easyocr.Reader(['en'])


app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)  # Create uploads folder if not exists

@app.post("/upload/")
async def upload_blood_report(file: UploadFile = File(...)):
    file_path = f"uploads/{file.filename}"

    # Save file
    with open(file_path, "wb") as buffer:
        #buffer.write(await file.read())
        # Read image bytes
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes))

    # # Perform OCR to extract text
    # extracted_text = extract_text_from_image(file_path)  # Ensure OCR is called
    # print("Extracted OCR Text:\n", extracted_text)  # Debugging line
    # Perform OCR using the preloaded model
    result = reader.readtext(image, detail=0)

    # Extract Parameters
    extracted_data = extract_parameters(result)
    print("Extracted Data:\n", extracted_data)  # Debugging line

    # Classify Data
    classified_data = classify_parameters(extracted_data)
    print("Classified Data:\n", classified_data)  # Debugging line

    return {"extracted_text": result, "extracted_data": extracted_data, "classified_data": classified_data}

