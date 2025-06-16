import os
from flask import Flask, render_template, request
from PIL import Image
import pytesseract
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_image():
    if "image" not in request.files:
        return "No image file provided", 400
    image = request.files["image"]
    if image.filename == "":
        return "No selected image", 400

    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
    image.save(image_path)

    try:
        # Extract Hindi text using Tesseract
        extracted_text = pytesseract.image_to_string(Image.open(image_path), lang='hin')

        prompt = f"""
You are a literary translator.

For each line of the Hindi poem below:
1. Show the original Hindi line.
2. Give its Romanized (phonetic) version.
3. Translate in English.

Please don't use any special characters, just provide the translations in a clear and straightforward manner and i dont anything else rather result.

Poem:
{extracted_text.strip()}
"""

        # Use OpenAI Chat API with GPT-4o
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )

        result_text = response.choices[0].message.content
    except Exception as e:
        result_text = f"Error during LLM processing: {str(e)}"

    return render_template("index.html", result=result_text)

if __name__ == "__main__":
    app.run(debug=True)
