from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv(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)

@app.route('/')
def index():
    return "✅ AI Chatbot is Running!"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_message}
            ]
        )
        reply = response.choices[0].message.content.strip()
        return jsonify({'reply': reply})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()
