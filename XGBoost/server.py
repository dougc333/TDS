import os
import flask
from flask import Flask, render_template, request

app = Flask(__name__)


def load_model(t):
  model = pickle.load(open('model.pkl','rb))
  predicted = model.predict(t)
  return predicted


@app.route('/')
@app.route('/index')
def index():
  return 'asdfasfasdf'

if __name__=='__main__':
  app.run()

