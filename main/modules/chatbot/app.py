from flask import Flask,render_template, jsonify, request,redirect, url_for
from flask_cors import CORS
import chat_API
import pywhatkit
import pickle
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
CORS(app)
run_with_ngrok(app)               #this is needed to use ngrok for port forwarding
database={'subho':'hero','soham':'chomu','yash':'pagla','tublu':'7415'}

# @app.route('/predict',methods=['POST'])
# def index():
#     user_input = request.args.get('user_input')
#     return jsonify({'user_input':str(chat_API.brain(user_input))})

@app.route("/")
def home():
    return render_template("login.html")

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
	    return render_template('login.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
	        return render_template('index.html',name=name1)



@app.route("/get")
def get_bot_response():
    userText = request.args.get('user_input')
    userText = userText.lower()
    if "search youtube" in userText:
        userText = userText.replace('search youtube', '')  
        pywhatkit.playonyt(userText)
        return "searched youtube"+str(userText)
    elif "search" in userText:
        userText = userText.replace('search', '')  
        pywhatkit.search(userText) 
        return "searched"+str(userText)
    elif "whatsapp" in userText:
        return "I am trying" + "I cannot open whatsapp"
    elif "what is your name" in userText:
        return "My name is Chatterbot"
    return str(chat_API.brain(userText))
    
@app.route('/logout')
def logout():
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()
    