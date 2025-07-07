from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import PyPDF2
from comment_processor import process_comments

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_pdf():
    file = request.files['file']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Extract PDF text
    with open(filepath, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = '\n'.join(page.extract_text() or "" for page in reader.pages)

    result = process_comments(text)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
