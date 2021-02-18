import random
proxyList = ['http://proxy.cht.com.tw:8080',
             'http://proxy.cht.com.tw:8081']

proxy = random.choice(proxyList).strip()
print(proxy)
