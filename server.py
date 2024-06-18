from flask import Flask, request

app = Flask(__name__)

@app.route('/summary',methods=['POST'])
def getSummary():
    return request.get_json()['text']

if __name__ == "__main__":
    app.run()



