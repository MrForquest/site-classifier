import asyncio
from joblib import Parallel, delayed
from bs4 import BeautifulSoup
import re
import time
import yarl
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import random
import traceback
import chrome_config
from functools import reduce

history = set()
start_time = time.time()

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("prefs", chrome_config.prefs)

for argrumnet in chrome_config.chrome_args:
    chrome_options.add_argument(argrumnet)


class BColors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def debug_procces(func):
    def wrapper(*args, **kwargs):
        try:
            return_value = func(*args, **kwargs)
        except Exception as exc:
            print(BColors.FAIL + traceback.format_exc() + BColors.ENDC)
        return return_value

    return wrapper


def many_scraper(urls):
    # driver = webdriver.Chrome("./chromedriver", options=chrome_options)
    results = list()
    driver = webdriver.Chrome("./chromedriver", options=chrome_options)
    for url in urls:
        try:
            driver.get(str(url))
            page = driver.page_source
            resp = parse_site(page, yarl.URL(url))
            results.append(resp)
            print("Ready!", url)
        except WebDriverException as exc:
            print(exc)
        except ValueError as exc:
            print(exc)
    driver.close()
    # res = parse_site(page, yarl.URL(url))
    # print(res)

    return results


def get_sites_list(filename):
    file = open(filename, "r")
    sites = file.readlines()
    file.close()
    return [yarl.URL(site.strip()) for site in sites]


def split_data(num_parts, data):
    if len(data) < num_parts:
        res = [list() for i in range(num_parts)]
        for i in range(len(data)):
            res[i] = data[i]
        return num_parts
    seg_len = len(data) // num_parts
    parts_sets = list()
    for i in range(num_parts):
        s_ind = i * seg_len
        e_ind = seg_len * (i + 1)
        if i == (num_parts - 1):
            parts_set = data[s_ind:]
        else:
            parts_set = data[s_ind:e_ind]
        parts_sets.append(parts_set)
    return parts_sets


def parse_site(content, main_url):
    soup = BeautifulSoup(content, features="html.parser")
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()  # rip it out
    # get text
    text = soup.get_text(separator=" ")
    text = re.sub("ё", "е", text.lower())
    text = re.sub("[^а-я ]", " ", text)
    text = re.sub("\s+", " ", text).strip()

    if not main_url.scheme:
        print(BColors.FAIL + str(main_url) + BColors.ENDC)
    host = main_url.host
    scheme = main_url.scheme
    links = list()
    for link in soup.find_all("a", href=True):
        link_ = link["href"]
        link_ = yarl.URL(link_)

        if not link_.is_absolute():
            # print(scheme, host, link_.path)
            path = link_.path
            path = path if path else "/"
            path = ("" if path[0] == "/" else "/") + path
            link_ = yarl.URL.build(scheme=scheme, host=host, path=path)
        if link_ in history:
            continue
        if link_.host == host:
            links.append(link_)
    if len(links) > MAX_LINKS_ON_PAGE:
        links = random.choices(links, k=MAX_LINKS_ON_PAGE)
    return host, text, links


MAX_LINKS_ON_PAGE = 10
MAX_DEPTH = 1


def get_sites_contents(urls):
    data_text = dict()
    num_processes = 7
    if len(urls) < num_processes:
        num_processes = len(urls)
    splt_urls = split_data(num_processes, urls)

    print(len(splt_urls))

    depth = 0
    procces_pool = Parallel(n_jobs=num_processes, prefer="processes",
                            verbose=1)

    while depth < MAX_DEPTH:
        splt_urls = split_data(num_processes, urls)

        results = procces_pool(
            delayed(many_scraper)(url_set) for url_set in splt_urls)
        urls.clear()

        results = reduce(lambda l1, l2: l1 + l2, results)
        for resp in results:
            host, text, links = resp
            new_text = data_text.get(host, "") + " " + text
            data_text[host] = new_text
            urls.extend(links)
        depth += 1
    return data_text
