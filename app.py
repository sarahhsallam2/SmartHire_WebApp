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

if __name__ == '__main__':
    app.run(debug=True)
