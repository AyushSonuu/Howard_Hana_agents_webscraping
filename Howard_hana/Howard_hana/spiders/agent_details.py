import scrapy


class AgentDetailsSpider(scrapy.Spider):
    name = 'agent_details'
    allowed_domains = ['www.howardhanna.com']
    # start_urls = ['http://www.howardhanna.com/']
    def start_requests(self):
        zip_codes = ["14072","16505","23462","28025","10605",'17601']
        for zip in zip_codes:
            url = f"https://www.howardhanna.com/Agent/List?Location={zip}&PageSize=50&Page=1"
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        pass
