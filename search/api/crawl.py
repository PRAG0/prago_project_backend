import time
import requests

from bs4 import BeautifulSoup

from selenium.webdriver.chrome.options import Options
from selenium import webdriver

products_name = []
products_price = []
products_image = []
products_site_link = []
products_site_name = []
del_index = []

options = Options()
options.headless = True
options.add_argument('disable-gpu')

driver = webdriver.Chrome('c:\chromedriver_win32\chromedriver.exe', options=options)

driver.implicitly_wait(10)


def crawlilng(keyword):
    for index in range(1, 2):
        driver.get(
            f'https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery={keyword}&pagingIndex={index}&pagingSize=40&productSet=total&query={keyword}&sort=rel&timestamp=&viewType=list')

        SCROLL_PAUSE_TIME = 2

        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            time.sleep(SCROLL_PAUSE_TIME)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
            time.sleep(SCROLL_PAUSE_TIME)

            new_height = driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                break

            last_height = new_height

        html = driver.page_source
        driver.close()

        soup = BeautifulSoup(html, 'html.parser')

        ul = soup.find('ul', {'class': 'list_basis'})

        names = ul.findAll('div', {'class': 'basicList_title__3P9Q7'})
        prices = ul.findAll('strong', {'class': 'basicList_price__2r23_'})
        images = ul.findAll('div', {'class': 'thumbnail_thumb_wrap__1pEkS _wrapper'})
        mall_names = ul.findAll('div', {'class': 'basicList_mall_title__3MWFY'})
        lis = ul.findAll('div', {'class': 'thumbnail_thumb_wrap__1pEkS _wrapper'})

        for name in names[1:41]:
            prt_name = name.find('a')
            products_name.append(prt_name.text)

        for price in prices[1:41]:
            prt_price = price.find('span')
            products_price.append(prt_price.text)


        for i in range(len(images)):
            if "adcr.naver.com" in images[i].find('a')['href']:
                del_index.append(i)

        del_index.reverse()
        for i in del_index:
            images.pop(i)

        for i in range(len(images)):
            text = images[i].find('a')['href']
            image_id = text[-26: -15]
            products_image.append(
                f'https://shopping-phinf.pstatic.net/main_{image_id[:7]}/{image_id}.jpg?type=f140')


        for mall_name in mall_names[1:41]:
            mall = mall_name.find('a')
            if mall.text:
                products_site_name.append(mall.text)
            else:
                buffer = mall.find('img')
                products_site_name.append(buffer['alt'])

        for li in lis[1:41]:
            link = li.find('a')
            products_site_link.append(link['href'])

    return products_name, products_price, products_image, products_site_name, products_site_link
