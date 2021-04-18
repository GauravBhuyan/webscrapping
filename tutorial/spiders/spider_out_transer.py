import scrapy

urli = []
class ScrapeTransferTable(scrapy.Spider):
    name = "scrape-transfer-out"
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
        for row in response.xpath('//*[@class="table table-striped table-bordered"]//tbody//tr'):
            yield {
                'name_out' : row.xpath('td[1]/a/text()').extract_first(),
				'name_out_no_link' : row.xpath('td[1]//text()').extract_first(),
				'club_out': row.xpath('td[2]//text()').extract_first(),
                'fee_out_link' : row.xpath('td[3]/a/text()').extract_first(),
				'fee_out' : row.xpath('td[3]//text()').extract_first(),
				'date_out' : row.xpath('td[4]//text()').extract_first(),
            }

