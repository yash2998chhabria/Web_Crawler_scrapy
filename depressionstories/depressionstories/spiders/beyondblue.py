# -*- coding: utf-8 -*-
import scrapy


class BeyondblueSpider(scrapy.Spider):
    name = 'beyondblue'
    allowed_domains = ['www.beyondblue.org.au']
    start_urls = ['https://www.beyondblue.org.au/who-does-it-affect/personal-stories?category=7c245435-a559-465b-bdcb-8b993cb47c6e']

    def parse(self, response):
        links = response.xpath('//a[@class="read-more"]')
        for link in links:
            http_link = link.xpath(".//@href").get()
            if link:
                yield response.follow(url=link, callback=self.parse_story)
        # next_page = response.xpath('//a[@id="ctl00_MainContentPlaceholder_C006_rlvList_pager_ctl02_lnkNext"]/@href').get()       
        # print(next_page)
        # if next_page:
        #     yield response.follow(url=next_page, callback= self.parse)                


    def parse_story(self, response):
        name_of_scrapees = response.xpath('////span[@class="title"]/text()').get()
        blocksofstory = response.xpath('//div[starts-with(@class,"cr69")]//p/text()').getall()
        yield {
            'name': name_of_scrapees,
            'story': blocksofstory
        }

        