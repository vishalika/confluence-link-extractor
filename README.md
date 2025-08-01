# 📄 Confluence Page Link Extractor

A Streamlit web application that connects to a Confluence space, extracts all page URLs (excluding archived pages), and allows users to download the list as an Excel file.

---

## 📌 Description

This app helps users from any organization retrieve a list of Confluence page URLs from a specified space. It filters out pages that are nested under an "Archive" section and provides a clean export of active page links.

---

## ✨ Features

- Connect to any Confluence instance using base URL, space key, email, and API token
- Fetch all pages from the specified space
- Exclude pages under "Archive" sections (case-insensitive)
- Display page titles and URLs in a table
- Export results to Excel (.xlsx) format

---

## 🚀 Setup Instructions

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/confluence-link-extractor.git
   cd confluence-link-extractor
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

---

## 🧑‍💻 Usage

1. Enter your Confluence base URL (e.g., `https://yourcompany.atlassian.net/wiki`)
2. Enter the space key (e.g., `ENG`, `HR`, `TSSG`)
3. Provide your Atlassian email and API token
4. Click **Fetch Page Links**
5. View the results and download them as an Excel file

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Requests
- OpenPyXL

---

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.
```

---
