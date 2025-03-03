from fastapi import FastAPI, File, UploadFile
from pdf2image import convert_from_path
import easyocr
import shutil
import os
from PIL import Image
import io
from extract_parameters import clean_ocr_text, extract_parameters, classify_parameters
from ocr_extraction import extract_text_from_image  # Import our functions
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
reader = easyocr.Reader(["en"])  # Initialize EasyOCR with English language

def process_image(image_path):
    """Extract text from an image using EasyOCR"""
    result = reader.readtext(image_path, detail=0)
    return " ".join(result)

def process_pdf(pdf_path):
    """Convert PDF pages to images and extract text from them"""
    images = convert_from_path(pdf_path,poppler_path=r"C:\Program Files\poppler-24.08.0\Library\bin")  # Convert PDF to images
    extracted_text = []
    
    for i, image in enumerate(images):
        image_path = f"temp_page_{i}.jpg"
        image.save(image_path, "JPEG")
        text = process_image(image_path)
        extracted_text.append(text)
        os.remove(image_path)  # Clean up temp image files
    
    return " ".join(extracted_text)


UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)  # Create uploads folder if not exists

@app.post("/upload/")
async def upload_blood_report(file: UploadFile = File(...)):
    # file_path = f"uploads/{file.filename}"
    file_ext = file.filename.split(".")[-1].lower()
    temp_path = f"temp_upload.{file_ext}"
    
    with open(temp_path, "wb") as f:
        f.write(file.file.read())

    if file_ext in ["png", "jpg", "jpeg"]:
        extracted_text = process_image(temp_path)
    elif file_ext == "pdf":
        extracted_text = process_pdf(temp_path)
    else:
        return {"error": "Unsupported file format. Use JPG, PNG, or PDF."}
    
    os.remove(temp_path)  # Cleanup
    print("Raw OCR Text:\n", extracted_text)  # Debugging print
    print("🔍 Cleaned OCR Text:\n", extracted_text)  
    
    # dynamic parameter extraction
    extracted_data = extract_parameters(extracted_text)
    print("Extracted Data Before Classification:", extracted_data)  # Debugging print
    classified_data = classify_parameters(extracted_data)

    

    return {"extracted_data": extracted_text, "classified_data": classified_data}

