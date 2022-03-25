import requests
import json

#print("gadfgadf")
#print(1+2)
#text=requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text

#print(text)

#currencies = json.loads(text)
    #print(currency)

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
        text = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text
        currencies = json.loads(text)
        result = ''
        for currency in currencies['Valute']:
            result += str(currency) + '<br>'
        result = text
        return result
if __name__ == "__main__":
        app.run()

b= 5
print(b)