from icrawler.builtin import BaiduImageCrawler, BingImageCrawler, GoogleImageCrawler


google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=10,
                                    storage={'root_dir': '/root/data/dogNcat/dogNcat_photos/dogs'})

google_crawler.crawl(keyword='dog', offset=0, max_num=400,
                     date_min=None, date_max=None,
                     min_size=(100,100), max_size=None)

google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=10,
                                    storage={'root_dir': '/root/data/dogNcat/dogNcat_photos/cats'})
google_crawler.crawl(keyword='cat', offset=0, max_num=400,
                     date_min=None, date_max=None,
                     min_size=(100,100), max_size=None)
