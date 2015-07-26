#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import traceback
from bs4 import BeautifulSoup


class Spider(object):

    def __init__(self, url):
        self._url = url

    def get_html(self):
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent}
        try:
            html = requests.get(self._url, headers=headers, timeout=10).text
        except:
            html = ''
            traceback.print_exc()
        return html

    def get_hot(self, html):
        soup = BeautifulSoup(html, 'lxml')
        article_tag_list = soup.find_all('div',
                                         class_='article block untagged mb15')
        res_list = []
        try:
            for article_tag in article_tag_list:
                author_a_tag = article_tag.find('div', class_='author')
                if author_a_tag:
                    author_tag = author_a_tag.find('a')
                    author = author_tag.text if author_tag else ''
                else:
                    author = ''
                content_tag = article_tag.find('div', class_='content')
                content = content_tag.text if content_tag else ''
                thumb_tag = article_tag.find('div', class_='thumb')
                img = thumb_tag.find('img').get('src') if thumb_tag else ''

                d = {'content': content, 'img': img, 'author': author}
                res_list.append(d)
        except:
            traceback.print_exc()

        return res_list

    def get_duanzi(self, html):
        return self.get_hot(html)

    def get_img(self, html):
        return self.get_hot(html)

def test_duanzi():
    url = "http://m.qiushibaike.com/text"
    spider = Spider(url)
    html = spider.get_html()
    duanzi_list = spider.get_hot(html)
    print len(duanzi_list)
    for each in duanzi_list:
        #print each.get('author'), each.get('content')
        print len(each.get('content'))
        print each.get('content')


def test_hot():
    url = "http://m.qiushibaike.com/hot/page/1"
    spider = Spider(url)
    html = spider.get_html()
    hot_list = spider.get_hot(html)
    print len(hot_list)
    for each in hot_list:
        print each.get('author'), each.get('content'), each.get('img')


def test_img():
    url = "http://m.qiushibaike.com/imgrank"
    spider = Spider(url)
    html = spider.get_html()
    duanzi_list = spider.get_hot(html)
    print len(duanzi_list)
    for each in duanzi_list:
        #print each.get('author'), each.get('content')
        print each.get('author'), each.get('content'), each.get('img')


def main():
    test_img()

if __name__ == '__main__':
    main()
