import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://www.babelio.com/auteur/Amin-Maalouf/4638/citations',
    ]

    def parse(self, response):
        for quote in response.css('div.post_con'):
            yield {
                'Auteur': quote.css('a.libelle::text').get(),
                'Titre': quote.css('a.titre1::text').get(),
                'Citation': quote.css('div.text.row div::text').get(),
            }

        next_page = response.css('a.fleche.icon-next::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
