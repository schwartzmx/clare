from sanic import Sanic
from sanic.response import json
from sanic.exceptions import NotFound
from data import COUNTRIES, LANGUAGES
import urllib.parse

app = Sanic()

@app.route("/country/<name>")
async def country(request, name):
    country = decode(name).lower()
    result = [c for c in COUNTRIES 
        if c['Name'].lower() == country]
    if result:
        return json(result)
    else:
        raise NotFound("Requested country was not found.")

@app.route("/country/all")
async def country_all(request):
    return json(COUNTRIES)

@app.route("/language/<name>")
async def language(request, name):
    lang = decode(name).lower()
    result = [l for l in LANGUAGES
        if l['Name'].lower() == lang]
    if result:
        return json(result)
    else:
        raise NotFound("Requested language was not found")

@app.route("/language/all")
async def language_all(request):
    return json(LANGUAGES)

def decode(token):
    return urllib.parse.unquote(token)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)