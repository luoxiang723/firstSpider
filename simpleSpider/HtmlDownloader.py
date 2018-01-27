#coding=utf-8
import requests
import chardet

class HtmlDownloader(object):
    def download(self,url):
        if url is None:
            return None
        user_agent='Mozilla/4.0 (compatible; MSID 5.5; Windows NT)'
        headers = {'User_Agent':user_agent}
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            response.encoding = chardet.detect(response.content)['encoding']
            return response.text
        return None