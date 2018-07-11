import scrapy
import re


class HzXinFangDetail(scrapy.Spider):
    print(111)



    def parse(self, response):
        yield {
            # 详情页字段
            'nearest_update_time': "",  # 最近更新时间
            'visited': "",  # 看房次数
            'deal_number': "",  # 成交量
            'developers': "",  # 开发商
            'open_time': '',  # 开盘时间
            'delivery_time': '',  # 交付时间
            'tenement': "",  # 物业
            'tenement_type': "",  # 物业类型
            'property_time': "",  # 产权年限
            'plot_ratio': "",  # 容积率
            'open_time': '',  # 绿化率
            'planning_number': '',  # 规划户数

            'tenement_price': "",  # 物业费用
            'carport': '',  # 车位情况
            'supply_heating': '',  # 供暖方式
            'supply_water': "",  # 供水方式
            'supply_electricity': "",  # 供电方式
            'building_types': "",  # 建筑类型
            # 嫌恶设施(嫌恶设施基本可分为两大类：1.对生命造成威胁的：加油站：高压电站：飞机场：2.对居家生活舒适度产生干扰的：a.高架桥b.工厂c.焚烧垃圾场)
            'bad_facility': "",
            'floor_area': '',  # 占地面积
            'building_number': '',  # 建筑面积
        }