# coding:utf-8
from baike_spider import url_manager
from baike_spider import html_downloader
from baike_spider import html_parser
from baike_spider import html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        # 记录爬取的数量
        count = 1
        # 添加根目录
        self.urls.add_new_url(root_url)
        # 当有新的Url时候进入循环
        while self.urls.has_new_url():

            try:

                print 'craw %d : %s' % (count, new_url)
                # 获得新的Url
                new_url = self.urls.get_new_url()
                # 下载HTML页面
                html_cont = self.downloader.download(new_url)
                # 解析HTML
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                # 把页面中的Url添加进Url库中
                self.urls.add_new_urls(new_urls)
                # 获取页面中的数据，并展示
                self.outputer.collect_data(new_data)

                count = count + 1
                # 只爬取1000个页面
                if count == 1000:
                    break
            except:
                print 'craw failed'
        self.outputer.output_html()

if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
