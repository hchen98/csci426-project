from flask import Flask
from flask import request, jsonify

app = Flask(__name__)
# app.config["DEBUG"] = True

profil_input = {
    'Email': "",
    'Gender': "",
    'dob': "",
    'Zip': "",
    'GPA': "",
    'Major': "",
    'Race': "",
    'Religion': "",
    'Disabilities': "",
    'SAT Score': "",
    'ACT Score': "",
    'Address 1': "",
    'Address 2': "",
    'Address 3': "",
}


@app.route('/api/v1/csci426/profileInput', methods=['POST'])
def assignProfile():
    global user_profile
    data = request.json
    profil_input = data

    # AA01 profile set code used in RN
    response = "AA01"
    response = jsonify(response)
    response.statue_code = 202
    return response



# =========================== TEST ===========================
# REST API test sample

# Create some test data for our catalog in the form of a list of dictionaries.
books = [{
    'id': 0,
    'title': 'A Fire Upon the Deep',
    'author': 'Vernor Vinge',
    'first_sentence': 'The coldsleep itself was dreamless.',
    'year_published': '1992'
}, {
    'id': 1,
    'title': 'The Ones Who Walk Away From Omelas',
    'author': 'Ursula K. Le Guin',
    'first_sentence':
    'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
    'published': '1973'
}, {
    'id': 2,
    'title': 'Dhalgren',
    'author': 'Samuel R. Delany',
    'first_sentence': 'to wound the autumnal city.',
    'published': '1975'
}]

userAcc = {
    'signedIn': False,
    'full_name': "",
    'last_name': "",
    'first_name': "",
    'email': "",
    'photoUrl': "",
}


@app.route('/api/v1/csci426/test', methods=['POST'])
def assignUsrAcc():
    global userAcc
    data = request.json
    userAcc = data
    return jsonify(userAcc)


@app.route('/', methods=['GET'])
def home():
    return '''
        <h1>Distant Reading Archive</h1>
        <p>A prototype API for distant reading of science fiction novels.</p>
        '''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    response = jsonify(books)
    response.status_code = 202
    return response


@app.route('/api/v1/resources/books', methods=['GET'])
def api_bookID():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        response = "Error: No id field provided. Please specify an id."
        response.statue_code = 204
        return response

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    response = jsonify(results)
    response.status_code = 202
    return response


if __name__ == '__main__':
    app.run()
