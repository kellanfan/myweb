#coding=utf8
"""
# Author: Kellan Fan
# Created Time : Fri 29 Jan 2021 01:22:44 PM CST

# File Name: doublecolorball.py
# Description:

"""
import random
from app.common.pg_client import Mypostgres
from collections import Counter
from flask_restful import Resource, abort

ACTION_BALL_LIST = ['random', 'count']

class DoubleColorBall(Resource):
    def get(self, action):
        if action not in ACTION_BALL_LIST:
            abort(404, message="Action [{}] doesn't exist".format(action))
        if action == 'random':
            return handle_random_ball()
        elif action == 'count':
            return handle_count_ball()

def handle_random_ball():
    red = []
    for _ in range(0,10000):
        red += sorted(random.sample(list(range(1,34)), 6))
    red_num_counts = Counter(red)
    
    true_red = []
    for item in red_num_counts.most_common(6):
        true_red.append(item[0])

    blue = []
    for _ in range(0,10000):
        blue.append(random.randint(1,17))
    blue_num_counts = Counter(blue)
    true_blue = blue_num_counts.most_common(1)[0][0]

    return {
          "red_ball": sorted(true_red),
          "blue_ball": true_blue
        }


def __red_ball(pg_conn):
    sql_command1 = "select r_number from shuang_se_qiu" 
    ret = pg_conn.execute(sql_command1)
    red = []
    for item in ret:
        red += item[0].strip().split(',')
    red_num_counts = Counter(red)
    true_red = []
    for item in red_num_counts.most_common(6):
        true_red.append(item[0])
    return sorted(true_red)

def __blue_ball(pg_conn):
    blue = []
    sql_command2 = "select b_number from shuang_se_qiu" 
    ret = pg_conn.execute(sql_command2)
    for item in ret:
        blue.append(item[0].strip())
    blue_num_counts = Counter(blue)
    return blue_num_counts.most_common(1)[0][0]

def handle_count_ball():
    pg_conn = Mypostgres()
    try:
        return {
                  "red_ball": __red_ball(pg_conn), 
                  "blue_ball": __blue_ball(pg_conn)
               }
    except:
        return None

