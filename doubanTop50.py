import requests
from bs4 import BeautifulSoup
download_url = "http://movie.douban.com/top250"
heads = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0'}
def download_page(url):
    data = requests.get(url).content
    return  data

def parse_html(html):
    movie_name_list = []
    soup = BeautifulSoup(html)
    movie_list_soup = soup.find('ol',attrs={'class':'grid_view'})
    for movie_li in movie_list_soup.find_all('li'):
        details = movie_li.find('div',attrs={'class':'hd'})
        movie_name = details.find('span',attrs={'class':'title'}).getText()
        movie_name_list.append(movie_name)
        next_page = soup.find('span',attrs={'class':'next'}).find('a')
        if next_page:
            return movie_name_list,download_url+next_page['href']
        return movie_name_list,None
def main():
    url = download_url
    parse_html(download_page(download_url))
    while url:
        html = download_page(url)
        for movie_name in parse_html(html):
            print(movie_name)



if __name__ == '__main__':
    main()

