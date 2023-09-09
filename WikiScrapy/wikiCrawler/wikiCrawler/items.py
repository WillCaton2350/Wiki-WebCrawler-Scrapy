from scrapy import Item, Field

class WikicrawlerItem(Item):
    id = Field()
    url = Field()
    title = Field()
    summary = Field()
    discovery = Field()
    composition = Field()
    physical_attributes = Field()
    other_information = Field()
    title_two = Field()
    summary_two = Field()
    taharqo = Field()
    the_statue = Field()
    title_three = Field()
    summary_three = Field()
    the_british_museum_state = Field()
    the_ashmolean_state = Field()