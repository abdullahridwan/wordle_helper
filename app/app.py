from flask import Flask,render_template,request
from app.screw_wordle import screw_wordle
import nltk

nltk.download('words')

app = Flask(__name__)
 

@app.route('/')
def form():
    return render_template('form.html')
 
@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        yellows = form_data.get("Yellow Letters", "")
        greys = form_data.get("Grey Letters", "")
        greens = form_data.get("Green Letters", "*****")
        possible_words = screw_wordle(yellows, greys, greens)
        return render_template('data.html',form_data = form_data, possible_words = possible_words)
 
 
app.run(host='localhost', port=5000)