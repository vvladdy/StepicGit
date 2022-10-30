import requests
from bs4 import BeautifulSoup

from autoriaadmin.models import CarModel

MODEL_LIST = []

def parsing(url):
    with requests.Session() as session:
        response = session.get(url, timeout=10)
        assert response.status_code == 200, 'BAD RESPONCE'
        print(response.status_code)

        soup = BeautifulSoup(response.content, 'html.parser')

        models = soup.select('#brandTooltipBrandAutocomplete-brand li')

        for i in range(1, 20):
            MODEL_LIST.append(models[i].text.strip().lower())
            print(models[i].text.strip().lower())
            cars, _ = CarModel.objects.get_or_create(
                car_model=models[i].text.strip().lower()
            )
        cars, _ = CarModel.objects.get_or_create(
            car_model='geely'.lower()
        )
        cars, _ = CarModel.objects.get_or_create(
            car_model='subaru'.lower()
        )
        cars, _ = CarModel.objects.get_or_create(
            car_model='citroen'.lower()
        )
        MODEL_LIST.append('Geely'.lower())
        MODEL_LIST.append('subaru'.lower())
        MODEL_LIST.append('citroen'.lower())

def _writefile():
    with open(r'C:\Users\User\PycharmProjects\StepicGit\Project_Dj_My'
              r'\autoriaadmin\media\Files\model_auto.txt', 'w') as file:
        for i in MODEL_LIST:
            file.write(i + '\n')


def main():
    parsing('https://auto.ria.com/uk/')
    _writefile()

