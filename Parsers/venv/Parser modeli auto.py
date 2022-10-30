import requests
from bs4 import BeautifulSoup

def parsing(url):
    with requests.Session() as session:
        response = session.get(url, timeout=10)
        assert response.status_code == 200, 'BAD RESPONCE'
        print(response.status_code)

        soup = BeautifulSoup(response.content, 'html.parser')

        models = soup.select('#brandTooltipBrandAutocomplete-brand li')

        for i in range(1, 20):
            print(models[i].text.strip().lower())
        print('Geely'.lower())
        print('subaru'.lower())
        print('citroen'.lower())


        # for n, i in enumerate(models):
        #     print(n, i.text)


        # print(models)

def main():
    parsing('https://auto.ria.com/uk/')

if __name__ == '__main__':
    main()