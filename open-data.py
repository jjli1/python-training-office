import requests as requests

user_agent = '"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36"'
headers = {'User-Agent': user_agent}
src = 'https://www.ntu.edu.tw/'


with requests.get(src, headers=headers) as response:
    data = response.read()
    print('len=', len(data))
