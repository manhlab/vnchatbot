from flask import Flask,render_template, jsonify, request
from setup import Chatbot
from keras.models import load_model

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    english = ""
    translate =""
    model = load_model('chatbot_model.h5')
    chatbot = Chatbot(model)
    if request.method == "POST":
        # get url that the user has entered
        try:
            english = request.form.get('textbox')
            translate = chatbot.chatbot_response(english)
        except:
           translate = "please type valid messenge."
            
    return render_template('index.html', english=english, translate= translate)

if __name__ == '__main__':
    app.run()