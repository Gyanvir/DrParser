import re

# ICMR Reference Ranges
reference_ranges = {
    "Hemoglobin": (13.8, 17.2),  # Normal range for males (g/dL)
    "WBC Count": (4000, 11000),  # Normal range (cells/µL)
    "Platelet Count": (150000, 450000),  # Normal range (cells/µL)
    "RBC Count": (4.7, 6.1),  # Normal range for males (million cells/µL)
    "Hematocrit (PCV)": (40, 54),  # Normal range for males (%)
    "MCV": (80, 100),  # Mean Corpuscular Volume (fL)
    "MCH": (27, 33),  # Mean Corpuscular Hemoglobin (pg)
    "MCHC": (32, 36),  # Mean Corpuscular Hemoglobin Concentration (g/dL)
    "RDW": (11.5, 14.5),  # Red Cell Distribution Width (%)
    "Neutrophils": (40, 75),  # (% of WBCs)
    "Lymphocytes": (20, 45),  # (% of WBCs)
    "Monocytes": (2, 10),  # (% of WBCs)
    "Eosinophils": (1, 6),  # (% of WBCs)
    "Basophils": (0, 2),  # (% of WBCs)
    "ESR": (0, 20),  # Erythrocyte Sedimentation Rate (mm/hr)
    "Fasting Blood Sugar": (70, 99),  # Normal range (mg/dL)
    "Postprandial Blood Sugar": (70, 140),  # After meal (mg/dL)
    "HbA1c": (4.0, 5.6),  # Glycated Hemoglobin (%)
    "Serum Creatinine": (0.7, 1.3),  # Kidney function (mg/dL)
    "Blood Urea": (7, 20),  # Kidney function (mg/dL)
    "Uric Acid": (3.4, 7.0),  # Normal range for males (mg/dL)
    "Total Cholesterol": (125, 200),  # Normal range (mg/dL)
    "LDL Cholesterol": (0, 100),  # Low-Density Lipoprotein (mg/dL)
    "HDL Cholesterol": (40, 60),  # High-Density Lipoprotein (mg/dL)
    "Triglycerides": (0, 150),  # Normal range (mg/dL)
    "SGPT (ALT)": (7, 56),  # Liver enzyme (U/L)
    "SGOT (AST)": (10, 40),  # Liver enzyme (U/L)
    "Total Bilirubin": (0.1, 1.2),  # Liver function (mg/dL)
    "Direct Bilirubin": (0, 0.3),  # Liver function (mg/dL)
    "Total Protein": (6.4, 8.3),  # Normal range (g/dL)
    "Albumin": (3.5, 5.0),  # Protein in blood (g/dL)
    "Globulin": (2.0, 3.5),  # Protein in blood (g/dL)
    "A/G Ratio": (1.1, 2.5),  # Albumin/Globulin ratio
    "Alkaline Phosphatase": (44, 147),  # Liver & Bone enzyme (U/L)
    "Calcium": (8.5, 10.5),  # Blood calcium levels (mg/dL)
    "Phosphorus": (2.5, 4.5),  # Blood phosphorus levels (mg/dL)
    "Sodium": (135, 145),  # Electrolyte balance (mmol/L)
    "Potassium": (3.5, 5.1),  # Electrolyte balance (mmol/L)
    "Chloride": (96, 106),  # Electrolyte balance (mmol/L)
    "TSH": (0.4, 4.0),  # Thyroid-Stimulating Hormone (µIU/mL)
    "T3": (80, 200),  # Triiodothyronine (ng/dL)
    "T4": (4.5, 12.0),  # Thyroxine (µg/dL)
    "Vitamin D": (30, 100),  # Normal range (ng/mL)
    "Vitamin B12": (200, 900),  # Normal range (pg/mL)
    "C-Reactive Protein (CRP)": (0, 10),  # Inflammation marker (mg/L)
    "Ferritin": (30, 400),  # Iron storage (ng/mL)
    "Iron": (60, 170),  # Normal range (µg/dL)
    "Total Iron Binding Capacity (TIBC)": (250, 450),  # (µg/dL)
}

def lab_selection(lab_no, pdf_text):
    if lab_no == 1:
        # SAHARA DIAGNOSTICS
        def clean_pdf_text(pdf_text):
            """ Cleans pdf text to merge multi-line values. """
            lines = pdf_text.split("\n")
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
            
        def extract_parameters(pdf_text):
            """ Extracts key medical parameters from cleaned pdf text. """
            parameters = {}
        
            patterns = {
                "Haemoglobin": r"HAEMOGLOBIN.*?\(?Hb\)?\s*([\d.]+)",  
                "Total Leucocyte Count": r"TOTAL LEUCOCYTE COUNT.*?\(?TLC\)?\s*([\d,]+)"
            }
            extracted_data = {}
        
            # cleaned_text = clean_pdf_text(pdf_text)  # Preprocess text before regex
            # print("Cleaned pdf Text:\n", clean_pdf_text(pdf_text))  # Debugging line
            for param, pattern in patterns.items():
                match = re.search(pattern, clean_pdf_text(pdf_text), re.IGNORECASE)
                if match:
                    parameters[param] = match.group()
                else:
                    print(f"No match found for {param}")  # Debugging statement
            # print("Extracted Data:", extracted_data)  # Debugging line
        
            return parameters
            
        cleaned_text = clean_pdf_text(pdf_text)
        # print("CLEANED pdf TEXT:\n", cleaned_text)  # Debugging step
    
        parameters = extract_parameters(cleaned_text)
        print("Extracted Parameters:", parameters)
    elif lab_no == 2:
        pass
    else: pass
    return parameters
    
# def classify_parameters(extracted_data):
#     """
#     Classifies extracted blood parameters into Critical, Borderline, and Normal.
#     """
#     classification = {"Critical": [], "Borderline": [], "Normal": []}

#     # Define normal ranges (ICMR Standards)
#     normal_ranges = {
#         "Haemoglobin": (13.5, 18.0),  # Adjust range for gender if needed
#         "Total Leucocyte Count": (4000, 11000),
#     }
    
#     for param, value in extracted_data.items():
#         print(f"Processing: {param} -> {value}")  # Debugging print

#         if param in normal_ranges:
#             lower, upper = normal_ranges[param]

#             try:
#                 value = float(value.replace(",", "").strip())  # Clean and convert to float
#                 print(f"Converted Value: {param} -> {value}")  # Debugging print
#             except ValueError:
#                 print(f"Skipping {param}, invalid number: {value}")  # Debugging print
#                 continue
        
        
#                 # Classification logic
#         if value < lower or value > upper:
#             classification["Critical"].append((param, value))
#         elif lower * 0.9 <= value <= upper * 1.1:  # Borderline = 10% deviation
#             classification["Borderline"].append((param, value))
#         else:
#             classification["Normal"].append((param, value))

#     return classification

# Function to Compare with Normal Ranges
def compare_with_reference(values, reference):
    for parameter, value in extracted_data.items():
        print(f"Processing {parameter}: {value}")  # Debugging Step 3
        # Convert value to a number
        match = re.search(r"[\d,]+\.?\d*", value)  # Extract numeric value
        if match:
            numeric_value = float(match.group().replace(",", ""))  # Remove commas
            print(f"Numeric Value of {parameter}: {numeric_value}")  # Debugging Step 4
    
            ref_low, ref_high = reference.get(test_name, (None, None))
            
            if ref_low is not None and ref_high is not None:
                if numeric_value < ref_low:
                    status = "Low"
                elif numeric_value > ref_high:
                    status = "High"
                elif numeric_value >= ref_high-1 :
                    status = "Borderline_High"
                elif numeric_value <= ref_low+1:
                    status = "Borderline_Low"
                else:
                    status = "Normal"
        else:
            print(f"❌ Could not extract numeric value for {parameter}")  # Debugging Step 5
                
    return status, numeric_value


def classify_parameters(extracted_data):
    critical = []
    borderline = []
    normal = []

    print("🔍 Debug: Inside classify_results function")  # Debugging Step 1
    print("Extracted Data for Classification:", extracted_data)  # Debugging Step 2
    status, value = compare_with_reference(extracted_data, reference_ranges)
    if status == "Low" or status  == "High":
        critical.append((parameter, status, value))
    elif status == "Borderline_Low" or "Borderline_High":
        borderline.append((parameter, status, value))
    else:
        normal.append((parameter, status, value))
    
    classified_data = {
        "Critical": critical,
        "Borderline": borderline,
        "Normal": normal
    }

    print("Final Classified Data:", classified_data)  # Debugging Step 6
    return classified_data

if __name__ == "__main__":
    # Load extracted text from pdf
    with open("pdf_text.txt", "r") as f:
        pdf_text = f.read()
    lab_no = dropdown
    parameters = lab_selection(lab_no, pdf_text)
    classified_results = classify_parameters(parameters)
    print("Classified Results:", classified_results)
   
