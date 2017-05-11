# -*- coding: utf-8 -*-
# @Time    : 17/4/24 下午5:52
# @Author  : 武明辉
# @File    : cmdline.py

import scrapy.cmdline

if __name__ == '__main__':
    #三月份新榜的数据
    #scrapy.cmdline.execute(['scrapy', 'crawl', 'weixin_xb'])
    #scrapy.cmdline.execute(['scrapy', 'crawl', 'test'])
    scrapy.cmdline.execute(['scrapy', 'crawl', 'sgwx'])

    #测试传入参数
    start_time = '2017-03-31'
    end_time = '2017-03-01'
    cmdstr = 'scrapy crawl test1 -a start_time=%s -a end_time=%s'%(start_time, end_time)
    #scrapy.cmdline.execute(cmdstr.split())
