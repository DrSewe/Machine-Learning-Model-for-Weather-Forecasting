from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the saved model
saved_model = joblib.load('best_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the form
    maxtempC = float(request.form['maxtempC'])
    mintempC = float(request.form['mintempC'])
    cloudcover = float(request.form['cloudcover'])
    humidity = float(request.form['humidity'])
    sunHour = float(request.form['sunHour'])
    HeatIndexC = float(request.form['HeatIndexC'])
    precipMM = float(request.form['precipMM'])
    pressure = float(request.form['pressure'])
    windspeedKmph = float(request.form['windspeedKmph'])

    # Create a DataFrame with the input data
    input_data = pd.DataFrame({
        'maxtempC': [maxtempC],
        'mintempC': [mintempC],
        'cloudcover': [cloudcover],
        'humidity': [humidity],
        'sunHour': [sunHour],
        'HeatIndexC': [HeatIndexC],
        'precipMM': [precpMM],
        'pressure': [pressure],
        'windspeedKmph': [windspeedKmph]
    })

    # Make predictions
    prediction = saved_model.predict(input_data)

    # Return the prediction
    return f'Predicted temperature: {prediction[0]}'

if __name__ == '__main__':
    app.run(debug=True)
