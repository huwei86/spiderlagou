# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from LaGou.items import LagouItem
from LaGou.utils.MD5 import get_md5
from datetime import datetime


class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    start_urls = ['https://www.lagou.com/zhaopin/']
    content_links=LinkExtractor(allow=(r"https://www.lagou.com/jobs/\d+.html"))
    page_links=LinkExtractor(allow=(r"https://www.lagou.com/zhaopin/\d+"))
    rules = (
        Rule(content_links, callback="parse_item", follow=False),
        Rule(page_links,follow=True)
    )

    def parse_item(self, response):
        item=LagouItem()
        #获取到公司拉钩主页的url作为ID
        item["obj_id"]=get_md5(response.url)
        #公司名称
        item["company_name"]=response.xpath('//dl[@class="job_company"]//a/img/@alt').extract()[0]
        # 职位
        item["positon_name"]=response.xpath('//div[@class="job-name"]//span[@class="name"]/text()').extract()[0]
        #工资
        item["salary"]=response.xpath('//dd[@class="job_request"]//span[1]/text()').extract()[0]
        # 工作地点
        work_place=response.xpath('//dd[@class="job_request"]//span[2]/text()').extract()[0]
        item["work_place"]=work_place.replace("/","")
        # 工作经验
        work_experience=response.xpath('//dd[@class="job_request"]//span[3]/text()').extract()[0]
        item["work_experience"]=work_experience.replace("/","")
        # 学历
        education=response.xpath('//dd[@class="job_request"]//span[4]/text()').extract()[0]
        item["education"]=education.replace("/","")
        # full_time
        item['full_time']=response.xpath('//dd[@class="job_request"]//span[5]/text()').extract()[0]
        #tags
        tags=response.xpath('//dd[@class="job_request"]//li[@class="labels"]/text()').extract()
        item["tags"]=",".join(tags)
        #publish_time
        item["publish_time"]=response.xpath('//dd[@class="job_request"]//p[@class="publish_time"]/text()').extract()[0]
        # 职位诱惑
        job_temptation=response.xpath('//dd[@class="job-advantage"]/p/text()').extract()
        item["job_temptation"]=",".join(job_temptation)
        # 工作描述
        job_desc=response.xpath('//dd[@class="job_bt"]/div//p/text()').extract()
        item["job_desc"]=",".join(job_desc).replace("\xa0","").strip()
        #job_publisher
        item["job_publisher"]=response.xpath('//div[@class="publisher_name"]//span[@class="name"]/text()').extract()[0]
        # 公司logo地址
        logo_image=response.xpath('//dl[@class="job_company"]//a/img/@src').extract()[0]
        item["logo_image"]=logo_image.replace("//","")
        # 领域
        field=response.xpath('//ul[@class="c_feature"]//li[1]/text()').extract()
        item["field"]="".join(field).strip()
        # 发展阶段
        stage=response.xpath('//ul[@class="c_feature"]//li[2]/text()').extract()
        item["stage"]="".join(stage).strip()
        # 投资机构
        financeOrg=response.xpath('//ul[@class="c_feature"]//li[3]/p/text()').extract()
        if financeOrg:
            item["financeOrg"]="".join(financeOrg)
        else:
            item["financeOrg"]=""
        #公司规模
        if financeOrg:
             company_size= response.xpath('//ul[@class="c_feature"]//li[4]/text()').extract()
             item["company_size"]="".join(company_size).strip()
        else:
            company_size = response.xpath('//ul[@class="c_feature"]//li[3]/text()').extract()
            item["company_size"] = "".join(company_size).strip()
        # 公司主页
        item["home"]=response.xpath('//ul[@class="c_feature"]//li/a/@href').extract()[0]
        # 爬取时间
        item["crawl_time"]=datetime.now()

        yield item
