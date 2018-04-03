import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://pokemondb.net/pokedex/bulbasaur'.
        ]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        products = response.xpath('//*[@id="svtabs_moves_16"]/div[1]/div[1]/div[1]/table/tbody//tr')
    # ignore the table header row
        for product in products[1:]:
            
            item = Schooldates1Item()
            item['level'] = product.c.xpath('//*[@id="svtabs_moves_16"]/div[1]/div[1]/div[1]/table/tbody/tr[1]/td[1]//text()').extract_first()
            item['move'] = product.c.xpath('//*[@id="svtabs_moves_16"]/div[1]/div[1]/div[1]/table/tbody/tr[1]/td[2]//text()').extract_first()
            item['type'] = product.c.xpath('//*[@id="svtabs_moves_16"]/div[1]/div[1]/div[1]/table/tbody/tr[1]/td[3]//text()').extract_first()
            item['category'] = product.c.xpath('//*[@id="svtabs_moves_16"]/div[1]/div[1]/div[1]/table/tbody/tr[1]/td[4]//text()').extract_first()
            item['power'] = product.c.xpath('//*[@id="svtabs_moves_16"]/div[1]/div[1]/div[1]/table/tbody/tr[1]/td[5]//text()').extract_first()
            item['level'] = product.c.xpath('//*[@id="svtabs_moves_16"]/div[1]/div[1]/div[1]/table/tbody/tr[1]/td[6]//text()').extract_first()
            yield item