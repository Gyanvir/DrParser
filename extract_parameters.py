import re

# Updated reference ranges
reference_ranges = {
    "Haemoglobin": (13.0, 17.0),  # Example range for males (g/dL)
    "Total Leucocyte Count": (4000, 11000),  # Example range (cells/µL)
}




def clean_ocr_text(ocr_text):
    """ Cleans OCR text to merge multi-line values. """
    lines = ocr_text.split("\n")
    cleaned_lines = []
    skip_next = False

    for i, line in enumerate(lines):
        if skip_next:
            skip_next = False
            continue

        line = line.strip()
        if i + 1 < len(lines) and re.match(r"^\d", lines[i + 1]):  # If next line starts with a digit, merge
            cleaned_lines.append(line + " " + lines[i + 1].strip())
            skip_next = True
        else:
            cleaned_lines.append(line)

    return "\n".join(cleaned_lines)

def extract_parameters(ocr_text):
    """ Extracts key medical parameters from cleaned OCR text. """
    parameters = {}

    patterns = {
        "Haemoglobin": r"HAEMOGLOBIN.*?\(?Hb\)?\s*([\d.]+)",  
        "Total Leucocyte Count": r"TOTAL LEUCOCYTE COUNT.*?\(?TLC\)?\s*([\d,]+)"
    }
    extracted_data = {}

    # cleaned_text = clean_ocr_text(ocr_text)  # Preprocess text before regex
    # print("Cleaned OCR Text:\n", clean_ocr_text(ocr_text))  # Debugging line
    for param, pattern in patterns.items():
        match = re.search(pattern, clean_ocr_text(ocr_text), re.IGNORECASE)
        if match:
            parameters[param] = match.group()
        else:
            print(f"No match found for {param}")  # Debugging statement
    # print("Extracted Data:", extracted_data)  # Debugging line

    return parameters
# def classify_parameters(extracted_data):
    """
    Classifies extracted blood parameters into Critical, Borderline, and Normal.
    """
    classification = {"Critical": [], "Borderline": [], "Normal": []}

    # Define normal ranges (ICMR Standards)
    normal_ranges = {
        "Haemoglobin": (13.5, 18.0),  # Adjust range for gender if needed
        "Total Leucocyte Count": (4000, 11000),
    }
    
    for param, value in extracted_data.items():
        print(f"Processing: {param} -> {value}")  # Debugging print

        if param in normal_ranges:
            lower, upper = normal_ranges[param]

            try:
                value = float(value.replace(",", "").strip())  # Clean and convert to float
                print(f"Converted Value: {param} -> {value}")  # Debugging print
            except ValueError:
                print(f"Skipping {param}, invalid number: {value}")  # Debugging print
                continue
        
        
                # Classification logic
        if value < lower or value > upper:
            classification["Critical"].append((param, value))
        elif lower * 0.9 <= value <= upper * 1.1:  # Borderline = 10% deviation
            classification["Borderline"].append((param, value))
        else:
            classification["Normal"].append((param, value))

    return classification
def classify_parameters(extracted_data):
    critical = []
    borderline = []
    normal = []

    print("🔍 Debug: Inside classify_results function")  # Debugging Step 1
    print("Extracted Data for Classification:", extracted_data)  # Debugging Step 2

    for parameter, value in extracted_data.items():
        print(f"Processing {parameter}: {value}")  # Debugging Step 3

        # Convert value to a number
        match = re.search(r"[\d,]+\.?\d*", value)  # Extract numeric value
        if match:
            numeric_value = float(match.group().replace(",", ""))  # Remove commas
            print(f"Numeric Value of {parameter}: {numeric_value}")  # Debugging Step 4

            # Define thresholds for classification
            if parameter.lower() == "haemoglobin":
                if numeric_value < 12.15 or numeric_value > 19.8:
                    critical.append((parameter, numeric_value))
                elif numeric_value >= 13.5 and numeric_value <= 18.0:
                    borderline.append((parameter, numeric_value))
                else:
                    normal.append((parameter, numeric_value))

            elif parameter.lower() == "total leucocyte count":
                if numeric_value <= 3600 or numeric_value >=12100:
                    critical.append((parameter, numeric_value))
                elif numeric_value >=4000 and numeric_value <= 11000:
                    borderline.append((parameter, numeric_value))
                else:
                    normal.append((parameter, numeric_value))

        else:
            print(f"❌ Could not extract numeric value for {parameter}")  # Debugging Step 5

    classified_data = {
        "Critical": critical,
        "Borderline": borderline,
        "Normal": normal
    }

    print("Final Classified Data:", classified_data)  # Debugging Step 6
    return classified_data

if __name__ == "__main__":
    # Load extracted text from OCR
    with open("ocr_text.txt", "r") as f:
        ocr_text = f.read()

    cleaned_text = clean_ocr_text(ocr_text)
    # print("CLEANED OCR TEXT:\n", cleaned_text)  # Debugging step

    parameters = extract_parameters(ocr_text)
    print("Extracted Parameters:", parameters)
    classified_results = classify_parameters(parameters)
    print("Classified Results:", classified_results)
   
