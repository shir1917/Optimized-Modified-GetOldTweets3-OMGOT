import scrapy



''' scrapy shell  

scrapy shell https://free-proxy-list.net/
table = response.xpath('//*[@id="proxylisttable"]')

rows = table.xpath('//tr')
row.xpath('td//text()')[0].extract()

ip:
Out[8]: '200.27.110.29'


port
In [10]: row.xpath('td//text()')[1].extract()
Out[10]: '51061'

''' 
 
 
class free_proxy(scrapy.Spider):
    name = "free_proxy"
 
    def start_requests(self):
        urls = [
            'https://free-proxy-list.net/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
 
    def get_proxies(self, response):
        proxies=[]
        table = response.xpath('//*[@id="proxylisttable"]')
        rows = table.xpath('//tr')
        for row in rows:
            ip= row.xpath('td//text()')[0].extract()
            port= row.xpath('td//text()')[1].extract()
            proxies.append("%s:%s",ip,port)

        return proxies    
            
def test_Username():
    proxies =free_proxy().get_proxies
    assert proxies != None
    print(proxies)
