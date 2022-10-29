import requests
from bs4 import BeautifulSoup

def parsing(url):
    with requests.Session() as session:
        response = session.get(url, timeout=10)
        assert response.status_code == 200, 'BAD RESPONCE'
        print(response.status_code)

        soup = BeautifulSoup(response.content, 'html.parser')

        models = soup.select('#brandTooltipBrandAutocomplete-brand li')

        for i in range(22, len(models)):
            print(models[i].text.strip())

def main():
    parsing('https://auto.ria.com/uk/')

if __name__ == '__main__':
    main()