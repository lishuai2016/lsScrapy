from scrapy.selector import Selector
from scrapy.http import HtmlResponse

#以文字构造：
# body = '<html><body><span>good</span></body></html>'
# print(Selector(text=body).xpath('.//span/text()').extract())


body1 =  '''
<html>
 <head>
  <base href='http://example.com/' />
  <title>Example website</title>
 </head>
 <body>
  <div id='images'>
   <a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' /></a>
   <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' /></a>
   <a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' /></a>
   <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' /></a>
   <a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' /></a>
  </div>
 </body>
</html>
'''

#以 response 构造：
response = HtmlResponse(url='http://example.com', body=body1.encode('utf-8'))
# print(response.selector.xpath('//span/text()').extract())
# print(response.xpath('//span/text()').extract())   #等价于上面的那种写法，和scrapy架构写法一致
# title = response.xpath('//title/text()').extract()
# print(title)
list = response.xpath('//div/a').extract()
for a in list:
    print(a.xpath('//a/text()').extract())
print(type(list))




#.xpath() 及 .css() 方法返回一个类 SelectorList 的实例, 它是一个新选择器的列表。
# print(response.xpath('//title/text()'))  #Selector对象  [<Selector xpath='//title/text()' data='Example website'>]
# print(response.xpath('//title/text()').extract()) #['Example website']
# print(response.xpath('//title/text()').extract_first()) #  Example website
#
# print(response.css('title::text'))  #[<Selector xpath='descendant-or-self::title/text()' data='Example website'>]
# print(response.css('title::text').extract())
#
# print(response.xpath('//base/@href').extract())  #['http://example.com/']
# print(response.css('base::attr(href)').extract())
#
# print(response.xpath('//a[contains(@href, "image")]/@href').extract()) #['image1.html', 'image2.html', 'image3.html', 'image4.html', 'image5.html']
# print(response.css('a[href*=image]::attr(href)').extract())
#
# print(response.xpath('//a[contains(@href, "image")]/img/@src').extract()) #['image1_thumb.jpg', 'image2_thumb.jpg', 'image3_thumb.jpg', 'image4_thumb.jpg', 'image5_thumb.jpg']
# print(response.css('a[href*=image] img::attr(src)').extract())
