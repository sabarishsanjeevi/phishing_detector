from flask import Flask, render_template, request
from tensorflow import keras
from Feature_Extractor import extract_features

app = Flask(__name__, template_folder='templates', static_folder='Static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    url = request.form.get("url")
    print(url)
    model_path = r"C:\Users\sabar\Downloads\Phishing-Attack-Domain-Detection-main\Phishing-Attack-Domain-Detection-main\models\Malicious_URL_Prediction.h5"
    print("Loading the model...")
    model = keras.models.load_model(model_path)

    url_features = extract_features(url)

    print("Making prediction...")
    prediction = model.predict([url_features])

    i = prediction[0][0] * 100
    i = round(i, 3)

    return render_template('result.html', data = {'url': url, 'score': i})
