import requests

from pyquery import PyQuery as pq



class Ruten:
    sales_items = []

    normal_items = []
    headers = requests.utils.default_headers()
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'

    def __init__(self, url):
        self.url = url
        try:
            res = requests.get(self.url,headers=self.headers)
            self.page_soruce = res.content
            self.doc = pq(self.page_soruce)
            self.fare = self.return_fare()
        except Exception as e:
            print(str(e))



    def return_normal_good(self):
        '''
        返回一般商品
        :return:
        '''
        titles = self.doc('div.rt-store-goods-listing h3 a')
        img_urls = self.doc('img[class=rt-product-image]')
        for index, item in enumerate(titles):

            self.normal_items.append({'title': item.text, 'img_url': img_urls[index].attrib['src'], 'type': 'normal'})
        return self.normal_items


    def return_best_good(self):
        '''
        返回 精選商品
        :return:
        '''
        titles = self.doc('div[class=best-goods-col] li[class=item-name]  a')
        img_urls = self.doc('a[class=item-img-wrapper] img')

        for index, item in enumerate(titles):
            self.sales_items.append({'title': item.text, 'img_url': img_urls[index].attrib['src'],'type': 'sales'})
        return self.sales_items

    def return_fare(self):
        '''
        返回運費
        :return:
        '''
        about_me_url = self.doc('a:Contains("關於我")')[0].attrib['href']

        res = requests.get(about_me_url, headers=self.headers)
        doc = pq(res.content)
        fare_texts = doc('span[class=pway-text]:Contains("元")')
        fares = doc('span[class=shipping-fee]')
        fares_list = []
        for index, fare_text in enumerate(fare_texts):
            fares_list.append({'fare_type': fare_text.text.replace('\n','').replace(' ',''), 'fare':fares[index].text.strip('\t\n\r')})
        return fares_list







