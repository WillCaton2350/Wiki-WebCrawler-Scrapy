from scrapy import Spider
from wikiCrawler.items import WikicrawlerItem

class wikipediaSpider(Spider):
    name = 'wikipediaCrawler'
    start_urls = [
        "https://en.wikipedia.org/wiki/Sphinx_of_Memphis",
        "https://en.wikipedia.org/wiki/Sphinx_of_Taharqo",
        "https://en.wikipedia.org/wiki/Statues_of_Amun_in_the_form_of_a_ram_protecting_King_Taharqa"
    ]
    def parse(self,response):
        webItem = WikicrawlerItem()
        webItem['id'] = None
        webItem['url'] = response.url
        webItem['title'] = None
        webItem['summary'] = None
        webItem['discovery'] = None
        webItem['composition'] = None
        webItem['physical_attributes'] = None
        webItem['other_information'] = None
        webItem['title_two'] = None
        webItem['summary_two'] = None
        webItem['taharqo'] = None
        webItem['the_statue'] = None
        webItem['title_three'] = None
        webItem['summary_three'] = None
        webItem['the_british_museum_state'] = None
        webItem['the_ashmolean_state'] = None
        if response.url == "https://en.wikipedia.org/wiki/Sphinx_of_Memphis":
                
                webItem['title'] = response.css('.mw-page-title-main::text').getall()
                webItem['summary'
                        ] = response.css('.mw-parser-output > p:nth-child(3)::text').getall()
                webItem['discovery'
                        ] = response.css('.mw-parser-output > p:nth-child(6)::text').getall()
                webItem['composition'
                        ] = ''.join(response.css('.mw-parser-output > p:nth-child(8)::text').getall()).strip()
                webItem['physical_attributes'
                        ] = response.css('.mw-parser-output > p:nth-child(10)::text').getall()
                webItem['other_information'
                        ] = response.css('.mw-parser-output > p:nth-child(12)::text').getall()
        elif response.url == "https://en.wikipedia.org/wiki/Sphinx_of_Taharqo":
                webItem['title_two'] = response.css('.mw-page-title-main::text').getall()
                webItem['summary_two'
                        ] = response.css('.mw-parser-output > p:nth-child(5)::text').getall()
                webItem['taharqo'
                        ] = response.css('.mw-parser-output > p:nth-child(8)::text').getall()
                webItem['the_statue'
                        ] = response.css('.mw-parser-output > p:nth-child(11)::text').getall()

        elif response.url == "https://en.wikipedia.org/wiki/Statues_of_Amun_in_the_form_of_a_ram_protecting_King_Taharqa":
                webItem['title_three'] = response.css('.mw-page-title-main::text').getall()
                webItem['summary_three'
                        ] = response.css('.mw-parser-output > p:nth-child(4)::text').getall()
                webItem['the_british_museum_state'
                        ] = response.css('.mw-parser-output > p:nth-child(9)::text').getall()
                webItem['the_ashmolean_state'
                        ] = response.css('.mw-parser-output > p:nth-child(11)::text').getall()
        yield webItem