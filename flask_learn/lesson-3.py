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


#@app.route('/users', methods=['GET'])
#def process():
 #   file_discriptor = open("/Users/harvindersingh/git_workspace/hello-world/flask_learn/clients_biodata.py", "r+")
  #  data = file_discriptor.read()
   # for line in data.split("\n"):
    #    if line is not "":
     #       client_data = line.split("|")
#	    id = client_data[0]    
#	    first_name = client_data[1]
 #           last_name = client_data[2]
  #          address = client_data[3]
    #        city = client_data[4]
     #       state = client_data[5]
	    
    #return {"first_name ":   first_name,"last_name ":  last_name, "address" :  address, "city ":  city,"state ":  state }"""
           
#@app.route("/users/<int:id>/", methods=['GET'])
#def tokenized_ids(id): 
#    discriptor = open("/Users/harvindersingh/git_workspace/hello-world/flask_learn/clients_biodata.py", "r+")
 #   biodata = discriptor.read()
  #  for lines in biodata.split("\n"):
   #     if lines is not "":
    #        users_data = lines.split("|")
            #print users_data
     #       users_id =  int(users_data[0])
      #      first_name = users_data[1]
       #     last_name = users_data[2]
        #    address = users_data[3]
         #   city = users_data[4]
          #  state = users_data[5]
           # if users_id == id:
            #    return {"users_id" : users_id , "first_name" : first_name , "last_name" : last_name , "address" : address , "city" : city , "state" : state}
	

if __name__ == "__main__":
    app.run(debug=True)

