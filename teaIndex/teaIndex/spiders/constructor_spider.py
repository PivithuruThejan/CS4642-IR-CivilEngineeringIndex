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
            link = article.css('div.post-content a::attr(href)').extract()[0]
            #yield {
                #'title': article.css('div.post-inner ::text').extract()[1],
                #'text':  article.css('div.post-inner ::text').extract()[8],
                #'link': article.css('div.post-content a::attr(href)').extract()[0],
            #}

            yield scrapy.Request(url = link, callback =self.parse2)

#follow pagination link
    def parse2(self, response):
        title = response.css('div.post-inner')
        for line in response.css('div.post-content'):
            yield {
                'title':title.css('span.entry-title ::text').extract(),
                'headings': line.css('h2 ::text').extract(),
                'sub headings': line.css('h3 ::text').extract(),
                'text': line.css('p ::text').extract(),


            }