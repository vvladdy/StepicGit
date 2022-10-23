import os
from pytube import YouTube, Playlist, Channel
import requests

def controll_responce(url):
    with requests.Session() as session:
        resp = session.get(url, timeout=20)

        assert resp.status_code == 200, 'Not response'
        print(resp.status_code)
        return resp.status_code

def download_content(status_code, url):
    try:
        os.mkdir('D:/Python/video/')
    except (FileExistsError, Exception) as error:
        print('CATALOG EXIST', error)
    if status_code == 200:
        yt = YouTube(url, )  # ссылка на видео.
        title = yt.title.strip()
        info = {
            'video_name': title,
            'video_description': yt.description,
            'video_subtitle': yt.captions
        }
        with open (f'D://Python/video/{title}.txt', 'w', encoding='utf-8') as \
                file:
            for k, v in info.items():
                file.write('{}: {}\n'.format(k, v))
        #yt.streams.filter(only_audio=True)
        stream = yt.streams.get_by_itag(22)
        streamaudio = yt.streams.get_by_itag(140)
        print(stream)
        print(f'Downloading{yt.title}')
        stream.download('D://Python/video/',
            f'{title}.mp4',
        )
        streamaudio.download(
            'D://Python/video/',
            f'{title}.mp3',
                        )

if __name__ == '__main__':
    url = 'https://www.youtube.com/watch?v=enHWpc77xQk'
    responce = controll_responce(url)
    download_content(responce, url)


# videolist = Playlist('https://www.youtube.com/playlist?list=PLA0M1Bcd0w8xO_39zZll2u1lz_Q-Mwn1F')
# for video in videolist.video_urls:
#     print(video)
#
# videochanel = Channel('https://www.youtube.com/c/INSTARDING/videos')
# print(videochanel.video_urls)
# for i in videochanel.video_urls:
#     print(i.title)
