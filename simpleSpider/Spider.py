# coding=utf-8

from UrlManager import UrlManager
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser
from DataOutput import DataOuput


class SpiderMan(object):
    def __init__(self):
        url_manager = UrlManager()
        html_downloader = HtmlDownloader()
        html_parser = HtmlParser()
        data_output = DataOuput()

    def crawl(self, root_url):
        self.url_manager.add_new_url(root_url)
        while self.url_manager.has_new_url and self.old_urls_size() < 100:
            new_url = self.url_manager.get_new_url()
            page_cont = self.html_downloader.download(new_url)
            new_urls,new_data = self.html_parser.parser()
            self.url_manager.add_new_urls(new_urls)
            self.data_output.store_data(new_data)
        self.data_output.output_html()


if __name__ == "__main__":
    spiderMan = SpiderMan()
    spiderMan.crawl("http://baike.baidu.com/view/284853.htm")
