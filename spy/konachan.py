#coding=utf-8
import urllib
import urllib2
import codecs
import lxml
import os

import sys
from lxml import etree


def get_html(string):

    url=string
    req =  urllib2.Request(url)
    #print req
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    #print res
    return res


def getimgurl():
    url = "http://konachan.net/post"
    baseurl = "http://konachan.net"
    imglist = []
    fullimglist = []

    selector = etree.HTML(get_html(url))
    con = selector.xpath('/html/body/div[7]/div[1]/div[3]/div[4]/ul/li[*]/a')

    for loop, url  in zip(range(len(con)), con):
         # fullimglist.append(url.attrib["href"])
         imgtype = ".jpg"
         imgname = str(loop) + imgtype

         download_img(url.attrib["href"], imgname)


def download_img(img_url,img_name):
    filename = "./img/"+img_name
    res2 = urllib.urlretrieve(img_url, filename)

getimgurl()




