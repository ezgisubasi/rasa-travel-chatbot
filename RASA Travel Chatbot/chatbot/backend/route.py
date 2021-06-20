# from wsgi import app
from flask import request,jsonify
import json
import requests
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)

CORS(app)
@app.route('/chat', methods=['POST'])
def chat():
    if request.method == 'POST':
        query = request.json['query']
        userChat = json.dumps({"sender": "User","message": str(query)})
        resp = requests.post("http://localhost:5005/webhooks/rest/webhook",data=userChat,
                        headers={'Content-type':'application/json','Accept':'text/plain'})
        if (resp.status_code ==200):
            returnList = []
            for i in resp.json():
                try:
                    var = json.loads(i['text'])
                    returnList.append({'reply':var['reply']})
                except Exception:
                    returnList.append({'reply':i['text']})
            return jsonify(returnList)
        else:
            return jsonify([{'reply':'Connection Problem to the response processing sever'}])
    
    else:
        return jsonify({'reply':'CORS OK'})

if __name__=='__main__':
    app.run(debug=True)