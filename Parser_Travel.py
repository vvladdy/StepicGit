import sys
from concurrent.futures import ThreadPoolExecutor
from queue import Queue
import requests
from bs4 import BeautifulSoup


TIME_OUT = 10

def download_image_to_local_media(img_url, image_name: str):
    with requests.Session() as session:
        img_responce = session.get(img_url, timeout=TIME_OUT)

    with open(f'imgTravel/{image_name}', 'wb') as file:
        file.write(img_responce.content)

def process(html_string: str, url:str):
    soup = BeautifulSoup(html_string, 'html.parser')
    try:
        title = soup.select('.column_attr h1')
        #title = title[0].text.strip()
        if title == []:
            title = soup.select('h1')
        print(title[0].text.strip())
        text = soup.select('.wpb_wrapper p')
        text1 = text[0].text.strip() + text[1].text.strip()
        text2 = ''.join(text1)
        images = soup.select('.vc_single_image-wrapper img')
        imag = [img.get('src') for img in images]
        imag_name = [name.split('/')[-1] for name in imag]


        info = {
            'title': title[0].text.strip(),
            'text': text[0].text.strip() + text[1].text.strip(),
            'text2': text2,
            'images': [img.get('src') for img in images]
        }
        print(info)

        for im, name in zip(imag, imag_name):
            print(name)
            download_image_to_local_media(im, name)

    except Exception as error:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print('Parsing error: ', error, exc_tb.tb_lineno)


def worker(queue: Queue):
    while queue.qsize() > 0:
        url = queue.get()
        print('WORKING ON: ', url)
        with requests.Session() as session:
            responce = session.get(
                url,
                allow_redirects=True,
                timeout=TIME_OUT
            )
            print(responce.status_code)
            status_code = [508, 404, 500, 503, 507]
            for code in status_code:
                if responce.status_code == code:
                    print('page not found: ', url)
                    break
            assert responce.status_code in (200, 301, 302), 'Bad responce'
        process(responce.text, url)
        # except (
        #     requests.Timeout,
        #     requests.ConnectionError,
        #     AssertionError
        # ) as error:
        #     print('Error: ', error)
        #     queue.put(url)
        print(queue.qsize())


def main():
    category_urls = ['https://loveyouplanet.com/blog']

    with requests.Session() as links_session:
        response = links_session.get(category_urls[0])

    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.select('.post-title a')
    links = [link.get('href') for link in links]
    # print(links)

    queue = Queue()


    for url in links[:3]:
        queue.put(url)

    work_num = 5

    with ThreadPoolExecutor(max_workers=work_num) as executor:
        for i in range(work_num):
            executor.submit(worker, queue)

if __name__ == '__main__':
    main()
