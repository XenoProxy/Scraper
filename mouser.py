import requests
import bs4


def search_part(part: str = "tms320f2808pza"):  # tms320f2808pza
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    url = "https://eu.mouser.com/c/"
    result = requests.get(url, {"q": part}, headers=headers)
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    trs = soup.find('div', class_='search-table-wrapper').find('table').find_all('tr')

    for i in range(len(trs)):

        tr = trs[i]
        position = tr.find_all(attrs={'id': f'lnkProductImage_{i+1}'})
        output = position[i]['onclick']
        print(output)

    # with open('test_mouser.html', 'w', encoding="utf-8") as f:
    #     f.write(result.text)
    print(result.url)


if __name__ == '__main__':
    search_part("tms320f2808pza")
