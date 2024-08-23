# Weather Predictor with DHT11

This project uses an ESP32 microcontroller to read temperature and humidity data from a DHT11 sensor and upload it to Firebase Realtime Database. The data is then retrieved by a Flask web application, which uses a machine learning model to predict weather conditions based on the sensor data.

## Table of Contents

- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Arduino Code](#arduino-code)
- [Flask Application](#flask-application)
- [Firebase Setup](#firebase-setup)
- [Machine Learning Model](#machine-learning-model)
- [How to Run the Project](#how-to-run-the-project)

## Hardware Requirements

- ESP32 microcontroller
- DHT11 temperature and humidity sensor
- Jumper wires
- Breadboard

## Software Requirements

- Arduino IDE
- Python  3.12.0
- Flask
- Firebase Admin SDK
- Scikit-learn
- NumPy
- Pickle

## Arduino Code

The `arduinocode.ino` file contains the code for the ESP32 microcontroller. This code connects to a Wi-Fi network, reads temperature and humidity data from the DHT11 sensor, and uploads the data to Firebase Realtime Database.

### Libraries Used

- `WiFi.h` for connecting to Wi-Fi
- `FirebaseESP32.h` for Firebase communication
- `DHT.h` for interfacing with the DHT11 sensor

### Key Configuration

```cpp
const char* ssid = "your_ssid";
const char* password = "your_password";
#define FIREBASE_HOST "your_firebase_host"
#define FIREBASE_AUTH "your_firebase_auth_token"
#define DHTPIN 4      
#define DHTTYPE DHT11
