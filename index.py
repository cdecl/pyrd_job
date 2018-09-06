from flask import Flask, request
from flask_api import FlaskAPI
import http.client
import json

app = FlaskAPI(__name__)

class Rundeck:
    @staticmethod
    def run(token, jobid):
        conn = http.client.HTTPConnection("localhost", 4440)
        headers = { 'x-rundeck-auth-token': token, 'accept': 'application/json' }

        conn.request("POST", "/api/26/job/{0}/run".format(jobid), headers=headers)
        res = conn.getresponse()
        xmltext = res.read().decode("utf-8")
        
        return json.loads(xmltext)  

@app.route("/api/Run/<string:token>/<string:jobid>", methods=['GET', 'POST'])
def index(token, jobid):
    result = Rundeck.run(token, jobid)
    return result
    
@app.route("/")
def home():
    return "alive"


if __name__ == '__main__':
    # app.run(debug=True)
    app.run()


