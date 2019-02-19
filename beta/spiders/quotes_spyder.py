import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://vcdepth.io/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('vue-main-table'):
            yield {
                'teste': quote.css('vue-main-table').attrib[':coins']
            }
