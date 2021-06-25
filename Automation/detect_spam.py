import os
import re 
import timeit
import asyncio
import logging
import threading
import os.path as p
import pandas as pd
from pathlib import Path 
from datatime import datetime
from selenium import webdriver
from concurrent.futures import ThreadPoolExecutor

# TODO : ThreadPool과 asyncio를 활용한 crawler 만들기

class SpamCrawler:
    """
        (args) 스팸으로 처리되는 키워드 인자 
        (routine) 스팸 탐지 -> csv로 정보 저장
    """
    def __init__(self,keyword:str=""):
        self.keyword=keyword
        self.is_spammed=False
        self.executor=ThreadPoolExecutor(max_workers=os.cpu_count())
        self.folder_root=p.join(Path(__file__).resolve().parent.parent,'data')
        self.csv_name=f'{self.keyword}.csv'

    def check_root_dir(self):
        if not p.isdir(self.folder_root):
            os.mkdir(self.folder_root)

    def detect_spam(self):
        def get_title(self):
            pass 

        def get_senders(self):
            pass
        
        def get_context(self):
            pass
        
    def save_spam_to_csv(self):
        pass 

    async def fetch(self):
        pass

    async def crawl(self):
        pass 

if __nam__=="__main__":
    loop=asyncio.get_event_loop()
    start=timeit.default_timer()
    crawler=SpamCrawler("광고")
    loop.run_until_complete(crawler.crawl())
    duration=timeit.default_timer()-start
    print("Running time: ",duration)
