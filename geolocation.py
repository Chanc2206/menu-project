from flask import Flask, jsonify , request
from geopy.geocoders import Nominatim

app = Flask(__name__)

@app.route('/geocoordinates',methods=["GET","POST"])
def geocoordinates():
    # Initialize Nominatim API
    main = request.form['n']
    geolocator = Nominatim(user_agent="geoapi")
    
    # Define a fixed location
    location = main
    
    # Get location details
    location_data = geolocator.geocode(location)
    
    # Return latitude and longitude
    if location_data:
        coordinates = (location_data.latitude, location_data.longitude)
    else:
        coordinates = "Location not found"
    
    return jsonify({"location": location, "coordinates": coordinates})


if __name__ == '__main__':
    app.run(debug=True)


