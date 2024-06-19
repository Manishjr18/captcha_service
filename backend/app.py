from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from captcha.image import ImageCaptcha
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("mongodb+srv://manishjr2507:9HrcegdiUIu80Cbr@captcha.s5rejtk.mongodb.net/")
mongo = PyMongo(app)

@app.route('/generate-captcha', methods=['GET'])
def generate_captcha():
    image = ImageCaptcha()
    captcha_text = "1234"  # Replace with actual captcha generation logic
    image_data = image.generate(captcha_text)
    image_file = f'static/captcha_{captcha_text}.png'
    image.write(captcha_text, image_file)
    return jsonify({"captcha": image_file})

@app.route('/validate-captcha', methods=['POST'])
def validate_captcha():
    data = request.json
    user_input = data.get('captcha')
    # Validation logic here
    return jsonify({"valid": user_input == "1234"})

if __name__ == '__main__':
    app.run(debug=True)
