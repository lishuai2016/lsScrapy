# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql
from lsScrapy import settings

#在这个pipeline文件中可以定义多个存储数据的class类，然后再setting文件中添加一行，如
# ITEM_PIPELINES = {
#    'lsScrapy.pipelines.LocalJsonPipeline': 300,  #本地json文件存储数据
#    # 'lsScrapy.pipelines.DBPipeline': 1,        #把数据保存到MySQL数据库
# }


class LocalJsonPipeline(object):
    def __init__(self):
        # 打开文件
        self.file = open('hzxinfang.json', 'w', encoding='utf-8')   #在当前目录下生成json文件

    # 该方法用于处理数据
    def process_item(self, item, spider):
        # file = open("E:\\spidersitems.txt", "a")
        # # 以追加的方式打开文件，不存在则创建
        # # 因为item中的数据是unicode编码的，为了在控制台中查看数据的有效性和保存，
        # # 将其编码改为utf-8
        # #item_string = str(item).decode("unicode_escape").encode('utf-8')
        # file.write(item)
        # file.write('\n')
        # file.close()
        # print(item)# 在控制台输出

        # 读取item中的数据
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        # 写入文件
        self.file.write(line)

        return item


    # 该方法在spider被开启时被调用。
    def open_spider(self, spider):
        pass

    # 该方法在spider被关闭时被调用。
    def close_spider(self, spider):
        self.file.close()


# 用于MySQL数据库存储
class DBPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            port=3306,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor();

    def process_item(self, item, spider):
        try:
            # 查重处理
            # self.cursor.execute(
            #     """select * from test.quotes where img_url = %s""",
            #     item['img_url'])
            # # 是否有重复数据
            # repetition = self.cursor.fetchone()
            #
            # # 重复
            # if repetition:
            #     pass
            #
            # else:
            #     # 插入数据
            #     self.cursor.execute(
            #         """insert into test.quotes(text, author) value (%s, %s)""",
            #         (item['text'],
            #          item['author']))

            # 插入数据
            self.cursor.execute(
                    """insert into test.quotes(text, author) value (%s, %s)""",
                    (item['text'],
                     item['author']))
            # 提交sql语句
            self.connect.commit()

        except Exception as error:
            # 出现错误时打印错误日志
            print(error)
        return item