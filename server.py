import json

from flask import Flask, request
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key="YOUR_SECRET_KEY_API")
@app.route('/summary', methods=['POST'])
@app.route('/summary', methods=['POST'])
def get_summary():
    text = request.get_json()['text']
    persona = 'High-school English teacher'
    prompt = f"Create the summary of the following text: {text}"
    response = client.chat.completions.create(
        model='gpt-4',
        messages=[
            {
                'role': 'system',
                'content': f'You are a {persona}'
            },
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )
    return response.choices[0].message.content
if __name__ =="__main__":
    app.run()
        
        