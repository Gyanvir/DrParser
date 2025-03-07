# Dr.Parser

![Dr.Parser Banner](DrParser.png)

## 🚀 Overview
Dr.Parser is an AI-powered blood report analysis tool designed to extract, interpret, and present key health metrics from medical reports. Our goal is to make medical diagnostics more accessible and understandable for both healthcare professionals and individuals.

## 🏆 About the Project
Developed for the **Health-Tech and AI Hackathon** at **IIT (BHU)**, Dr.Parser is our take on simplifying medical report analysis. While we may not be the most technically advanced team, our strength lies in execution. We believe in the power of innovation and dedication, and if selected, we are eager to take this project to new heights.

## 💡 Why No Deployment?
Since Dr.Parser includes an ML-based backend, deploying it on a cloud engine would require resources beyond our current capacity. However, we have ensured that everything is well-documented so that you can run it locally without issues.

Even if this project doesn’t seem technically extravagant, we promise to give our heart and soul to making it a real-world healthcare solution.

---

## 🛠 Tech Stack & Tools Used
- **Frontend:** React.js (Material-UI, Redux)
- **Backend:** FastAPI
- **AI/ML:** EasyOCR, OpenCV, Gemini AI
- **Database & Caching:** MongoDB, Redis

## 📥 Installation & Setup (Run Locally)
To set up the project on your local machine, follow these steps:

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/Gyanvir/DrParser.git
cd Parsec Vol.1
```

### 2️⃣ Set Up the Python Backend (API)
Navigate to the `api` folder and create a virtual environment:
```sh
cd api
python -m venv venv  # Windows
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

Now install the required dependencies:
```sh
pip install -r requirements.txt
```

Run the backend server:
```sh
uvicorn main:app --reload
```

### 3️⃣ Set Up the Frontend
Open a new terminal while keeping the virtual environment active and navigate to the `frontend` folder:
```sh
cd ../frontend
npm install  # Install dependencies
npm start  # Start the development server
```

Your frontend will now be running at `http://localhost:3000`, and the backend API will be available at `http://localhost:8000`.

---

## ⚠️ Important Note on Upload Button
When you press the **Upload** button, kindly wait patiently for the analysis to generate. The process may take up to **2 minutes** due to the ML model's processing time. Currently, there is no visible action after clicking the button, but rest assured, your file is being processed in the background.

---

## 🌟 Features
- **OCR-Powered Report Parsing:** Extracts key health parameters from blood reports.
- **AI-Based Analysis:** Provides insights using Gemini AI.
- **User-Friendly Interface:** Built with Material-UI for a smooth experience.
- **Scalable Architecture:** Designed with MongoDB and Redis for future improvements.

---

## 🔮 Future Vision
We plan to enhance Dr.Parser with:
- ✅ Advanced AI models to dynamically interpret test reference ranges.
- ✅ Improved UI/UX for seamless interaction.
- ✅ Support for direct PDF uploads.
- ✅ A login & authorization system for user report tracking.
- ✅ Optimized ML model deployment for real-time results.

---

## 📷 Screenshots & Demo
### 1️⃣ Home Page  
![Home Page](https://github.com/user-attachments/assets/8b43cc2b-4cb9-4244-8c37-ae689fd89577)  

### 2️⃣ Analysis Output  
![Analysis Output](https://private-user-images.githubusercontent.com/44435797/420402198-9968ea41-1d17-4eab-b485-074639353d6b.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDEzNjIxOTIsIm5iZiI6MTc0MTM2MTg5MiwicGF0aCI6Ii80NDQzNTc5Ny80MjA0MDIxOTgtOTk2OGVhNDEtMWQxNy00ZWFiLWI0ODUtMDc0NjM5MzUzZDZiLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAzMDclMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMzA3VDE1MzgxMlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTdkNTBkNjkzNmIzZjU1MjVhMWM2OTM3NzhiOTdmMGE2YmYzZWJiYmU3ZDU1MzRiY2I4YjYxOGRjOWQ1Nzc2ZmUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.2EpsX5pAzEjXKCvZ5_lPDH0M3Ox9c0zBuUXbjckB6QY
)  

### 3️⃣ Future Vision  
![Future Vision](https://private-user-images.githubusercontent.com/44435797/420402199-bd1b8e40-c0d6-4671-82dd-1e64dc8a5120.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDEzNjIxOTIsIm5iZiI6MTc0MTM2MTg5MiwicGF0aCI6Ii80NDQzNTc5Ny80MjA0MDIxOTktYmQxYjhlNDAtYzBkNi00NjcxLTgyZGQtMWU2NGRjOGE1MTIwLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAzMDclMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMzA3VDE1MzgxMlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWFhMDUyYjU4MTFmYzNiNmMwYzBhOTdmY2UwZDUyYThiYzIwNzAzZDE0MmE0ZDQzN2I2MDA0NDFhZTRmNjYxNmUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.KtU34jhC8PWpGakbj49AUjQIHbR1_lOySMnxiw4iCQ4
)  

### 4️⃣ What People Say  
![What People Say](https://private-user-images.githubusercontent.com/44435797/420402197-f0b8b451-e5a1-4278-a9a6-c5bb91a65818.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDEzNjIxOTIsIm5iZiI6MTc0MTM2MTg5MiwicGF0aCI6Ii80NDQzNTc5Ny80MjA0MDIxOTctZjBiOGI0NTEtZTVhMS00Mjc4LWE5YTYtYzViYjkxYTY1ODE4LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAzMDclMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMzA3VDE1MzgxMlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWZmNzBjNWMxMTUzZjU5NjJlNmU1NmNhM2EwMTdiMDljYzUzOWM5YmY5ZmRjN2VjYzM4OWZkYTFhMWRjMWEzMjgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.KvZzE0PO-EPfF5Mfomp5nyWyXznFQoY1mYCwpl1aswo
)  


### 5️⃣ Made with ❤️ By Team Euphoria
![Team Euphoria](https://private-user-images.githubusercontent.com/44435797/420402201-260c8b97-8a75-4463-8a68-9aa76f9113e4.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDEzNjIxOTIsIm5iZiI6MTc0MTM2MTg5MiwicGF0aCI6Ii80NDQzNTc5Ny80MjA0MDIyMDEtMjYwYzhiOTctOGE3NS00NDYzLThhNjgtOWFhNzZmOTExM2U0LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAzMDclMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMzA3VDE1MzgxMlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWM1ZWNjMzViNmQ2ZmQ3MGIxNTFhNGVhOTMwYzFlNmRmMTJlZWZkMGIzNGJmYWFjOTJjZGRiYmU1ZDE0MGNlZGEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.SI32x6TM0Zpv5VnMTNNoH5qFT2siOebmlU3m9OAMrog)  


---

## 🏆 Team Euphoria
Developed by:
- **Gyanvir Singh**
- **Himanshu Bansal**
- **Rajveer Rangile**

---

## 📝 Judging Criteria & Compliance
This project meets the hackathon's judging criteria:
✅ **Functionality:** Fully working local setup.
✅ **Code Quality:** Well-structured and documented.
✅ **Scalability:** Designed for future improvements.
✅ **Innovation:** AI-driven medical analysis.

---

## 📜 License
This project is open-source under the [MIT License](LICENSE).

---

## ❤️ Final Words
We may not be the best coders, but we are passionate executors. Given the opportunity, we are determined to make Dr.Parser a revolutionary healthcare tool. Thank you for reviewing our project!

