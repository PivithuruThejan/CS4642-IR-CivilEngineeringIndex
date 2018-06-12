import scrapy


class TeaSpider(scrapy.Spider):
    name = "tea"
    start_urls = [
        'http://www.pureceylontea.com/',
    ]

    def parse(self, response):
        for tea in response.css('div.sprocket-features-content'):
            yield {
                'link': tea.css('h2.sprocket-features-title a::attr(href)').extract_first(),

            }
        #for tea in response.css('div.sltb_common_para'):
            #yield {
                #'text': tea.css('::text').extract_first(),

            #}
        #for tea in response.css('div'):
            #yield {
                #'text': tea.css('::text').extract_first(),

            #}