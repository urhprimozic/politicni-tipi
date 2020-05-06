import scrapy

class Pajek_po_mladini(scrapy.Spider):
    name = 'Pajek_po_mladini'
    start_urls = ['https://www.mladina.si/']

    def parse(self, response):
        for quote in response.css('li.item.bigger'):
            yield {
                #'author': quote.xpath('p.h2/a').get(),
                'text': quote.css('p').get(),
               # 'text2': quote.css('p/text()').get(),
            }

        next_page = None# response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

   