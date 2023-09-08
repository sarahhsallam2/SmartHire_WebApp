from flask import Flask, request, jsonify, render_template
#from backend import create_core
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
'''@app.route('/api/create_core', methods=['POST'])
def create_core_view():
    data = request.json
    selected_value = data.get('selectedValue')

    # Call your Python function with the selected_value
    result = create_core.create_cores(selected_value)

    # Return a response (if needed)
    return jsonify({'result': result})'''


# Define a route to render a template
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/acceptedresumes')
def acceptedresumes():
    return render_template('acceptedresumes.html')
@app.route('/candidates')
def candidates():
    return render_template('candidates.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
@app.route('/features')
def features():
    return render_template('features.html')
@app.route('/Login')
def Login():
    return render_template('Login.html')
@app.route('/pricing')
def pricing():
    return render_template('pricing.html')
@app.route('/product')
def product():
    return render_template('product.html')
@app.route('/service')
def service():
    return render_template('service.html')
@app.route('/signup')
def signup():
    return render_template('signup.html')
@app.route('/startscreening')
def startscreening():
    return render_template('startscreening.html')
@app.route('/register')
def Register():
    return render_template('Register.html')

if __name__ == '__main__':
    app.run(debug=True)
