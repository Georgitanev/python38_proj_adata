import scrapy
from scrapy.selector import Selector


class QuotesSpider(scrapy.Spider):
    name = "parliament_all"
    start_urls = [
        "https://parliament.bg/bg/MP",
    ]

    def parse(self, response):
        selector = Selector(response)
        urls_short = selector.xpath("//div[3]/div/div/div/a/@href").getall()
        start_urls = ["https://www.parliament.bg" + short for short in
                      urls_short]
        yield {
            "urls": start_urls,
        }
