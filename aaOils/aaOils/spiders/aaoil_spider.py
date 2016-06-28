import scrapy
import json
from aaOils.items import OilItem

missRecord = 0

class aaoilSpider(scrapy.Spider):
    name = "spider"
    start_urls = ["http://www.amphora-retail.com/index.php/essential-oils-pure-essential-oils-c-101105_102000","http://www.amphora-retail.com/index.php/essential-oils-speciality-essential-oils-c-101105_101101","http://www.amphora-retail.com/index.php/essential-oils-precious-absolute-oils-c-101105_101102","http://www.amphora-retail.com/index.php/essential-oils-diluted-absolute-precious-oils-c-101105_101103","http://www.amphora-retail.com/index.php/essential-oils-organic-essential-oils-c-101105_101104",]

    def parse(self,response):
        hrefs = response.xpath("//a[contains(@href,'page=')]/@href").extract()
        for href in hrefs:
            if href.endswith('a'):
                yield scrapy.Request(href,callback=self.parse_list_page)

    def parse_list_page(self,response):
        certain_page_urls = response.xpath("//div[@id='products']/div/div/div[@class='caption']/h2/a/@href").extract()
        for certain_page_url in certain_page_urls:
            yield scrapy.Request(certain_page_url,callback=self.parse_certain_page)

    def parse_certain_page(self,response):
        item = OilItem()
        item['htmlUrl'] = response.url
        item['imgSrc'] = response.urljoin(response.xpath("//img[@id='piGalImg_1']/@src").extract()[0])
        item['oilName'] = response.xpath("//h1/a/span[@itemprop='name']/text()").extract()[0]
        descriptions = response.xpath("//div[@itemprop='description']/div/ul/li/h2/text()").extract()
        item['description'] = descriptions 
        info = response.xpath("//td[@class='producttext']/text()").extract()
        content = response.xpath("//div[@class='contentContainer']/div[@class='contentText']/table//td")
        for i in range(0,len(content)/2):
            key = content[i].xpath("span/text()").extract()[0].lower().replace(' ','_')
            value = content[i+len(content)/2].xpath("text()").extract()[0]
            item[key] = value
            pricesRangeInfo = response.xpath("//h1[@itemprop='offers']//text()").extract()
        if len(pricesRangeInfo) > 4:
            pricesRangeInfo.pop()
            pricesRangeInfo.pop()
        item['priceRange'] = ''.join(pricesRangeInfo)
        #tempNum = len(response.xpath("//div[@id='stocktable']//span[@class='ProductDetails']"))
        tempTrNum = len(response.xpath("//div[@id='stocktable']//tr")) - 1
        tempPriceInfo = response.xpath("//div[@id='stocktable']//td[@class='producttext']/text()").extract()
        item['prices'] = {}
        for i in range(tempTrNum):
            item['prices'][tempPriceInfo[i*2]] = tempPriceInfo[i*2+1]
        #except:
        #    global missRecord
        #    missRecord += 1
        #    print("----------------------------------------------------------This oil's info is missing!The total num is %d"% missRecord)
        #    print(item['htmlUrl'])
        #else:
           # with open('oilsMessages.json','a') as file:
           #     json.dumps(item,file)
        yield item
