from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/handle_form', methods=['POST'])
def handle_form():
    if request.method == 'POST':
        input_data = request.form['inputField']
        return render_template('result.html', input_data=input_data)

if __name__ == '__main__':
    app.run(debug=True)
