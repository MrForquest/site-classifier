import aiohttp
import asyncio
import time
from bs4 import BeautifulSoup
import re
import yarl
import random

start_time = time.time()
history = set()
abs_hist = list()


async def get_content(session, urls: list, depth=1, max_depth=1):
    depth += 1
    links_ = list()
    text = ""
    for url in urls:
        if isinstance(url, str):
            url = yarl.URL(url)
        abs_hist.append(url)
        if url in history:
            continue
        else:
            history.add(url)
        try:
            async with session.get(url, ssl=False) as resp:
                content = await resp.content.read()
                text, links = parse_site(content, resp)
                links_.extend(links)
                # print(links)
        except Exception as exc:
            print(exc, url)
    if depth > max_depth:
        return text
    else:
        return text + " " + await get_content(session, links_, depth, max_depth)


def parse_site(content, resp):
    soup = BeautifulSoup(content, features="html.parser")
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()  # rip it out
    # get text
    text = soup.get_text()
    text = re.sub("ё", "е", text.lower())
    text = re.sub("[^а-я ]", " ", text)
    text = re.sub("\s+", " ", text).strip()
    # print((resp.real_url.join(yarl.URL("lol"))))
    host = yarl.URL(resp.real_url.origin())
    links = list()
    for link in soup.find_all("a", href=True):
        link_ = link["href"]
        link_ = yarl.URL(link_)

        if not link_.is_absolute():
            link_ = host.join(link_)
        if link_ in history:
            continue
        if link_.host == host.host:
            links.append(link_)
    if len(links) > 15:
        links = random.choices(links, k=15)
    return text, links


def get_sites_list(filename):
    file = open(filename, "r")
    sites = file.readlines()
    file.close()
    return sites


async def get_sites_contents(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []

        for url in sites:
            tasks.append(
                asyncio.ensure_future(get_content(session, [url], max_depth=1))
            )

        sites_contents = await asyncio.gather(*tasks)
        return sites_contents
