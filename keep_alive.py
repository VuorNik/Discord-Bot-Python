from flask import Flask
from threading import Thread
import random
import time
import urllib

app = Flask('')#Flask('')

@app.route('/')
def home():
  return "Elossa ollaan!"

def run():
  app.run(host='0.0.0.0', port=random.randint(2000,9000))#8080)

def keep_alive():
  t = Thread(target=run)
  t.start()
