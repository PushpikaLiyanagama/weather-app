from flask import Flask, render_template
import numpy as np
import pickle
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime


app = Flask(__name__)


model = pickle.load(open('finalModel.pkl', 'rb'))
label_encoder = pickle.load(open('finalEncoder.pkl', 'rb'))

# Credeitials for firebase
cred = credentials.Certificate('weather-predictor-with-dht11-firebase-adminsdk-cm6w2-877a3b4fb1.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://weather-predictor-with-dht11-default-rtdb.asia-southeast1.firebasedatabase.app'
})

@app.route('/')
def home():
    
    ref = db.reference('sensorData')
    data = ref.get()
    
    temperature = data['temperature']
    humidity = data['humidity']

    # Adding data to array
    input_data = np.array([[temperature, humidity]])
    
    encoded_prediction = model.predict(input_data)
    predicted_weather = label_encoder.inverse_transform(encoded_prediction)

    weather_images = {
        'drizzle': 'drizzel.png',
        'fog': 'fog.png',
        'rain': 'rain.png',
        'snow': 'snow.png',
        'sun': 'sunny.png'
    }
    prediction_image = weather_images.get(predicted_weather[0], 'default.png')

    current_date = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")

    return render_template('firebase_result.html', temperature=temperature, humidity=humidity, prediction=predicted_weather[0], prediction_image=prediction_image, current_date=current_date, current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True)
