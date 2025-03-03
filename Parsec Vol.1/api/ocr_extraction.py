import easyocr
import cv2

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])  # 'en' for English

def extract_text_from_image(image_path):
    # Read image
    img = cv2.imread(image_path)

    # Extract text
    results = reader.readtext(img, detail=0)  # detail=0 gives plain text
    extracted_text = "\n".join(results)

    return extracted_text

if __name__ == "__main__":
    image_path = "img.jpg"  # Change this to your image path
    text = extract_text_from_image(image_path)
    text = extract_text_from_image(image_path)
    with open("ocr_text.txt", "w") as f:
        f.write(text)
    print("Extracted text saved to ocr_text.txt")
    print("Extracted Text:\n", text)

    

