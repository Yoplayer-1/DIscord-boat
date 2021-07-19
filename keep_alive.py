from flask import Flask , render_template
from threading import Thread


app = Flask('')

@app.route('/')
def home():
  return """<title>Discord.bot</title>
  <h1>Hello discord</h1>"""



def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
