import requests
import string
import random
import time
from Concurrency.logger import FileLogger

def generate_urls(base_url,num_urls):
    """
    url 맨 마지막에 임의의 문자를 추가해서
    requests 라이브러리나 서버의 캐시 기능을 무효화시킨다.
    """
    for i in range(num_urls):
        yield base_url+''.join(random.sample(string.ascii_lowercase,10))

def run_experiment(base_url, num_iter=500):
    response_size=0
    for url in generate_urls(base_url,num_iter):
        start = time.time()
        response=requests.get(url)
        response_size+=len(response.text)
        end = time.time()
        # write log of sequential process
        f.write(start,end)
    return response_size

if __name__=="__main__":

    # start logger
    f=FileLogger(log_name='<Log of sequential crawler>')
    f.make_log_dir()
    f.start_logging(log_name='<Log of sequential crawler>')

    delay=100
    num_iter=500
    base_url=f'https://blog.naver.com/sjy263942?delay={delay}&'
    start=time.time()
    result=run_experiment(base_url,num_iter)
    end=time.time()
    print(f'Result: {result}, Time: {end-start}')

    # finish logger
    f.finish_logging()

