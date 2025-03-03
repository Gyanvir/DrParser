import re
import json

standard_names = {
    # 🔹 Common Blood Parameters
    "Haemoglobin": ["Haemoglobin", "Hb", "HAEMOGLOBIN"],
    "WBC Count": ["WBC", "Total Leucocyte Count", "TLC", "TOTAL LEUCOCYTE COUNT"],
    "RBC Count": ["RBC", "Red Blood Cell Count", "RBC COUNT"],
    "Platelets": ["Platelets", "Platelet Count", "PLATELET COUNT", "PLT"],
    "Hematocrit": ["Hematocrit", "HCT", "PCV", "PACKED CELL VOLUME"],
    
    # 🔹 New Blood Parameters
    "MCV": ["MCV", "Mean Corpuscular Volume"],
    "MCH": ["MCH", "Mean Corpuscular Hemoglobin"],
    "MCHC": ["MCHC", "Mean Corpuscular Hemoglobin Concentration"],
    "RDW": ["RDW", "Red Cell Distribution Width"],
    
    # 🔹 Kidney Function Test (KFT)
    "Blood Urea": ["Blood Urea"],
    "BUN": ["Blood Urea Nitrogen", "BUN"],
    "Serum Creatinine": ["Serum Creatinine"],
    "Serum Uric Acid": ["Serum Uric Acid"],
    "Calcium": ["Calcium"],
    "Phosphorus": ["Inorganic Phosphorus", "Phosphorus"],
    "Sodium": ["Sodium"],
    "Potassium": ["Potassium"],
    "Total Protein": ["Total Protein"],
    "Albumin": ["Albumin"],
    "Globulin": ["Globulin"],

    # 🔹 Biochemistry
    "Fasting Blood Sugar": ["Blood Sugar Fasting", "FBS"],
    "Postprandial Blood Sugar": ["Blood Sugar PP", "PPBS"],
}

patterns = {
    "Haemoglobin": r"\b(?:Haemoglobin|Hb|HAEMOGLOBIN)[^\d]+([\d.]+)",
    "WBC Count": r"\b(?:WBC Count|Total Leucocyte Count|TLC|TOTAL LEUCOCYTE COUNT)[^\d]+([\d,]+)",
    "RBC Count": r"\b(?:RBC Count|Red Blood Cell Count|RBC)[^\d]+([\d.]+)",
    "Platelets": r"\b(?:Platelets|Platelet Count|PLT)[^\d]+([\d,.]+(?:\sLakh)?)",
    "Hematocrit": r"\b(?:Hematocrit|HCT|PCV|PACKED CELL VOLUME|P.C.V)[^\d]+([\d.]+)",
    
    # 🔹 New Blood Parameters
    "MCV": r"\b(?:MCV|Mean Corpuscular Volume|M C V)[^\d]+([\d.]+)",  # Improved
    "MCH": r"\b(?:MCH|Mean Corpuscular Hemoglobin)[^\d]+([\d.]+)",
    "MCHC": r"\b(?:MCHC|Mean Corpuscular Hemoglobin Concentration)[^\d]+([\d.]+)",
    "RDW": r"\b(?:RDW|Red Cell Distribution Width)[^\d]+([\d.]+)",
    
    # 🔹 Kidney Function Test (KFT)
    "Blood Urea": r"\b(?:Blood Urea)[^\d]+([\d.]+)",
    "BUN": r"\b(?:Blood Urea Nitrogen|BUN)[^\d]+([\d.]+)",
    "Serum Creatinine": r"\b(?:Serum Creatinine)[^\d]+([\d.]+)",
    "Serum Uric Acid": r"\b(?:Serum Uric Acid)[^\d]+([\d.]+)",
    "Calcium": r"\b(?:Calcium)[^\d]+([\d.]+)",
    "Phosphorus": r"\b(?:Inorganic Phosphorus|Phosphorus)[^\d]+([\d.]+)",
    "Sodium": r"\b(?:Sodium)[^\d]+([\d.]+)",
    "Potassium": r"\b(?:Potassium)[^\d]+([\d.]+)",
    "Total Protein": r"\b(?:Total Protein)[^\d]+([\d.]+)",
    "Albumin": r"\b(?:Albumin)[^\d]+([\d.]+)",
    "Globulin": r"\b(?:Globulin)[^\d]+([\d.]+)",

    # 🔹 Biochemistry
    "Fasting Blood Sugar": r"\b(?:Blood Sugar Fasting|FBS)[^\d]+([\d.]+)",
    "Postprandial Blood Sugar": r"\b(?:Blood Sugar PP|PPBS)[^\d]+([\d.]+)",    
}




def clean_ocr_text(ocr_text):
    
    """ Fixes OCR spacing issues & normalizes extracted text """
    ocr_text = re.sub(r"\s+", " ", ocr_text)  # Convert multiple spaces/newlines to a single space

    # 🔹 Fix common OCR misreads (Expand if needed)
    corrections = {
        "RB C": "RBC",
        "PLATELET COUNT": "Platelets",
        "PCV / HAEMATOCRIT": "Hematocrit",
        "WBC SERIES": "WBC Count",
        "TOTAL LEUCOCYTE COUNT": "WBC Count",
        "TLC": "WBC Count",
        "HAEMOGLOBIN": "Haemoglobin",
        "P.C.V": "Hematocrit",
        "M C V": "MCV",
        "M C H": "MCH",
        "M C H C": "MCHC",
        "RDW FL": "RDW",

    }

    for wrong, correct in corrections.items():
        ocr_text = ocr_text.replace(wrong, correct)

    return ocr_text.strip()


def extract_parameters(ocr_text):
    """ Extracts key medical parameters from cleaned OCR text. """
      
    extracted_data = {}

    # cleaned_text = clean_ocr_text(ocr_text)  # Preprocess text before regex
    # print("Cleaned OCR Text:\n", clean_ocr_text(ocr_text))  # Debugging line
    for param, pattern in patterns.items():
        match = re.search(pattern, clean_ocr_text(ocr_text), re.IGNORECASE)
        if match:
            value = match.group(1).replace(",", "").strip()  # Remove commas and extra spaces
            if "Lakh" in value:
                value = float(value.split()[0]) * 100000  # Convert to numeric value
            else:
                value = float(value)  # Convert to float
            extracted_data[param] = float(value)  # Convert to float
            print(f"✅ Match Found: {param} -> {value}")  # Debugging print
            # parameters[param] = match.group()
        else:
            print(f"No match found for {param}")  # Debugging statement
    # print("Extracted Data:", extracted_data)  # Debugging line

    return extracted_data
def classify_parameters(extracted_data):
    """
    Classifies blood report values into Critical, Borderline, and Normal.
    """
    classification = {"Critical": [], "Borderline": [], "Normal": []}

    normal_ranges = {
        # 🩸 Hemogram (Blood Test)
        "Haemoglobin": (13.5, 18.0),  # Males: 13.5-18.0 g/dL, Females: 12.0-16.0 g/dL
        "WBC Count": (4000, 11000),
        "RBC Count": (4.7, 6.1),
        "Platelets": (150000, 450000),
        "Hematocrit": (38, 50),
        "MCV": (80, 100),  # Normal: 80-100 fL
        "MCH": (27, 33),  # Normal: 27-33 pg
        "MCHC": (32, 36),  # Normal: 32-36 g/dL
        "RDW": (11, 15),  # Normal: 11-15%

        # 🏥 Kidney Function Test (KFT)
        "Blood Urea": (7, 20),
        "BUN": (7, 22),
        "Serum Creatinine": (0.6, 1.3),
        "Serum Uric Acid": (2.4, 7.0),
        "Calcium": (8.5, 10.5),
        "Phosphorus": (2.5, 4.5),
        "Sodium": (135, 145),
        "Potassium": (3.5, 5.0),
        "Total Protein": (6.0, 8.3),
        "Albumin": (3.5, 5.0),
        "Globulin": (2.0, 3.5),

        # 🍬 Blood Sugar Test
        "Fasting Blood Sugar": (70, 100),
        "Postprandial Blood Sugar": (100, 140),

    }
    for param, value in extracted_data.items():
        if param in normal_ranges:
            lower, upper = normal_ranges[param]

            # 🔹 Ensure value is numeric
            try:
                value = float(value)
            except ValueError:
                continue  

            # 🔹 Classification Logic
            if value < lower or value > upper:
                classification["Critical"].append((param, value))
            elif lower * 0.9 <= value <= upper * 1.1:  # Borderline = ±10%
                classification["Borderline"].append((param, value))
            else:
                classification["Normal"].append((param, value))

    print("Final Classified Data:", classification)  # Debugging print
    return classification

    # print("🔍 Debug: Inside classify_results function")  # Debugging Step 1
    # print("Extracted Data for Classification:", extracted_data)  # Debugging Step 2
    # if isinstance(extracted_data, str):  
    #     extracted_data = json.loads(extracted_data)  # Convert string to dictionary
    # print("Extracted Data Type:", type(extracted_data))
    # print("Extracted Data:", extracted_data)

    # for parameter, value in extracted_data.items():
    #     print(f"Processing {parameter}: {value}")  # Debugging Step 3

    #     # Convert value to a number
    #     match = re.search(r"[\d,]+\.?\d*", value)  # Extract numeric value
    #     if match:
    #         numeric_value = float(match.group().replace(",", ""))  # Remove commas
    #         print(f"Numeric Value of {parameter}: {numeric_value}")  # Debugging Step 4

    #         # Define thresholds for classification
    #         if parameter.lower() == "haemoglobin":
    #             if numeric_value < 12.15 or numeric_value > 19.8:
    #                 critical.append((parameter, numeric_value))
    #             elif numeric_value >= 13.5 and numeric_value <= 18.0:
    #                 borderline.append((parameter, numeric_value))
    #             else:
    #                 normal.append((parameter, numeric_value))

    #         elif parameter.lower() == "total leucocyte count":
    #             if numeric_value <= 3600 or numeric_value >=12100:
    #                 critical.append((parameter, numeric_value))
    #             elif numeric_value >=4000 and numeric_value <= 11000:
    #                 borderline.append((parameter, numeric_value))
    #             else:
    #                 normal.append((parameter, numeric_value))

    #     else:
    #         print(f"❌ Could not extract numeric value for {parameter}")  # Debugging Step 5

    # classified_data = {
    #     "Critical": critical,
    #     "Borderline": borderline,
    #     "Normal": normal
    # }

    # print("Final Classified Data:", classified_data)  # Debugging Step 6
    # return classified_data

if __name__ == "__main__":
    # Load extracted text from OCR
    with open("ocr_text.txt", "r") as f:
        ocr_text = f.read()

    print("🔍 RAW OCR TEXT:\n", ocr_text)  # Print raw text before regex
    cleaned_text = clean_ocr_text(ocr_text)
    # print("CLEANED OCR TEXT:\n", cleaned_text)  # Debugging step  
    cleaned_text = clean_ocr_text(ocr_text)  
    print("🔍 Cleaned OCR Text:\n", cleaned_text)  # Debugging print

    parameters = extract_parameters(ocr_text)
    print("Extracted Parameters:", parameters)
    classified_results = classify_parameters(parameters)
    print("Classified Results:", classified_results)
   
