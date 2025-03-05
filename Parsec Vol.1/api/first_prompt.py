# from google import genai
# from extract_parameters import classified_results as cl

# Category = list(cl.keys())
# table_txt = ""
# for i in cl[Category[0]]:
#     client = genai.Client(api_key="AIzaSyBpJg5IAB6iykrpg8di15wJ6tL8Bumvhtc")
#     response1 = client.models.generate_content(
#         model="gemini-2.0-flash", contents=f"List the diseases happen and causes if {i[0]} is {i[2]} in 10-20 words."
#     )
#     table_txt += response1.text


# client = genai.Client(api_key="AIzaSyBpJg5IAB6iykrpg8di15wJ6tL8Bumvhtc")
# response2 = client.models.generate_content(
#     model="gemini-2.0-flash", contents=f"List {table_txt} in a table with test name, low/high, disease, causes as columns"
# )
# print(response2.text)

from google import genai
from extract_parameters import extract_parameters, classify_parameters

# Load extracted text from OCR
with open("ocr_text.txt", "r") as f:
    ocr_text = f.read()

# Extract parameters and classify them
parameters = extract_parameters(ocr_text)
classified_results = classify_parameters(parameters)

Category = list(classified_results.keys())
table_txt = ""
for i in classified_results[Category[0]]:
    client = genai.Client(api_key="AIzaSyBpJg5IAB6iykrpg8di15wJ6tL8Bumvhtc")
    response1 = client.models.generate_content(
        model="gemini-2.0-flash", contents=f"List the diseases happen and causes if {i[0]} is {i[2]} in 10-20 words."
    )
    table_txt += response1.text

client = genai.Client(api_key="AIzaSyBpJg5IAB6iykrpg8di15wJ6tL8Bumvhtc")
response2 = client.models.generate_content(
    model="gemini-2.0-flash", contents=f"List {table_txt} in a table with test name, low/high, disease, causes as columns"
)
print(response2.text)