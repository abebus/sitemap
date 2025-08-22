from scrapy.crawler import CrawlerProcess
from scrapy.http import Response
from scrapy.spiders import SitemapSpider

class BasicSpider(SitemapSpider):
    custom_settings = {"TELNETCONSOLE_ENABLED": False, "LOG_LEVEL": "INFO"}
    name = "sitemap"
    sitemap_urls = ["https://www.ebay.com/robots.txt"]

    def parse(self, r: Response):
        pass

if __name__ == "__main__":
    process = CrawlerProcess()

    process.crawl(BasicSpider)
    process.start()
