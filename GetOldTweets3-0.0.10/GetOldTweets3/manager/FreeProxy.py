import requests
from lxml import html


class FreeProxy:

    def loadProxies(self):
        with open('proxies.txt') as f:
            content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        return [x.strip() for x in content]

    name = "free_proxy"

    def getProxies(self):
        return self.proxies

    proxies = []

    def __init__(self) -> None:
        super().__init__()
        self.proxies = self.loadProxies()

    '''deprecated '''

    def get_proxies(self):
        pageContent = requests.get(
            'https://free-proxy-list.net/'
        )
        tree = html.fromstring(pageContent.content)
        rows = tree.xpath('//*[@id="proxylisttable"]//tr')
        proxies = []
        for row in rows:
            ip = row[0].text_content()
            port = row[1].text_content()
            url = ip + ':' + port
            proxies.append(url)
        proxies = proxies[1:]
        print(proxies)
        return proxies
