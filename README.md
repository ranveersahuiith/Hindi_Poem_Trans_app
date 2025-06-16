# Hindi Poem Translator App

A simple AI-powered app to:
- Extract Hindi text from images
- Romanize and translate it line-by-line

### ✅ Features
- Image Upload
- OCR with Tesseract
- GPT-4o based Romanization + Translation

---

## 🛠️ Setup (Ubuntu)

### 1. Install Tesseract with Hindi support
```bash
sudo apt update
sudo apt install tesseract-ocr tesseract-ocr-hin
```

### 2. Clone this repository and install dependencies
```bash
git clone <repo-url>
cd Poem_chat_app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Set up your OpenAI API key

Create a `.env` file in the project root with:
```
OPENAI_API_KEY=your_openai_api_key_here
```

---

## 🚀 Usage

1. Start the Flask app:
    ```bash
    python app.py
    ```
2. Open your browser and go to [http://localhost:5000](http://localhost:5000)
3. Upload an image containing a Hindi poem.
4. View the extracted, romanized, and translated text.

---

## 📁 Project Structure

```
.
├── app.py
├── requirements.txt
├── .env
├── README.md
├── statics/
│   └── style.css
├── templates/
│   └── index.html
├── uploads/
│   └── (uploaded images)
```

---

## 📝 Notes

- Make sure Tesseract is installed with Hindi language support.
- The app uses OpenAI's GPT-4o for translation and romanization.
- Uploaded images are stored in the `uploads/` directory.

---


