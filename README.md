# scrpay-genpdf
This is a project base on scrapy and use reportlab to generate a pdf to save all the messages.

You can custom your items in aaOils/aaOils/items.py.

File aaOils/aaOils/spiders/aaoil_spider.py is your spider used to crawl infomation from website.You can custom the start urls
and parse function in this file.

Use scrapy crawl spider -o XXX.json to run this project at aaOils directory and you will get a XXX.json file.

File genPdf.py use the reportlab package to convert the infos in XXX.json to a pdf which contains pictures.
