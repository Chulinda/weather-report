from flask import Flask, request, render_template, url_for
import requests



API_KEY = 'b423654d53af65eeb9570ef202b47f51'
WS_URL = 'http://api.weatherstack.com/current'
app = Flask(__name__)



@app.route('/' , methods = ['POST', 'GET'])
def index():

    if request.method == 'GET':
        userquery = request.args.get('q', '')

        parameters = {'access_key': API_KEY, 'query':userquery}

        reponse = requests.get(WS_URL, parameters)

        js = reponse.json()


        temperature = js['current']['temperature']
        city = js['location']['name']
        date_ = js['location']['localtime']
        country = js['location']['country']


        return render_template('index.html',temperature = temperature, city = city, date_ = date_, country = country)




if __name__ == '__main__':
    app.run(debug = True)