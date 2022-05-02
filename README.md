# orca-validation-python

Example of [how to validate barcode scans in real-time](https://orcascan.com/guides/how-to-validate-barcode-scans-in-real-time-56928ff9) using [Python](https://www.python.org/) and [flask](https://github.com/pallets/flask) framework.

## Install

First ensure you have [Python](https://www.python.org/downloads/) installed:

```bash
# should return 3.7 or higher
python3 --version
```

Then execute the following:

```bash
# download this example code
git clone https://github.com/orca-scan/orca-validation-python.git

# go into the new directory
cd orca-validation-python

# create virtual environment and activate it
python3 -m venv orca && source ./orca/bin/activate

# upgrade pip to latest version
pip install --upgrade pip

# install dependencies
pip install -r requirements.txt
```

## Run

```bash
# activate virtual environment
source ./orca/bin/activate

# enable development features only for development
export FLASK_ENV=development

# start the project
flask run -p 5000 
```

Your server will now be running on port 5000.

You can emulate an Orca Scan Validation input using [cURL](https://dev.to/ibmdeveloper/what-is-curl-and-why-is-it-all-over-api-docs-9mh) by running the following:

```bash
curl --location --request POST 'http://127.0.0.1:5000/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "___orca_sheet_name": "Vehicle Checks",
    "___orca_user_email": "hidden@requires.https",
    "Barcode": "orca-scan-test",
    "Date": "2022-04-19T16:45:02.851Z",
    "Name": Orca Scan Validation Example,
}'
```
### Important things to note

1. Only Orca Scan system fields start with `___`
2. Properties in the JSON payload are an exact match to the  field names in your sheet _(case and space)_

## Example

This [example](app.py) uses the [flask](https://github.com/pallets/flask) framework:

### Barcode validation

[Orca Scan Barcode Data Validation](https://orcascan.com/guides/how-to-validate-barcode-scans-in-real-time-56928ff9)

```python
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
            # return error message
            return json.dumps({
                "title": "Invalid Name",
                "message": "Name cannot contain more than 20 characters",
                })

        # return HTTP Status 204 (No Content)
        return '', 204
```
## Test server locally against Orca Cloud

To expose the server securely from localhost and test it easily against the real Orca Cloud environment you can use [Secure Tunnels](https://ngrok.com/docs/secure-tunnels#what-are-ngrok-secure-tunnels). Take a look at [Ngrok](https://ngrok.com/) or [Cloudflare](https://www.cloudflare.com/).

```bash
ngrok http 5000
```

## Troubleshooting

If you run into any issues not listed here, please [open a ticket](https://github.com/orca-scan/orca-validation-python/issues).

## Examples in other langauges
* [orca-validation-dotnet](https://github.com/orca-scan/orca-validation-dotnet)
* [orca-validation-python](https://github.com/orca-scan/orca-validation-python)
* [orca-validation-go](https://github.com/orca-scan/orca-validation-go)
* [orca-validation-java](https://github.com/orca-scan/orca-validation-java)
* [orca-validation-php](https://github.com/orca-scan/orca-validation-php)
* [orca-validation-node](https://github.com/orca-scan/orca-validation-node)

## History

For change-log, check [releases](https://github.com/orca-scan/orca-validation-python/releases).

## License

&copy; Orca Scan, the [Barcode Scanner app for iOS and Android](https://orcascan.com).