# -*- coding: utf-8 -*-
import scrapy
import logging 

class DepressiondatasetSpider(scrapy.Spider):
    name = 'depressiondataset'
    allowed_domains = ['www.time-to-change.org.uk']
    start_urls = ['https://www.time-to-change.org.uk/category/blog/depression/']

    def parse(self, response):
        stories = response.xpath('//article[@role="article"]')
        for story in stories:
            link = story.xpath('.//a[@rel="bookmark"]/@href').get()

            if link is not None:
                present_link = link
                yield response.follow(url=present_link, callback=self.parse_story)
        next_page = response.xpath('//a[@title="Go to next page"]/@href').get()       
        if next_page:
            yield response.follow(url=next_page, callback= self.parse)

        

    def parse_story(seld,response):
        name_of_scrapees = response.xpath('//span[@class="blog-name"]/text()').get()
        blocksofstory = response.xpath('//div[@class="node-content"]//p[text() !="Too many people are made to feel ashamed. By sharing your story, you can help spread knowledge and perspective about mental illness that could change the way people think about it."]/text()').getall()

        yield {
            'name': name_of_scrapees,
            'story': blocksofstory
        }