
import json
from flask import Flask
from flask import request
import re


app = Flask(__name__)


REGEX_VOGAL = '[aeiouAEIOUáàâãéèêíïóôõöú]'
def count_vogals(element:str):
    p = re.findall(REGEX_VOGAL,element)
    return len(p)


@app.route("/", methods = ["POST"])
def vogal_route():
    return "<h1>Bem vindo à api do javier!</h1>"


@app.route("/vowel_count", methods = ["POST"])
def main_route():
    data = json.dumps(request.json)

    if data is None:
        return "É necessario um input valido no formato ['termo1','termo2','termo3']"

    resp = {}

    if not isinstance([0, 10, 20, 30], list):
        return "Input precisa ser um array"

    post_data = request.get_json()

    for x in post_data:
        resp[x] = count_vogals(x)

    if post_data is not None:
        return resp

    return "É necessario um input valido no formato ['termo1','termo2','termo3']"


if __name__ == '__main__':
    app.run()