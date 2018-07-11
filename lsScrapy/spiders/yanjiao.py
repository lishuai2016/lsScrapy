# -*- coding: utf-8 -*-
import scrapy
import re

class ershoufangSpider(scrapy.Spider):
    name = "yanjiao"
    # start_urls = ["http://bj.lianjia.com/ershoufang/dongcheng/pg1", "http://bj.lianjia.com/ershoufang/xicheng/pg1", "http://bj.lianjia.com/ershoufang/chaoyang/pg1", "http://bj.lianjia.com/ershoufang/haidian/pg1", "http://bj.lianjia.com/ershoufang/fengtai/pg1", "http://bj.lianjia.com/ershoufang/shijingshan/pg1", "http://bj.lianjia.com/ershoufang/tongzhou/pg1", "http://bj.lianjia.com/ershoufang/changping/pg1", "http://bj.lianjia.com/ershoufang/daxing/pg1", "http://bj.lianjia.com/ershoufang/yizhuangkaifaqu/pg1", "http://bj.lianjia.com/ershoufang/shunyi/pg1", "http://bj.lianjia.com/ershoufang/fangshan/pg1", "http://bj.lianjia.com/ershoufang/mentougou/pg1", "http://bj.lianjia.com/ershoufang/pinggu/pg1", "http://bj.lianjia.com/ershoufang/huairou/pg1", "http://bj.lianjia.com/ershoufang/miyun/pg1", "http://bj.lianjia.com/ershoufang/yanqing/pg1", "http://bj.lianjia.com/ershoufang/yanjiao/pg1"]
    start_urls = ["https://lf.lianjia.com/ershoufang/yanjiao/pg1"]
    def parse(self, response):
        houses = response.xpath(".//ul[@class='sellListContent']/li")   #所有ul中class=sellListContent下的li列表
        for house in houses:
            # attention = ''  #关注的数量
            # visited = ''   #看房的次数
            # publishday = ''  #看房的时间
            # try:      #   39人关注 / 共8次带看 / 6天以前发布
            #     attention = house.xpath(".//div[@class='followInfo']/text()").re("\d+")[0] #第一个匹配的字符串    39
            #     visited = house.xpath(".//div[@class='followInfo']/text()").re("\d+")[1] #第二个匹配的字符串     8
            #     if u'月' in house.xpath(".//div[@class='followInfo']/text()").extract()[0].split('/')[2]:   #6天以前发布
            #         number = house.xpath(".//div[@class='followInfo']/text()").re("\d+")[2]
            #         publishday = int(number)*30
            #
            #     elif u'年' in house.xpath(".//div[@class='followInfo']/text()").extract()[0].split('/')[2]:
            #         number = house.xpath(".//div[@class='followInfo']/text()").re("\d+")[2]
            #         publishday = 365
            #     else:
            #         publishday = house.xpath(".//div[@class='followInfo']/text()").re("\d+")[2]
            # except:
            #     print("These are some ecxeptions")
            # else:
            #     pass
            page = response.xpath("//div[@class='page-box house-lst-page-box'][@page-data]").re("\d+")

            yield {
                # 'region': house.xpath(".//div[@class='houseInfo']/a/text()").extract(), #提取房子的位置信息
                # 'url':house.xpath(".//a[@class='img ']/@href").extract(),  #图片上的URL，跳转到情页
                # 'houseInfo':house.xpath(".//div[@class='houseInfo']/text()").extract(), #房子信息
                # 'unitPrice':house.xpath(".//div[@class='unitPrice']/span").re("\d+.\d+"),#  平米单价
                # 'totalPrice':house.xpath(".//div[@class='totalPrice']/span").re("\d+.\d+"),#总价格
                # 'attention': attention,
                # 'visited': visited,
                # 'publishday': publishday
                "page":page  #['62', '1']

            }
        page = response.xpath("//div[@class='page-box house-lst-page-box'][@page-data]").re("\d+")  #获得page-data的数字内容 ，返回一个list
        p = re.compile(r'[^\d]+')  #匹配所有的非数字字符
        if len(page)>1 and page[0] != page[1]:
            print(p.match(response.url).group())   #https://lf.lianjia.com/ershoufang/yanjiao/pg
            next_page = p.match(response.url).group()+str(int(page[1])+1)  #在当前页的基础上加1
            print(next_page+"****************************************************************")
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)  #递归请求
