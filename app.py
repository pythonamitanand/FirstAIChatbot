# app.py
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# Initialize OpenAI client (Replace with your API key)
client = OpenAI(api_key='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')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    
    try:
        # Create chat completion with OpenAI's new API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[
                {"role": "user", "content": user_message}
            ]
        )
        
        # Extract the AI's response
        ai_response = response.choices[0].message.content
        
        return jsonify({"response": ai_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)