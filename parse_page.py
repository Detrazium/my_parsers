import requests
from bs4 import BeautifulSoup

def getpage(url):
    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, 'html.parser')
    return soup
def alldesript(soup):
    descr = soup.find('section', {'class': 'page-product-box'})
    datas = descr.find('table', attrs={'class': 'table-data-sheet'})
    items = {}
    for i in datas:
        source = []
        for el in i:
            source.append(el.text)
        items[source[0]] = source[1]
    print(items)
    print('\n')
    return
def get_items(soup, url):
    # urli = url
    # title = soup.find('title').text
    # Model = soup.find('h1', attrs={'itemprop': 'name'}).text
    # price = soup.find('span', attrs={'id': 'our_price_display'}).text
    # price_discount = None
    # availability = soup.find('span', attrs={'id': 'availability_value'}).text
    # delivery_time = None
    # all_images = [image.find('a').get('href') for image in soup.find('ul', attrs={'id': 'thumbs_list_frame'})]
    # descript_low = soup.find('div', {'id': 'short_description_content'}).text.replace('PRODUCT DETAILS' , '')
    descript = soup.select('div.rte')
    for i in descript:
        print(i.text)
    print('\n')

    # descript_all =  alldesript(soup)


def parsepage(url):
    soup = getpage(url)
    items = get_items(soup, url)

if __name__ == '__main__':
    url1 = 'https://shop.pixsys.net/en/home/1-regolatori-controllori-atr121-ad.html'
    url2 = 'https://shop.pixsys.net/en/net250/87-net250-2ad.html'
    for u in [url1, url2]:
        parsepage(u)