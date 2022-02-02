import requests
import bs4


def search_part(part: str = "tms320f2808pza"):  # tms320f2808pza
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    url = "https://www.digikey.com//en/products/result"
    result = requests.get(url, {"keywords": part}, headers=headers)
    soup = bs4.BeautifulSoup(result.text, 'lxml')

    trs = soup.find('div', class_='jss122')
    # for tr in trs:
    #     position = tr.find_all('th', class_='MuiTableCell-root MuiTableCell-head jss336 jss337 MuiTableCell-paddingNone')
    #     for i in position:
    #         positions = i.text.replace('\n', '')
    #         print(positions)

    with open('test_digikey.html', 'w', encoding="utf-8") as f:
        f.write(trs.text)
    print(result.url)


if __name__ == '__main__':
    search_part("tms320f2808pza")
