import urllib.request
import bs4

url = 'https://www.ptt.cc/bbs/movie/index.html'
proxy_handler = urllib.request.ProxyHandler({
    'http': 'http://proxy.cht.com.tw:8080',
    'https': 'http://proxy.cht.com.tw:8080',
})

opener = urllib.request.build_opener(proxy_handler)
opener.addheaders = [
    ('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36')]
urllib.request.install_opener(opener)

with urllib.request.urlopen(url) as response:
    data = response.read().decode('utf-8')

root = bs4.BeautifulSoup(data, 'html.parser')
titles = root.find_all('div', class_='title')
# <div class="title">
# <a href="/bbs/movie/M.1612455357.A.73C.html">[好雷] 刻在你心底的名字／時代體制寫給自由的深刻告白</a>
# </div>

for title in titles:
    if title.a != None:
        print(title.a.string)
