import json

from ruten import Ruten


class Crawler:

    def __init__(self,url, page):
        self.url = url
        self.page = page + 1
        self.fare = Ruten(url=self.url).fare

    def return_best_goods(self):
        best_goods_list = []
        for page in range(1, self.page):
            ruten = Ruten(url=self.url + '&p={}'.format(self.page))
            best_goods_list.append(ruten.return_best_good())
        return json.dumps(best_goods_list,ensure_ascii=False)

    def return_normal_goods(self):
        normal_goods_list = []
        for page in range(1, self.page):
            ruten = Ruten(url=self.url + '&p={}'.format(self.page))
            normal_goods_list.append(ruten.return_normal_good())
        return json.dumps(normal_goods_list, ensure_ascii=False)


    def return_fare(self):
        return self.fare


