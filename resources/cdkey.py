#coding=utf8
"""
# Author: Kellan Fan
# Created Time : Fri 29 Jan 2021 01:30:45 PM CST

# File Name: cdkey.py
# Description:

"""
import random
import string
from flask_restful import Resource

class CDKey(Resource):
    def get(self):
        return handle_cdkey()

def handle_cdkey():
    return { "cdkey": ''.join(random.sample(string.ascii_letters + string.digits, 16)) }
