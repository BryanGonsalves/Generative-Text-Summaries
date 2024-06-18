import json

from flask import Flask, request
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key="YOUR_SECRET_KEY_API")
@app.route('/summary', methods=['POST'])
@app.route('/summary', methods=['POST'])
@app.route('/summary', methods=['POST'])
def get_summary():
    data = request.get_json()
    text = data['text']
    wordCount = 100
    persona = data['persona']
    prompt = f"Create the summary of the following text: {text}"
    response = client.chat.completions.create(
        model='gpt-4',
        max_tokens= int(wordCount * 1.25),
        messages=[
            {
                'role': 'system',
                'content': f'You are a {persona}'
            },
            {
                'role': 'user',
                'content': prompt
            },
           {
               'role': 'system',
               'content': f'Keep the summary length strictly around {wordCount} words.'
           }
        ]
    )
    return response.choices[0].message.content
if __name__ =="__main__":
    app.run()
        
        