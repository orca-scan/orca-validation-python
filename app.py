# import flask framework
from flask import Flask, request
import requests
import json

# create a flask app instance
app = Flask(__name__)

# POST / handler
@app.route('/', methods=['POST'])
def orca_validation():
    if request.method == 'POST':
        data = request.get_json()

        # dubug purpose: show in console raw data received
        print("Request received: \n"+json.dumps(data, sort_keys=True, indent=4))

        # NOTE:
        # orca system fields start with ___
        # you can access the value of each field using the field name (data["Name"], data["Barcode"], data["Location"])
        name = data["Name"]

        # validation example
        if(len(name) > 20):
            # return json error message
            return json.dumps({
                "title": "Invalid Name",
                "message": "Name cannot contain more than 20 characters",
                })

        # return HTTP Status 204 (No Content)
        return '', 204

