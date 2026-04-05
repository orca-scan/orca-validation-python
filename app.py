import json
import os
from flask import Flask, request, jsonify

# create a flask app instance
app = Flask(__name__)

# validationHandler is called every time Orca Scan sends a barcode scan to your server.
# It reads the scan data, applies your validation logic, and tells Orca Scan whether
# to save the data, reject it, or change it before saving.
@app.route('/', methods=['POST'])
def validation_handler():
    data = request.get_json()

    # Fields starting with ___ are Orca system fields (e.g. ___orca_sheet_name).
    # All other fields match your sheet column names exactly (case and spaces matter).
    # For example: data.get('Barcode'), data.get('Name'), data.get('___orca_sheet_name')
    name = data.get('Name', '')

    # ---------------------------------------------------------------
    # OPTION 1: Reject the scan and show an error dialog in the app.
    # Return HTTP 400 with an ___orca_message to block the save and
    # display the message to the user. They must dismiss the dialog
    # before they can try again.
    # ---------------------------------------------------------------
    if len(name) > 20:
        return jsonify({
            '___orca_message': {
                'display': 'dialog',
                'type': 'error',
                'title': 'Invalid Name',
                'message': 'Name cannot be longer than 20 characters'
            }
        }), 400

    # ---------------------------------------------------------------
    # OPTION 2: Modify the data before it saves.
    # Return HTTP 200 with only the fields you want to change.
    # Orca Scan will update those fields and allow the save.
    # ---------------------------------------------------------------
    # return jsonify({
    #     'Name': name  # example: you could trim whitespace or reformat the value
    # }), 200

    # ---------------------------------------------------------------
    # OPTION 3: Show a success notification (green banner in the app).
    # The data still saves - this just gives the user feedback.
    # Return HTTP 200 with an ___orca_message to show the notification.
    # ---------------------------------------------------------------
    # return jsonify({
    #     '___orca_message': {
    #         'display': 'notification',
    #         'type': 'success',
    #         'message': 'Barcode scanned successfully'
    #     }
    # }), 200

    # ---------------------------------------------------------------
    # SECURITY: Verify the request came from your specific Orca sheet.
    # Set a secret in Orca Scan (Integrations > Events API > Secret)
    # then check it matches here before trusting the data.
    # ---------------------------------------------------------------
    # secret = request.headers.get('orca-secret')
    # if secret != os.environ.get('ORCA_SECRET'):
    #     return '', 401

    # All good - return HTTP 204 to allow the data to save with no changes.
    # HTTP 204 means "success, no content" - Orca Scan will save the data as-is.
    return '', 204


if __name__ == '__main__':
    # Use the PORT environment variable if set, otherwise default to 8888.
    # This makes the server easy to deploy to cloud platforms that set PORT for you.
    port = int(os.environ.get('PORT', 8888))
    print(f'Listening on port {port}. Ready for Orca Scan requests.')
    app.run(port=port)

