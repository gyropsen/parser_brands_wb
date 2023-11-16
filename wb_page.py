import requests
import re


class ParceWB:
    def __str__(self):
        return "Экземпляр класса, в котором есть url и brand"

    def __repr__(self):
        return f"ParceWB({self.url})"

    def __init__(self, url):
        """
        Инициализатор экземпляра класса
        """
        self.url = url
        self.brand = ""

    def find_brand(self):
        """
        Ищем имя бренда
        """
        brand = re.search('(?<=brands/).*', self.url)
        self.brand = brand[0]
        return self.brand

    def get_brand(self):
        """
        Отправляем запрос для получения id брэнда и его name
        """
        response_brand = requests.get(f'https://static-basket-01.wb.ru/vol0/data/brands/{self.find_brand()}.json')
        response_brand = response_brand.json()
        brand_id, brand_name = response_brand["id"], response_brand["name"]
        return brand_id, brand_name

    def get_data(self, word, count):
        """
        Подставляем id брэнда, и получаем данные
        """
        response = requests.get(
            f'https://catalog.wb.ru/brands/{word}/catalog?TestGroup=test_group_q10_60&TestID=317&appType=1'
            f'&brand={self.get_brand()[0]}&curr=rub&dest=-1257786&page={count}'
            f'&regions=80,83,38,4,64,33,68,70,30,40,86,75,69,1,66,110,22,48,31,71,112,114'
            f'&sort=popular&spp=29')
        return response
