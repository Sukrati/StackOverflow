# -*- coding: utf-8 -*-
import scrapy


class TagsSpider(scrapy.Spider):
    name = 'tags'
    allowed_domains = ['stackoverflow.com']
    start_urls = ['https://stackoverflow.com/tags?tab=popular']

    def parse(self, response):
        obj=response.css('.tag-cell')
        for count in obj:
            tag=count.css('.post-tag::text').extract_first()
            link=count.css('.post-tag::attr(href)').extract_first()
            description=count.css('.excerpt::text').extract_first()
            #today=count.css('a::text')[1].extract()
            #week=count.css('a::text')[2].extract()
            yield{'tag':tag, 'link':link, 'description':description}
        next_page_url=response.xpath('//*[@class="pager fr"]/a/@href')[-1].extract()
        if next_page_url:
            yield scrapy.Request(response.urljoin(next_page_url),callback=self.parse)
