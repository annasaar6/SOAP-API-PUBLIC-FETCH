# bank_info.py
from zeep import Client, helpers
from flask import Flask, request, jsonify

# ------------------------------------------------------------------
# Define the WSDL URL – this is the contract that describes the
# API.
WSDL_URL = "http://www.thomas-bayer.com/axis2/services/BLZService?wsdl"
# Create a Zeep client. Internally it parses the WSDL and builds
# stubs.
client = Client(wsdl=WSDL_URL)

# Create the Flask application.
app = Flask(__name__)


# ------------------------------------------------------------------
def get_bank_details(blz_code: str):
    """
    Calls the getBank operation of BLZService
    and returns the results in plain Python objects.
    """

    # Validate the bank code before calling the SOAP service.
    if not blz_code.isdigit():
        raise ValueError("Bank code must contain only numeric characters.")

    if len(blz_code) != 8:
        raise ValueError("Bank code must be exactly 8 digits long.")

    # Call the SOAP operation – Zeep returns a custom object.
    bank_info = client.service.getBank(blz_code)

    # Convert the Zeep object into a plain dict for easier use.
    bank_dict = helpers.serialize_object(bank_info)

    return {
        "bankCode": bank_dict["blz"],
        "bankName": bank_dict["bezeichnung"],
        "city": bank_dict["ort"],
        "postalCode": bank_dict["plz"],
        "bic": bank_dict["bic"],
    }


# ------------------------------------------------------------------
@app.route("/", methods=["GET"])
def home():
    """
    Simple GET endpoint that displays instructions.
    """
    return jsonify(
        {"message": "German Bank-Code SOAP Service", "example": {"blz": "37050198"}}
    )


# ------------------------------------------------------------------
@app.route("/bank", methods=["POST"])
def bank_lookup():
    """
    POST endpoint that accepts a BLZ code and
    returns bank information from the SOAP service.
    """

    try:
        data = request.get_json()

        if not data or "blz" not in data:
            return jsonify({"error": "Please provide a BLZ bank code."}), 400

        result = get_bank_details(str(data["blz"]).strip())

        return jsonify(result)

    except Exception as exc:
        return (
            jsonify({"error": f"Custom Validation Error: Invalid BLZ value. {exc}"}),
            400,
        )


# ------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
