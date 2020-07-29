import time
import json

from bs4 import BeautifulSoup

from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def crawlilng(keyword):
    prev_soup = ""
    products_name = []
    products_price = []
    products_image = []
    products_site_link = []
    products_site_name = []

    options = Options()
    options.headless = True
    options.add_argument('disable-gpu')

    for index in range(1, 2):
        driver = webdriver.Chrome(executable_path=r'c:\chromedriver_win32\chromedriver.exe', options=options)
        driver.get(
            f'https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery={keyword}&pagingIndex={index}&pagingSize=40&productSet=total&query={keyword}&sort=rel&timestamp=&viewType=list')

        time.sleep(3)

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
        # driver.quit()

        soup = BeautifulSoup(html, 'html.parser')
        # if prev_soup == soup:
        #     return products_name, products_price, products_image, products_site_name, products_site_link

        ul = soup.find('ul', {'class': 'list_basis'})

        names = ul.findAll('div', {'class': 'basicList_title__3P9Q7'})
        prices = ul.findAll('strong', {'class': 'basicList_price__2r23_'})
        images = driver.find_element_by_xpath('//*[@id="__NEXT_DATA__"]')
        mall_names = ul.findAll('div', {'class': 'basicList_mall_area__lIA7R'})
        lis = ul.findAll('div', {'class': 'thumbnail_thumb_wrap__1pEkS _wrapper'})

        for name in names[1:41]:
            prt_name = name.find('a')
            products_name.append(prt_name.text)

        for price in prices[1:41]:
            prt_price = price.find('span')
            products_price.append(prt_price.text)

        json_text = json.loads(images.get_attribute('text'))
        json_list = json_text['props']['pageProps']['initialState']['products']['list']

        for element in json_list:
            item = element['item']
            name = item['productName']

            if item.get('imageUrl') == None:
                image_url = item.get('productImgUrl')
            else:
                image_url = item.get('imageUrl') + "?type=f300"

            products_image.append(image_url)

        for mall_name in mall_names[:41]:
            mall_tag = mall_name.find('div', {'class': 'basicList_mall_title__3MWFY'})
            mall = mall_tag.find('a')
            if mall.text == "쇼핑몰별 최저가":
                first_mall = mall_name.find('a', {'class': 'basicList_mall_item__tHbWj'})
                products_site_name.append(first_mall['title'])

            elif mall.text:
                products_site_name.append(mall.text)
            else:
                buffer = mall.find('img')
                products_site_name.append(buffer['alt'])

        for li in lis[1:41]:
            link = li.find('a')
            products_site_link.append(link['href'])

        prev_soup = soup
        driver.quit()

    return products_name, products_price, products_image, products_site_name, products_site_link
