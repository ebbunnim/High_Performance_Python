import requests
import asyncio
import aiohttp

def get_html_sync(urls):
    """
        코루틴을 이용한 get_html_async(url)와 실행 시간 5배 정도 차이가 남
    """
    _html=""
    for url in urls:
        response=requests.get(url)
        if response.status_code==200:
            _html=response.text
        print(_html)

async def get_html_async(url):
    html=None
    response=None
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print("status: ",response.status)
            print("content type: ",response.headers["content-type"])
            html = await response.text()
            print("Body: ",html[:30],"...")

request_url="http://python.org"
request_urls=[request_url]*20
tasks = [get_html_async(x) for x in request_urls]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks)) # ($ time python get_html.py) 0.34s user 0.07s system 24% cpu 1.671 total

# get_html_sync(request_urls) # ($ time python get_html.py) 1.66s user 0.20s system 6% cpu 29.526 total