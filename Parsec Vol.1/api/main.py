from fastapi import FastAPI, File, UploadFile, Request
from pdf2image import convert_from_path
import easyocr
import shutil
import os
from PIL import Image
import io
from extract_parameters import clean_ocr_text, extract_parameters, classify_parameters
from ocr_extraction import extract_text_from_image  # Import our functions
from fastapi.middleware.cors import CORSMiddleware
from google import genai
from markdown import markdown
import re
from fastapi.responses import JSONResponse
# from fastapi.templating import Jinja2Templates
# import uvicorn

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
reader = easyocr.Reader(["en"])  # Initialize EasyOCR with English language
# templates = Jinja2Templates(directory="templates")

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


def markdown_to_html_table(markdown_table):
    """Convert Markdown table to a proper HTML table."""
    rows = markdown_table.strip().split("\n")

    if not rows or len(rows) < 3:
        return "<p>No valid table data</p>"

    # Extract header and data rows
    header = rows[0].split("|")[1:-1]  # Remove empty first and last elements
    data_rows = [row.split("|")[1:-1] for row in rows[2:]]

    # Build HTML table
    table_html = "<table class='border-collapse border border-gray-500 w-full'>"
    table_html += "<thead><tr>" + "".join(f"<th class='border border-gray-500 p-2'>{col.strip()}</th>" for col in header) + "</tr></thead>"
    table_html += "<tbody>"
    for row in data_rows:
        table_html += "<tr>" + "".join(f"<td class='border border-gray-500 p-2'>{col.strip()}</td>" for col in row) + "</tr>"
    table_html += "</tbody></table>"

    return table_html
def process_markdown_table(markdown_table):
    """Convert Markdown table to structured JSON for React frontend."""
    rows = markdown_table.strip().split("\n")
    if len(rows) < 3:
        return {"headers": [], "rows": []}

    headers = [col.strip() for col in rows[0].split("|")[1:-1]]
    data_rows = [[col.strip() for col in row.split("|")[1:-1]] for row in rows[2:]]

    return {"headers": headers, "rows": data_rows}



UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)  # Create uploads folder if not exists


# @app.get("/")
# def index(request: Request):
#     return templates.TemplateResponse(
#         name="index.html",
#         context={"request": request}
#     )

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
        
    Category = list(classified_data.keys())
    table_txt = ""
    for i in classified_data[Category[0]]:
        client = genai.Client(api_key="AIzaSyBpJg5IAB6iykrpg8di15wJ6tL8Bumvhtc")
        # response1 = client.models.generate_content(
        #     model="gemini-2.0-flash", contents=f"List the diseases happen and causes if {i[0]} is {i[2]} in 10-20 words."
        # )
        response1 = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=f"List the diseases happen and causes if {i[0]} is {i[2]} in 10-20 words."
        )
        table_txt += response1.candidates[0].content.parts[0].text

    client = genai.Client(api_key="AIzaSyBpJg5IAB6iykrpg8di15wJ6tL8Bumvhtc")
    response2 = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"List {table_txt} in a table with test name, low/high, disease, causes as columns. Give only table No other text."
    )
    final_table=response2.candidates[0].content.parts[0].text
    # Convert Markdown table to HTML
    # final_table_html = markdown_to_html_table(final_table)
    table_data=process_markdown_table(final_table)
    response_data = {
        'extracted_data': extracted_text,
    'classified_data': classified_data,
    'final_table_headers': table_data["headers"],
    'final_table_rows': table_data["rows"],
    }
    print("Backend Response:", response_data)  # Debugging log
    return JSONResponse(content=response_data)  # Ensure JSON response
if __name__ == '__main__':
    app.run(debug=True)
    