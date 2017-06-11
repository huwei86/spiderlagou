# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class LagouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #id
    obj_id=scrapy.Field()
    #职位名
    positon_name=scrapy.Field()
    #工作地点
    work_place=scrapy.Field()
    #发布日期
    publish_time=scrapy.Field()
    #工资
    salary=scrapy.Field()
    #工作经验
    work_experience=scrapy.Field()
    #学历
    education=scrapy.Field()
    #full_time
    full_time=scrapy.Field()
    #标签
    tags=scrapy.Field()
    #公司名字
    company_name=scrapy.Field()
    # #产业
    # industry=scrapy.Field()
    #职位诱惑
    job_temptation=scrapy.Field()
    #工作描述
    job_desc=scrapy.Field()
    #公司logo地址
    logo_image=scrapy.Field()
     #领域
    field=scrapy.Field()
    #发展阶段
    stage=scrapy.Field()
    #公司规模
    company_size=scrapy.Field()
    # 公司主页
    home = scrapy.Field()
    #职位发布者
    job_publisher=scrapy.Field()
    #投资机构
    financeOrg=scrapy.Field()
    #爬取时间
    crawl_time=scrapy.Field()

