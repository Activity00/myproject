#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/4/26 下午5:48
# @Author  : 武明辉
# @File    : aaa.py
import scrapy
from selenium import webdriver
import time
# dr = webdriver.Firefox()
# time.sleep(1)
# print 'Browser will close.'
# dr.quit()
# print 'Browser is close'
def aaa():
    for i in range(10):
        yield i
        yield i+10

for i in aaa():
    print i
