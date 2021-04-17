import scrapy

urli = []
class ScrapeTransferTable(scrapy.Spider):
    name = "scrape-transfer"
    start_urls = [
        'https://www.lfchistory.net/Transfers/BySeason/122',
    ]
    def start_requests(self):
        for i in range(1,130):
            url_link = "https://www.lfchistory.net/Transfers/BySeason/" + str(i)
            urli.append(url_link)
        
        for url in urli:
            yield scrapy.Request(url=url, callback=self.parse)
			
    def parse(self, response):
        for row in response.xpath('//*[@class="table table-striped table-bordered layout_fixed lf-primary_table"]//tbody//tr'):
            yield {
                'name' : row.xpath('td[1]/a/text()').extract_first(),
                'club': row.xpath('td[2]//text()').extract_first(),
                'fee' : row.xpath('td[3]//text()').extract_first(),
				'date' : row.xpath('td[4]//text()').extract_first(),
            }

