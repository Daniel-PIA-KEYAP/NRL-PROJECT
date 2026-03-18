from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200

@app.route('/api/predict/next-match', methods=['GET'])
def predict_next_match():
    # Logic for predicting next match goes here
    return jsonify({'next_match': 'Match details'}), 200

if __name__ == '__main__':
    app.run(debug=True)