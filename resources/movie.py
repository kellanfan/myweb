#coding=utf8
"""
# Author: Kellan Fan
# Created Time : Fri 29 Jan 2021 01:32:29 PM CST

# File Name: movie.py
# Description:

"""
from app.common.pg_client import Mypostgres
from flask_restful import reqparse, abort, Resource

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True,
                    help="Name cannot be blank!")

class Movie(Resource):
    def post(self):
        args = parser.parse_args()
        ret = handle_movie(args['name'])
        if ret:
            return ret
        else:
            abort(404, message="movie [{}] doesn't exist".format(args['name']))

def handle_movie(name):
    client = Mypostgres()
    sql = "select name, content from piaohua where name like '%{}%'".format(name)
    ret = client.execute(sql)
    final = {}
    try:
        for num in range(len(ret)):
            final['movie' + str(num)] =  {
                  "name": ret[num][0],
                  "content": ret[num][1]}
        return final
    except:
        return None

