from scrapy import Spider
from wikiCrawler.items import WikicrawlerItem

class wikipediaSpider(Spider):
    name = 'wikipediaCrawler'
    start_urls = [
        "https://en.wikipedia.org/wiki/Sphinx_of_Memphis",
        "https://en.wikipedia.org/wiki/Sphinx_of_Taharqo",
        "https://en.wikipedia.org/wiki/Statues_of_Amun_in_the_form_of_a_ram_protecting_King_Taharqa",
        'https://en.wikipedia.org/wiki/Ashmolean_Museum',
        'https://en.wikipedia.org/wiki/Sumerian_King_List',
        'https://en.wikipedia.org/wiki/Sumerian_creation_myth#Sumerian_flood_myth',
        'https://en.wikipedia.org/wiki/Mesopotamian_myths',
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
        webItem['title_four'] = None
        webItem['summary_four'] = None
        webItem['Broad_Street'] = None
        webItem['Beaumont_Street'] = None
        webItem['Beaumont_Street_2'] = None
        webItem['Beaumont_Street_3'] = None
        webItem['Beaumont_Street_4'] = None
        webItem['Beaumont_Street_5'] = None
        webItem['Renovations'] = None
        webItem['Renovations_2'] = None
        webItem['Renovations_3'] = None
        webItem['Renovations_4']  = None
        webItem['Renovations_5'] = None
        webItem['Renovations_6'] = None
        webItem['Collections'] = None
        webItem['title_five'] = None
        webItem['summary_five'] = None
        webItem['summary_five2'] = None
        webItem['summary_five3'] = None
        webItem['Naming_Conventions'] = None 
        webItem['Naming_Conventions_2'] = None
        webItem['Naming_Conventions_3'] = None
        webItem['Sources'] = None
        webItem['Sources_2'] = None
        webItem['Sources_3'] = None
        webItem['Sources_4'] = None
        webItem['Contents'] = None
        webItem['Contents_2'] = None
        webItem['Contents_3'] = None
        webItem['Before_the_Flood'] = None
        webItem['Before_the_Flood_2'] = None
        webItem['First_Dynasty_of_Kish_to_Lugal_zage_si'] = None
        webItem['First_Dynasty_of_Kish_to_Lugal_zage_si_2'] = None
        webItem['First_Dynasty_of_Kish_to_Lugal_zage_si_3'] = None
        webItem['First_Dynasty_of_Kish_to_Lugal_zage_si_4'] = None
        webItem['Akkad_to_Isin'] = None
        webItem['Akkad_to_Isin_2'] = None
        webItem['Sumerian_King_Summary_title'] = None
        webItem['Sumerian_King_Summary'] = None
        webItem['Discussion'] = None
        webItem['Discussion_2'] = None
        webItem['Dating_reaction_and_purpose'] = None
        webItem['Dating_reaction_and_purpose_2'] = None
        webItem['Dating_reaction_and_purpose_3'] = None
        webItem['Reliability_of_Source'] = None 
        webItem['Reliability_of_Source_2'] = None
        webItem['Reliability_of_Source_3'] = None
        webItem['Reliability_of_Source_4'] = None
        webItem['Reliability_of_Source_5'] = None
        webItem['Reliability_of_Source_6'] = None
        webItem['Antediluvian_rulers'] = None        
        webItem['title_six'] = None
        webItem['summary_six'] = None
        webItem['summary_six2'] = None
        webItem['summary_six3'] = None
        webItem['Flood_Myth'] = None
        webItem['Flood_Myth_2'] = None
        webItem['Flood_Myth_3'] = None
        webItem['Flood_Myth_4'] = None
        webItem['Flood_Myth_5'] = None
        webItem['Flood_Myth_6'] = None
        webItem['Flood_Myth_7'] = None
        webItem['Parallels'] = None
        webItem['Parallels_2'] = None
        webItem['Ziusudra_and_Xisuthros'] = None
        webItem['Ziusudra_and_Xisuthros_2'] = None
        webItem['Ziusudra_and_Xisuthros_3'] = None
        webItem['Ziusudra_and_Xisuthros_4'] = None
        webItem['title_seven'] = None
        webItem['summary_seven'] = None
        webItem['Creation_Myths'] = None
        webItem['Creation_Myths2'] = None
        webItem['Atra_Hasis'] = None
        webItem['Atra_Hasis_2'] = None
        webItem['Eridu_Genesis'] = None
        webItem['Eridu_Genesis_2'] = None
        webItem['Enuma_Elish'] = None
        webItem['Enuma_Elish_2'] = None
        webItem['Heroic_epics'] = None
        webItem['Heroic_epics_2'] = None
        webItem['The_Myth_of_Adapa'] = None
        webItem['The_Myth_of_Adapa_2'] = None
        webItem['Common_Themes'] = None
        webItem['Common_Themes_2'] = None
        webItem['Common_Themes_3'] = None
        webItem['Common_Themes_4'] = None
        webItem['Common_Themes_5'] = None
        webItem['Sources_Mesopotamian_Myths'] = None
        webItem['Sources_Mesopotamian_Myths_2'] = None
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
                
        elif response.url == "https://en.wikipedia.org/wiki/Ashmolean_Museum":

              webItem['title_four'] = response.css('.mw-page-title-main::text').getall()
              webItem['summary_four'] = response.css('#mw-content-text > div:nth-child(1) > p:nth-child(5)::text').getall()
              webItem['Broad_Street'] = response.css('#mw-content-text > div:nth-child(1) > p:nth-child(10)::text').getall()
              webItem['Beaumont_Street'] = response.css('#mw-content-text > div:nth-child(1) > p:nth-child(13)::text').getall()
              webItem['Beaumont_Street_2'] = response.css('#mw-content-text > div:nth-child(1) > p:nth-child(14)::text').getall()
              webItem['Beaumont_Street_3'] = response.css('#mw-content-text > div:nth-child(1) > p:nth-child(15)::text').getall()
              webItem['Beaumont_Street_4'] = response.css('#mw-content-text > div:nth-child(1) > p:nth-child(16)::text').getall()
              webItem['Beaumont_Street_5'] = response.css('#mw-content-text > div:nth-child(1) > p:nth-child(17)::text').getall()
              webItem['Renovations'] = response.css('#mw-content-text > div:nth-child(1) > p:nth-child(20)::text').getall()
              webItem['Renovations_2'] = response.css('#mw-content-text > div:nth-child(1) > p:nth-child(21)::text').getall()
              webItem['Renovations_3'] = response.css('#mw-content-text > div:nth-child(1) > p:nth-child(22)::text').getall()
              webItem['Renovations_4'] = response.css('#mw-content-text > div:nth-child(1) > p:nth-child(23)::text').getall()
              webItem['Renovations_5'] = response.css('#mw-content-text > div:nth-child(1) > p:nth-child(24)::text').getall()
              webItem['Renovations_6'] = response.css('#mw-content-text > div:nth-child(1) > p:nth-child(25)::text').getall()
              webItem['Collections'] = response.css('#mw-content-text > div:nth-child(1) > p:nth-child(30)::text').getall()
        
        elif response.url == 'https://en.wikipedia.org/wiki/Sumerian_King_List':

              webItem['title_five'] = response.css('#firstHeading > i:nth-child(1)::text').getall()
              webItem['summary_five'] = response.css('.mw-parser-output > p:nth-child(6)::text').getall()
              webItem['summary_five2'] = response.css('.mw-parser-output > p:nth-child(7)::text').getall()
              webItem['summary_five3'] = response.css('.mw-parser-output > p:nth-child(8)::text').getall()
              webItem['Naming_Conventions'] = response.css('.mw-parser-output > h2:nth-child(10)::text').getall()
              webItem['Naming_Conventions_2'] = response.css('.mw-parser-output > p:nth-child(11)::text').getall()
              webItem['Naming_Conventions_3'] = response.css('.mw-parser-output > p:nth-child(12)::text').getall()
              webItem['Sources'] = response.css('.mw-parser-output > h2:nth-child(13)::text').getall()
              webItem['Sources_2'] = response.css('.mw-parser-output > p:nth-child(16)::text').getall()
              webItem['Sources_3'] = response.css('.mw-parser-output > p:nth-child(17)::text').getall()
              webItem['Sources_4'] = response.css('.mw-parser-output > p:nth-child(18)::text').getall()
              webItem['Contents'] = response.css('.mw-parser-output > h2:nth-child(19)::text').getall()
              webItem['Contents_2'] = response.css('.mw-parser-output > p:nth-child(22)::text').getall()
              webItem['Contents_3'] = response.css('.mw-parser-output > p:nth-child(23)::text').getall()
              webItem['Before_the_Flood'] = response.css('.mw-parser-output > h3:nth-child(24)::text').getall()
              webItem['Before_the_Flood_2'] = response.css('.mw-parser-output > p:nth-child(25)::text').getall()
              webItem['First_Dynasty_of_Kish_to_Lugal_zage_si'] = response.css('.mw-parser-output > h3:nth-child(26)::text').getall()
              webItem['First_Dynasty_of_Kish_to_Lugal_zage_si_2'] = response.css('.mw-parser-output > p:nth-child(27)::text').getall()
              webItem['First_Dynasty_of_Kish_to_Lugal_zage_si_3'] = response.css('.mw-parser-output > p:nth-child(28)::text').getall()
              webItem['First_Dynasty_of_Kish_to_Lugal_zage_si_4'] = response.css('.mw-parser-output > p:nth-child(30)::text').getall()
              webItem['Akkad_to_Isin'] = response.css('.mw-parser-output > h3:nth-child(31)::text').getall()
              webItem['Akkad_to_Isin_2'] = response.css('.mw-parser-output > p:nth-child(32)::text').getall()
              webItem['Sumerian_King_Summary_title'] = response.css('#Lines_378–431\:_summary::text').getall()
              webItem['Sumerian_King_Summary'] = response.css('.mw-parser-output > p:nth-child(34)::text').getall()
              webItem['Discussion'] = response.css('.mw-parser-output > h2:nth-child(35)::text').getall()
              webItem['Discussion_2'] = response.css('.mw-parser-output > p:nth-child(36)::text').getall()
              webItem['Dating_reaction_and_purpose'] = response.css('.mw-parser-output > h3:nth-child(37)::text').getall()
              webItem['Dating_reaction_and_purpose_2'] = response.css('.mw-parser-output > p:nth-child(39)::text').getall()
              webItem["Dating_reaction_and_purpose_3"] = response.css('.mw-parser-output > p:nth-child(40)::text').getall()
              webItem['Reliability_of_Source'] = response.css('.mw-parser-output > h3:nth-child(41)::text').getall()
              webItem['Reliability_of_Source_2'] = response.css('.mw-parser-output > p:nth-child(42)::text').getall()
              webItem['Reliability_of_Source_3'] = response.css('.mw-parser-output > p:nth-child(43)::text').getall()
              webItem['Reliability_of_Source_4'] = response.css('.mw-parser-output > p:nth-child(44)::text').getall()
              webItem['Reliability_of_Source_5'] = response.css('.mw-parser-output > p:nth-child(45)::text').getall()
              webItem['Reliability_of_Source_6'] = response.css('.mw-parser-output > p:nth-child(46)::text').getall()
              webItem['Antediluvian_rulers'] = response.css('.mw-parser-output > p:nth-child(52)::text').getall()

        elif response.url == 'https://en.wikipedia.org/wiki/Sumerian_creation_myth#Sumerian_flood_myth':

              webItem['title_six'] = response.css('.mw-page-title-main::text').getall()
              webItem['summary_six'] = response.css('.mw-parser-output > p:nth-child(2)::text').getall()
              webItem['summary_six2'] = response.css('.mw-parser-output > p:nth-child(5)::text').getall()
              webItem['summary_six3'] = response.css('.mw-parser-output > p:nth-child(6)::text').getall()
              webItem['Flood_Myth'] = response.css('.mw-parser-output > h2:nth-child(7)::text').getall()
              webItem['Flood_Myth_2'] = response.css('.mw-parser-output > p:nth-child(8)::text').getall()
              webItem['Flood_Myth_3'] = response.css('.mw-parser-output > p:nth-child(9)::text').getall()
              webItem['Flood_Myth_4'] = response.css('.mw-parser-output > p:nth-child(10)::text').getall()
              webItem['Flood_Myth_5'] = response.css('.mw-parser-output > p:nth-child(11)::text').getall()
              webItem['Flood_Myth_6'] = response.css('.mw-parser-output > p:nth-child(12)::text').getall()
              webItem['Flood_Myth_7'] = response.css('.mw-parser-output > p:nth-child(13)::text').getall()
              webItem['Parallels'] = response.css('.mw-parser-output > h3:nth-child(14)::text').getall()
              webItem['Parallels_2'] = response.css('.mw-parser-output > p:nth-child(15)::text').getall()
              webItem['Ziusudra_and_Xisuthros'] = response.css('.mw-parser-output > h2:nth-child(16)::text').getall()
              webItem['Ziusudra_and_Xisuthros_2'] = response.css('.mw-parser-output > p:nth-child(17)::text').getall()
              webItem['Ziusudra_and_Xisuthros_3'] = response.css('.mw-parser-output > ul:nth-child(18)::text').getall()
              webItem['Ziusudra_and_Xisuthros_4'] = response.css('.mw-parser-output > p:nth-child(19)::text').getall()

        elif response.url == 'https://en.wikipedia.org/wiki/Mesopotamian_myths':

              webItem['title_seven'] = response.css('.mw-page-title-main').getall()
              webItem['summary_seven'] = response.css('.mw-parser-output > p:nth-child(13)::text').getall()
              webItem['Creation_Myths'] = response.css('.mw-parser-output > h2:nth-child(15)::text').getall()
              webItem['Creation_Myths2'] = response.css('.mw-parser-output > p:nth-child(18)::text').getall()
              webItem['Atra_Hasis'] = response.css('#Atra-Hasis::text').getall()
              webItem['Atra_Hasis_2'] = response.css('.mw-parser-output > p:nth-child(22)::text').getall()
              webItem['Eridu_Genesis'] = response.css('#Eridu_Genesis::text').getall()
              webItem['Eridu_Genesis_2'] = response.css('.mw-parser-output > p:nth-child(26)::text').getall()
              webItem['Enuma_Elish'] = response.css('#Enuma_Elish::text').getall()
              webItem['Enuma_Elish_2'] = response.css('.mw-parser-output > p:nth-child(30)::text').getall()
              webItem['Heroic_epics'] = response.css('#Heroic_epics::text').getall()
              webItem['Heroic_epics_2'] = response.css('.mw-parser-output > p:nth-child(32)::text').getall()
              webItem['The_Myth_of_Adapa'] = response.css('#The_Myth_of_Adapa::text').getall()
              webItem['The_Myth_of_Adapa_2'] = response.css('.mw-parser-output > p:nth-child(40)::text').getall()
              webItem['Common_Themes'] = response.css('#Common_themes::text').getall()
              webItem['Common_Themes_2'] = response.css('.mw-parser-output > p:nth-child(42)::text').getall()
              webItem['Common_Themes_3'] = response.css('.mw-parser-output > blockquote:nth-child(43)::text').getall()
              webItem['Common_Themes_4'] = response.css('.mw-parser-output > p:nth-child(44)::text').getall()
              webItem['Common_Themes_5'] = response.css('.mw-parser-output > p:nth-child(45)::text').getall()
              webItem['Sources_Mesopotamian_Myths'] = response.css('.mw-parser-output > h2:nth-child(46)::text').getall()
              webItem['Sources_Mesopotamian_Myths_2'] = response.css('.mw-parser-output > p:nth-child(47)::text').getall()

        yield webItem 