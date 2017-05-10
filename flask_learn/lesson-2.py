from flask import request, url_for
from flask.ext.api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)

@app.route('/', methods=['GET', 'POST'])
def example():
    if request.method == 'POST':
	note = str(request.data.get("name"))
	return {'message': note}
    else:
    	return {'message': 'This is a get call'}

@app.route("/<int:key>/", methods=['GET', 'PUT', 'DELETE'])
def item(key):
    print(key)
    return "10"

if __name__ == "__main__":
    app.run(debug=True)
