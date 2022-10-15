import os
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
import requests
from pytube import YouTube, Playlist
from pprint import pprint

TIMEOUT = 20

def process(url):
    try:
        os.mkdir('D:/Django From Youtube/')
    except FileExistsError as error:
        print('CATALOG EXIST', error)
    yt = YouTube(url)
    title = yt.title.split('|')[0].replace('.', '_').rstrip()
    info = {
        'url': url,
        'title': title,
        'description': yt.description
    }
    # pprint(info)
    with open(f'D:/Django From Youtube/{title}.txt', 'w') as file:
        for k, v in info.items():
            file.write('{}: {}\n'.format(k, v))
    stream = yt.streams.get_by_itag(22)
    stream.download(
        'D:/Django From Youtube/',
        f'{title}.mp4'
    )


def parser_for_queue(queue: Queue):
    while queue.qsize() > 0:
        url = queue.get()
        print('WORKING ON: ', url)
        with requests.Session() as session:
            responce = session.get(
                url,
                allow_redirects=True,
                timeout=TIMEOUT
            )
            print(responce.status_code)
            status_code = [508, 404, 500, 503, 507]
            for code in status_code:
                if responce.status_code == code:
                    print('page not found: ', url)
                    # queue.put(url)
                    break
            assert responce.status_code in (200, 301, 302), 'Bad responce'
        process(url)
        print(queue.qsize())


def main():
    url = 'https://www.youtube.com/playlist?list=PLA0M1Bcd0w8xO_39zZll2u1lz_Q-Mwn1F'
    with requests.Session() as session:
        responce = session.get(url, timeout=TIMEOUT)
        assert responce.status_code == 200, 'Bad Response'

        urls = Playlist(url)

        queue = Queue()

        for i in urls.video_urls:
            queue.put(i)

        work_num = 4

        with ThreadPoolExecutor(max_workers=work_num) as executor:
            for i in range(work_num):
                executor.submit(parser_for_queue, queue)

if __name__ == '__main__':
    main()