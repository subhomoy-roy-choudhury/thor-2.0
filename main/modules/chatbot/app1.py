from flask import Flask,render_template, jsonify, request,redirect, url_for
from flask_cors import CORS
import chat_API
import pywhatkit
import pickle
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
CORS(app)
# run_with_ngrok(app)               #this is needed to use ngrok for port forwarding
database={'subho':'hero','soham':'chomu','yash':'pagla','tublu':'7415'}

@app.route('/predict',methods=['GET','POST'])
def index():
    user_input = request.args.get('user_input')
    user_input = user_input.lower()
    print(user_input)
    if "search youtube" in user_input:
        user_input = user_input.replace('search youtube', '')  
        pywhatkit.playonyt(user_input)
        return jsonify({'user_input':str("searched youtube"+str(user_input))})
    elif "search" in user_input:
        user_input = user_input.replace('search', '')  
        pywhatkit.search(user_input) 
        return jsonify({'user_input':str("searched"+str(user_input))})
    else:
        return jsonify({'user_input':str(chat_API.brain(user_input))})

if __name__ == '__main__':
    app.run()
    