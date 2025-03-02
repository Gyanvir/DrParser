import pytesseract
from PIL import Image
import cv2
#reduce image size before upload
img = Image.open("uploads/img.jpg")
img = img.resize((int(img.width * 0.5), int(img.height * 0.5)))  # Reduce by 50%

# Initialize EasyOCR reader
text = pytesseract.image_to_string(img)
def extract_text_from_image(image_path):
    # Read image
    img = cv2.imread(image_path)

    # Extract text
    results = text.readtext(img, detail=0)  # detail=0 gives plain text
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

    

