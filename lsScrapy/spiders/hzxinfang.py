import scrapy
import re

class HZxinFanf(scrapy.Spider):
    name="hzxinfang"
    start_urls = [
        "https://hz.fang.lianjia.com/loupan/rs/",
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
            feature = house.xpath(".//div[@class='resblock-tag']/span/text()").extract()  # 特色标签

            yield {
                'region': region,
                'bankuai': bankuai,
                'street': street,
                'house_detail_url': house_detail_url,
                'unit_price': unit_price,
                'total_price': total_price,
                'name': name,
                'area': area,
                'type': type,
                'feature': feature
            }

        page = response.xpath("//div[@class='page-box'][@data-page]").re("\d+")  # 获得data-page的数字内容 ，返回一个list
        p = re.compile(r'[^\d]+')
        if len(page) > 1 and page[0] != page[1]:
            next_page = p.match(response.url).group() + str(int(page[1]) + 1)  # 在当前页的基础上加1
            print(next_page + "****************************************************************")
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)  # 递归请求



