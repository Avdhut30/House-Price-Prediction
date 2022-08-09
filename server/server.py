from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_house_price', methods=['POST'])
def predict_house_price():
    Area = float(request.form['Area'])
    location = request.form['location']
    Num_of_bathrooms = int(request.form['Num_of_bathrooms'])
    Num_of_bedrooms = int(request.form['Num_of_bedrooms'])
    CarParking = int(request.form['CarParking'])
    Gasconnection = int(request.form['Gasconnection'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,Area,Num_of_bathrooms,Num_of_bedrooms,CarParking,Gasconnection)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response





if __name__ == "__main__":
    print("Startting Python Flask Server for House Price prediction....")
    util.load_saved_artifacts()
    app.run()