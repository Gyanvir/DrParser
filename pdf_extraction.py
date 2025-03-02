from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    # Read pdf
    reader = PdfReader(f"{pdf_path}.pdf")       # Initialize PDF reader
    all_pages = reader.pages
    extracted_txt = ""
    for page in all_pages:
        pg = page.extract_text()
        extracted_txt += "\n".join(pg)
        
    return extracted_text

if __name__ == "__main__":
    pdf_path = "pdf.pdf"  # Change this to your pdf path
    text = extract_text_from_pdf(pdf_path)
    with open("pdf_text.txt", "w") as f:
        f.write(text)
    print("Extracted text saved to pdf_text.txt")
    # print("Extracted Text:\n", text)

    

