from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('portfolio.html')

@app.route('/portfolio', methods=['GET'])
def portfolio():
    return render_template('portfolio.html')

@app.route('/experience', methods=['GET'])
def experience():
    return render_template('experience.html')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/skills', methods=['GET'])
def skills():
    return render_template('skills.html')

@app.route('/education', methods=['GET'])
def education():
    return render_template('education.html')

if __name__ == '__main__':
    app.run(debug=True)