import os
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import HTMLResponse
import PyPDF2
from extract_parameters import extract_parameters, classify_parameters

app = FastAPI()

UPLOAD_DIR = "uploads" 
os.makedirs(UPLOAD_DIR, exist_ok=True)  # Create uploads folder if not exists

def extract_text_from_pdf(file_path):
    # Open the provided PDF
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        # Extract text from each page of the PDF
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

@app.get("/", response_class=HTMLResponse)
async def upload_form():
    return """
        <html>
            <body>
                <h2>Upload PDF and Select Option</h2>
                <form action="/upload/" method="post" enctype="multipart/form-data">
                    <label for="dropdown">Choose an option:</label>
                    <select name="dropdown" id="dropdown">
                        <option value="1">SAHARA DIAGNOSTICS</option>
                        <option value="2">Option 2</option>
                        <option value="3">Option 3</option>
                    </select><br><br>
                    <input type="file" name="file" accept=".pdf" required><br><br>
                    <input type="submit" value="Upload">
                </form>
            </body>
        </html>
    """

@app.post("/upload/")
async def upload_blood_report(file: UploadFile = File(...), dropdown: str = Form(...)):
    file_path = f"uploads/{file.filename}"

    # Save the uploaded PDF file
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Extract text from the PDF
    extracted_text = extract_text_from_pdf(file_path)

    # Return the extracted text along with the selected dropdown option
    return {
        "extracted_text": ext_text,
        "selected_option": dropdown
    }

    lab_no = dropdown
    parameters = lab_selection(lab_no, ext_text)
    
    # Extract Parameters
    extracted_data = extract_parameters(ext_text)
    print("Extracted Data:\n", extracted_data)  # Debugging line

    # Classify Data
    classified_data = classify_parameters(extracted_data)
    print("Classified Data:\n", classified_data)  # Debugging line

    return {"lab_no": dropdown, "extracted_data": extracted_data, "classified_data": classified_data}

