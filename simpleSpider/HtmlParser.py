# coding=utf-8
import re
import urlparse
from bs4 import BeautifulSoup


class HtmlParser(object):
    def _get_new_urls(self, page_url, soup):
        '''
        抽取新的URL集合
        :param page_url:下载页面的URL
        :param soup:soup
        :return:返回新的URL集合
        '''
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/item/.*'))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            if new_full_url not in new_urls:
                new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        '''
        抽取有效数据
        :param page_url: 下载页面的URL
        :param soup: soup
        :return:返回有效数据
        '''
        data = {}
        data['url'] = page_url
        title = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h2')
        data['title'] = title.get_text()
        summary = soup.find('div', class_='lemma-summary')
        data['summary'] = summary.get_text()
        return data

    def parser(self, page_url, page_cont):
        '''
        用于解析网页内容抽取URL和数据
        :param page_url:下载页面的URL
        :param page_cont:下载的网页内容
        :return:返回URL和数据
        '''
        soup = BeautifulSoup(page_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        newdata = self._get_new_data(page_url, soup)
        return new_urls,newdata
