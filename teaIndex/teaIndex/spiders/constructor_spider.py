import scrapy


class QuotesSpider(scrapy.Spider):
    name = "constructor"
    start_urls = [
        'https://theconstructor.org/',

    ]

    for i in range (2,277):
        start_urls.append('https://theconstructor.org/page/' + str(i) +'/')

    def parse(self, response):
        for article in  response.css('div.post-inner' ):
            yield {
                'title': article.css('div.post-inner ::text').extract()[1],
                'text':  article.css('div.post-inner ::text').extract()[8],
                'link': article.css('div.post-content a::attr(href)').extract()[0],
            }

#follow pagination link