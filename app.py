from flask import Flask, render_template
import numpy as np
import pickle
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Load the model and label encoder from the .pkl files
model = pickle.load(open('finalModel.pkl', 'rb'))
label_encoder = pickle.load(open('finalEncoder.pkl', 'rb'))

# Firebase setup
cred = credentials.Certificate('weather-predictor-with-dht11-firebase-adminsdk-cm6w2-877a3b4fb1.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://weather-predictor-with-dht11-default-rtdb.asia-southeast1.firebasedatabase.app'
})

# Route to display data and predict weather
@app.route('/')
def home():
    # Get temperature and humidity from Firebase
    ref = db.reference('sensorData')
    data = ref.get()
    
    temperature = data['temperature']
    humidity = data['humidity']

    # Prepare the input for the model
    input_data = np.array([[temperature, humidity]])
    
    # Make the prediction
    encoded_prediction = model.predict(input_data)
    predicted_weather = label_encoder.inverse_transform(encoded_prediction)

    # Map the prediction to the corresponding image filename
    weather_images = {
        'drizzle': 'drizzel.png',
        'fog': 'fog.png',
        'rain': 'rain.png',
        'snow': 'snow.png',
        'sun': 'sunny.png'
    }
    prediction_image = weather_images.get(predicted_weather[0], 'default.png')

    # Get the current date and time
    current_date = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")

    return render_template('firebase_result.html', temperature=temperature, humidity=humidity, prediction=predicted_weather[0], prediction_image=prediction_image, current_date=current_date, current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True)
