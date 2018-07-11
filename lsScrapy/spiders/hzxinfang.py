import scrapy
import re
import datetime

class HZxinFanf(scrapy.Spider):
    name="hzxinfang"
    start_urls = [
        "https://hz.fang.lianjia.com/loupan/pg1/",
    ]

    def parse(self, response):
        print(response)
        houses = response.xpath(".//ul[@class='resblock-list-wrapper']/li")
        for house in houses:
            region = house.xpath(".//div[@class='resblock-location']/span/text()")[0].extract(),  # 所属的行政区
            bankuai = house.xpath(".//div[@class='resblock-location']/span/text()")[1].extract(),  # 所属的地产板块
            street = house.xpath(".//div[@class='resblock-location']/a/text()").extract(),  # 所属的街道
            house_detail_url = house.xpath(".//a[@class='resblock-img-wrapper']/@href").extract(),  # 房子详情页URL
            unit_price = house.xpath(".//div[@class='main-price']/span[@class='number']/text()").extract(),  # 平米单价
            total_price = house.xpath(".//div[@class='resblock-price']/div[@class='second']/text()").re("\d+.\d+"),  # 总价
            name = house.xpath(".//div[@class='resblock-name']/a/text()").extract(),  # 小区名称
            area = house.xpath(".//div[@class='resblock-area']/span/text()").re("\d+.\d+"),  # 面积
            type = house.xpath(".//div[@class='resblock-name']/span[@class='resblock-type']/text()").extract(),  # 类型
            feature = house.xpath(".//div[@class='resblock-tag']/span/text()").extract(),  # 特色标签




            yield {
                'current_url':response.url,   #当前请求的URL
                'current_time':datetime.datetime.now().strftime('%Y-%m-%d'),#当前日期
                'region': region,
                'bankuai': bankuai,
                'street': street,
                'house_detail_url': house_detail_url,
                'unit_price': unit_price,
                'total_price': total_price,
                'name': name,
                'area': area,
                'type': type,
                'feature': feature,
            }



        page = response.xpath("//div[@class='page-box'][@data-current]").re("\d+")  # 当前页码[1,700]
        total_num = page[1]
        #n_page = "https://hz.fang.lianjia.com/loupan/pg"   #有规律的下一页https://hz.fang.lianjia.com/loupan/pg1
        p1 = re.compile(r'[^\d]+')  #获取URL的公共前缀
        current_num = re.findall(r"\d+",response.url)[0]
        if  current_num != total_num:
            next_page = p1.match(response.url).group() + str(int(current_num) + 1)  # 在当前页的基础上加1
            print(next_page + "****************************************************************")
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)  # 递归请求



