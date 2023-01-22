from flask import Flask, request


app = Flask(__name__)

@app.route("/soma", methods=["POST"])
def operacao():
    response = request.json
    return{"r": response["x"] + response["y"]}

    
if __name__ == "___main___":
    app.run(debug=True)