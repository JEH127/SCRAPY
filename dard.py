import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://www.babelio.com/auteur/Frederic-Dard/7187/citations',
    ]

    def parse(self, response):
        for quote in response.css('div.post_con'):
            yield {
                'Auteur': quote.css('a.libelle::text').get(),
                'Citation': quote.css('div.text.row div::text').get(),

                # si pas de'.'devant //div => affiche que le 1er auteur
                # 'Auteur': quote.xpath('.//div[@class="text row"]/a[@class="libelle"]/text()').get(),
                # 'Citation': quote.xpath('.//div[@class="text row"]/div/text()').get(),

            }

        next_page = response.css(
            'div.pagination.row a.fleche.icon-next::attr("href")').get()

        if next_page is not None:
            yield response.follow(next_page, self.parse)
