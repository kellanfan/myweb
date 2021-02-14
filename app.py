#coding=utf8
"""
# Author: Kellan Fan
# Created Time : Fri 29 Jan 2021 10:18:23 AM CST

# File Name: api.py
# Description:

"""
from flask import Flask
from flask_restful import Api
from app.resources.doublecolorball import DoubleColorBall
from app.resources.cdkey import CDKey
from app.resources.cka import Cka
from app.resources.movie import Movie

app = Flask(__name__)
api = Api(app)

api.add_resource(DoubleColorBall, '/doublecolorball/<action>')
api.add_resource(CDKey, '/cdkey')
api.add_resource(Cka, '/cka')
api.add_resource(Movie, '/movie/search')

if __name__ == '__main__':
    app.run(debug=True)
