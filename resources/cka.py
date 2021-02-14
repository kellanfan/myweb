#coding=utf8
"""
# Author: Kellan Fan
# Created Time : Wed 10 Feb 2021 09:25:52 PM CST

# File Name: cka.py
# Description:

"""

# here put the import lib
import yaml
import platform
from pathlib import Path
from app.common.openurl import OpenUrl
from lxml import etree
from flask_restful import Resource

class Cka(Resource):
    def get(self):
        current_price = get_price()
        if comp(current_price):
            return { "msg": "Current price is [{}]!".format(current_price) }
        else:
            return { "msg": "The price not changed" }

def get_price():
    ourl = OpenUrl('https://training.linuxfoundation.cn/certificate/details/1')
    code,html = ourl.run()
    if code==200:
        selecter = etree.HTML(html)
        try:
            tmp = str(selecter.xpath('//span[@class="text-red mr-2 text-sm"]/text()')[0])

            return int(float(tmp.replace(',','')))
        except:
            return None

def comp(current_price):
    stand_price = 2088
    if current_price:
        if current_price < stand_price:
            return True
    return False
