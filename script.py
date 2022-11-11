import time
import requests
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from database import save_product,select_product_data,save_link,select_links,save_feedback,clear_table_fb,clear_table_links,clear_table_prod

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def parse_products(url):
    response = requests.get(url=url).json()
    data = response["data"]["products"]
    for i in data:
        id = i["id"]
        root = i["root"]
        size = i["sizes"][0]["optionId"]

        save_product(id=id,root=root,size=size)

def generate_links():
    for i in select_product_data():
        link = f'https://www.wildberries.ru/catalog/{i[0]}/questions?imtId={i[1]}&size={i[2]}'
        print(link)
        save_link(url=link)


# parse_products(url='https://catalog.wb.ru/catalog/beauty11/catalog?appType=1&couponsGeo=2,12,7,3,6,13,21&curr=rub&dest=-1113276,-79379,-1104258,-5803327&emp=0&ext=63527&lang=ru&locale=ru&pricemarginCoeff=1.0&reg=0&regions=80,64,58,83,4,38,33,70,82,69,68,86,30,40,48,1,22,66,31&spp=0&subject=344;346;347;350;351;353;354;358;437;796;1250;1410;1527;1613;1614;1624;1871;1934;2027;2375;2565;4837;4838;5278;6059;6120')
# generate_links()


def parse_fb(url):
    clear_table_links()
    clear_table_fb()
    clear_table_prod()
    parse_products(url=url)
    generate_links()
    count = 0
    for i in select_links():
        count = count + 1

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        response = driver.get(url=i[0])
        html = driver.page_source
        driver.implicitly_wait(5)
        try:
            text = driver.find_element(by=By.CLASS_NAME,value='feedback__sellers-reply').text
            print(text)
            save_feedback(text=text, url=i[0])
        except Exception as e:
            print('NO SELLERS REPLY')
            pass





