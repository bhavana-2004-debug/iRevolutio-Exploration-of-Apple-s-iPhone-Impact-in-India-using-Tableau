from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')  # Make sure the file name matches

if __name__ == '__main__':
    app.run(debug=True)
