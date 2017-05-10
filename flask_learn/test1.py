from flask import request, url_for
from flask.ext.api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)

@app.route("/users", methods=['GET'])
def get_users():
    discriptor = open("/Users/harvindersingh/git_workspace/hello-world/flask_learn/clients_biodata.py", "r+")
    biodata = discriptor.read()
    all_users = {}
    for lines in biodata.split("\n"):
        if lines is not "":
            users_data = lines.split("|")
            all_users[users_data[0]] = {}
            all_users[users_data[0]]["first_name"] = users_data[1]
            all_users[users_data[0]]["last_name"] = users_data[2]
            all_users[users_data[0]]["address"] = users_data[3]
            all_users[users_data[0]]["city"] = users_data[4]
            all_users[users_data[0]]["state"] = users_data[5]
    return all_users

if __name__ == "__main__":
    app.run(debug=True)
