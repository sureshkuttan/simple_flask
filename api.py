from flask import Flask, request, render_template,jsonify

app = Flask(__name__)

def morse_code(text1):
   text1 = text1.lower()
   #text2 = text2.upper()
   combine = text1 + " Will be convertedd to morse code after implementing Rohans code"
   return combine

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/join', methods=['GET','POST'])
def my_form_post():
    text1 = request.form['text1']
    word = request.args.get('text1')
    #text2 = request.form['text2']
    combine = morse_code(text1)
    result = {
        "output": combine
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)

