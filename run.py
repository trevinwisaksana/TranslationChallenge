# Importing Flask
from flask import Flask, request, redirect
# Importing Twilio
import twilio.twiml

app = Flask(__name__)

''' We're doing this because 'POST' means that we're going
to make an update. In this case, the reply is the update? '''


@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
    resp = twilio.twiml.Response()
    resp.message("Hello, Mobile Monkey")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
