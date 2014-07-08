from scrapy.spider import Spider
from scrapy.selector import Selector
from restaurants.items import RestaurantsItem

class MySpider(Spider):
    name = "rider"
    allowed_domains = ["restaurant.com"]
    start_urls = [
    "http://www.restaurant.com/city-cuisine/chicago-restaurants"]

    def parse(self, response):
        hxs = Selector(response)
        titles = hxs.xpath("//div[@class='cityLink']/div/div")
        items = []
        for titles in titles:
            item = RestaurantsItem()
            item["title"] = titles.xpath("a/text()").extract()
            item["link"] = titles.xpath("a/@href").extract()
            item["rating"] = titles.xpath("div[@class='ratingsReviews']\
            /span[@class='ratings']/span[@class='rating']/text()").extract()
            item["address"] = titles.xpath("div[@class='address']/text()").extract()
            if len(item["title"])>0:
                items.append(item)
        return items

