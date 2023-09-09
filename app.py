from flask import Flask, request, jsonify, render_template
from backend import create_core, embeddings, index_documents , extract_text , summarize_cvs
from Post_solr import get_documents_in_folder
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# route to call the create_core function
@app.route('/api/create_core', methods=['POST'])
def create_core_view():
    data = request.json
    selected_value = data.get('selectedValue')

    # Call your Python function with the selected_value
    result = create_core.create_cores(selected_value)
    folder_path = "E:\ITworx\CVs\Documents"+ "\\"+ result
    
    print(embeddings.test_function())
    print(get_documents_in_folder(folder_path))
    # Return a response (if needed)
    return jsonify({'result': result})
# step 0: check if we will add the function that will download the files to the corresponding dircetory based on core name or not.
# step 1: After importing documents call function get_documents_int_folder which will index documents to solr
# step 2: call function get top_ranked_cvs which will take the prompt entered in the search field + perecentage of cvs
# step 3: We need to populate the top applicants page by returning the candidate names
# step 4: call function that will get the matching cv chunks after clicking the button get relevant text
# route to get sentence embedding

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
candidate_data = {
    1: {
        "name": "Candidate 1",
        "summary": "This is the summary for Candidate 1.",
        "sentences": ["Sentence 1", "Sentence 2", "Sentence 3"],
    },
    2: {
        "name": "Candidate 2",
        "summary": "This is the summary for Candidate 2.",
        "sentences": ["Sentence 4", "Sentence 5"],
    },
    3: {
        "name": "Candidate 3",
        "summary": "This is the summary for Candidate 3.",
        "sentences": ["Sentence 6", "Sentence 7", "Sentence 8"],
    },
}
@app.route('/searchprompt', methods=['POST'])
def receive_input():
    data = request.get_json()
    user_input = data.get('userInput')
    # Process user_input as needed
    # You can return a response back to the frontend if necessary
    response_data = {'message': 'Received user input', 'input': user_input}
    return jsonify(response_data)

# Function to handle view_summary action
def view_summary(candidate_id):
    # Replace this with your actual code to handle view_summary
    summary = candidate_data[candidate_id]["summary"]
    return summary

def view_sentence(candidate_id):
    # Replace this with your actual code to handle view_sentence
    sentences = candidate_data[candidate_id]["sentences"]
    return sentences

@app.route('/api/view_data', methods=['POST'])
def view_data():
    data = request.get_json()
    action = data.get('action')
    candidate_id = data.get('candidateId')

    if action == "view_summary":
        summary = view_summary(candidate_id) #call our summary func
        return jsonify({"summary": summary})
    elif action == "view_sentence":
       sentences = view_sentence(candidate_id) #call our sentences func
       return jsonify({"sentences": sentences})
    else:
        return jsonify({"error": "Invalid action"})
    

if __name__ == '__main__':
    app.run(debug=True)
