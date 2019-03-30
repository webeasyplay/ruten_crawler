
from Crawer import Crawler


if __name__ == '__main__':
    crawler = Crawler(url='https://class.ruten.com.tw/user/index00.php?s=hambergurs&fbclid=IwAR0DSgqeqHGiWd8BIU5YA-GUJ1qZFvesZ5KNUQw57fJ_LCyn8T_NCQYbtLM',
                      page=3)
    best_good = crawler.return_best_goods()
    fare = crawler.return_fare()
    normal_good = crawler.return_normal_goods()
    print(best_good)
    print(fare)
    print(normal_good)


