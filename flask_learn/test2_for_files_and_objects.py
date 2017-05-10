from flask import request, url_for
from flask.ext.api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)

@app.route("/client/", methods=['GET'])
def clients():
    discriptor = open("/Users/harvindersingh/git_workspace/hello-world/flask_learn/clients_biodata.py", "r+")
    biodata_of_clients = discriptor.read()
    users = {}
    for lines in biodata_of_clients.split("\n"):
        if lines is not "":
            biodata = lines.split("|")
            users[biodata[0]] = {}
            users[biodata[0]] = biodata[1]
	    users[biodata[0]] = biodata[2]
	    users[biodata[0]] = biodata[3]

        return users 

if __name__ == "__main__":
    app.run(debug=True)
        
