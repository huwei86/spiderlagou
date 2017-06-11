# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class LagouPipeline(object):

    def process_item(self, item, spider):
        con = pymysql.connect(host="127.0.0.1", user="root", passwd="229801", db="lagou",charset="utf8")
        cur = con.cursor()
        sql = ("insert into lagouwang(obj_id,company_name,positon_name,salary,work_place,work_experience,education,full_time,tags,publish_time,job_temptation,job_desc,job_publisher,logo_image,field,stage,financeOrg,company_size,home,crawl_time)"
               "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        lis=(item["obj_id"],item["company_name"],item["positon_name"],item["salary"],item["work_place"],item["work_experience"],item["education"],item['full_time'],item["tags"],item["publish_time"],item["job_temptation"],item["job_desc"],item["job_publisher"],item["logo_image"],item["field"],item["stage"],item["financeOrg"],item["company_size"],item["home"],item["crawl_time"])
        cur.execute(sql, lis)
        con.commit()
        cur.close()
        con.close()

        return item
