# nothing special just flask lol

from flask import Flask

app = Flask(__name__)

@app.after_request
def treat_as_plain_text(response):
    response.headers["content-type"] = "text/plain; charset=utf-8"
    return response
  
with open("files/init.lua", "r") as init:
  init = init.read()

with open("files/ecstasy.lua", "r") as septex:
  septex = septex.read()

@app.route('/')
def index():
  return "Cracked by Team Ecstasy"


@app.route('/septex/client')
def client():
  return init

@app.route('/septex/server')
def server():
  return septex


app.run(host="0.0.0.0", port=80)
