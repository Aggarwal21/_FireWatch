from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory storage for users
users = []

class User:
    def __init__(self, username, user_type, details):
        self.username = username
        self.user_type = user_type  # 'helper' or 'helpee'
        self.details = details  # Dictionary containing help-related info

    def to_dict(self):
        return {
            'username': self.username,
            'user_type': self.user_type,
            'details': self.details
        }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/helper')
def helper():
    return render_template('helper.html')

@app.route('/helpee')
def helpee():
    return render_template('helpee.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    
    # Basic validation
    if 'username' not in data or 'user_type' not in data or 'details' not in data:
        return jsonify({'message': 'Missing required fields'}), 400
    
    if data['user_type'] not in ['helper', 'helpee']:
        return jsonify({'message': 'Invalid user type'}), 400
    
    try:
        details = data['details']
        if not isinstance(details, dict):
            raise ValueError
        if 'offers' not in details and 'needs' not in details:
            return jsonify({'message': 'Details must contain offers or needs'}), 400
    except ValueError:
        return jsonify({'message': 'Details must be a valid JSON object'}), 400
    
    new_user = User(
        username=data['username'],
        user_type=data['user_type'],
        details=data['details']
    )
    users.append(new_user)
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    
    if 'user_type' not in data or 'responses' not in data:
        return jsonify({'message': 'Missing required fields'}), 400
    
    if data['user_type'] == 'helpee':
        responses = data['responses']
        recommendations = recommend_resources(responses)
        return jsonify({'message': 'Thank you for your responses', 'recommendations': recommendations}), 200
    
    return jsonify({'message': 'Thank you for your responses'}), 200

def recommend_resources(details):
    resources = {
        "food": "Contact local food banks or community kitchens.",
        "shelter": "Check with local shelters or temporary housing organizations.",
        "financial": "Reach out to emergency relief funds or local charities."
        # Add more resources as needed
    }
    
    resource_recommendations = []
    for need in details.get('needs', []):
        if need in resources:
            resource_recommendations.append(resources[need])
    
    return resource_recommendations

@app.route('/match', methods=['POST'])
def match():
    data = request.json
    
    if 'user_type' not in data or 'details' not in data:
        return jsonify({'message': 'Missing required fields'}), 400
    
    matches = []
    for user in users:
        if data['user_type'] == 'helper' and user.user_type == 'helpee':
            if set(data['details']['offers']).intersection(user.details.get('needs', [])):
                matches.append(user.to_dict())
        elif data['user_type'] == 'helpee' and user.user_type == 'helper':
            if set(data['details']['needs']).intersection(user.details.get('offers', [])):
                matches.append(user.to_dict())
    
    return jsonify({'matches': matches}), 200

if __name__ == '__main__':
    app.run(debug=True)
