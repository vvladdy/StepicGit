import sys
import os
from pytube import YouTube, Playlist, Channel
import requests
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QWidget, QLabel, QInputDialog, QMenuBar, \
    QMenu, QHBoxLayout


class Ui_Downloader():
    def __init__(self, radioqueuelist=None, cond_dict=None):
        if cond_dict is None:
            cond_dict = {}
        if radioqueuelist is None:
            radioqueuelist = []
        self.radioqueuelist = radioqueuelist
        self.cond_dict = cond_dict


    def setupUi(self, Downloader):
        Downloader.setObjectName("Downloader")
        Downloader.resize(513, 197)
        Downloader.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.UrlField = QtWidgets.QLineEdit(Downloader)
        self.UrlField.setGeometry(QtCore.QRect(20, 10, 481, 31))
        self.UrlField.setStyleSheet("background-color: rgb(207, 255, 255);")
        # self.UrlField.setIndent(2)
        self.UrlField.setObjectName("UrlField")
        self.DownloadButton = QtWidgets.QPushButton(Downloader)
        self.DownloadButton.setGeometry(QtCore.QRect(20, 50, 231, 31))
        self.DownloadButton.setObjectName("DownloadButton")
        self.AddSingleURL = QtWidgets.QRadioButton(Downloader)
        self.AddSingleURL.setGeometry(QtCore.QRect(20, 90, 82, 17))
        self.AddSingleURL.setObjectName("AddSingleURL")

        self.AddPlaylist = QtWidgets.QRadioButton(Downloader)
        self.AddPlaylist.setGeometry(QtCore.QRect(20, 120, 82, 17))
        self.AddPlaylist.setObjectName("AddPlaylist")

        self.AddChanel = QtWidgets.QRadioButton(Downloader)
        self.AddChanel.setGeometry(QtCore.QRect(20, 150, 82, 17))
        self.AddChanel.setObjectName("AddChanel")


        self.OnlyVideoRadioButton = QtWidgets.QCheckBox(Downloader)
        self.OnlyVideoRadioButton.setGeometry(QtCore.QRect(160, 110, 82, 17))
        self.OnlyVideoRadioButton.setObjectName("OnlyVideoRadioButton")
        self.OnlyVideoRadioButton.setChecked(False)

        self.VideoAudioRadioButton = QtWidgets.QCheckBox(Downloader)
        self.VideoAudioRadioButton.setGeometry(QtCore.QRect(160, 130, 82, 17))
        self.VideoAudioRadioButton.setObjectName("VideoAudioRadioButton")
        self.VideoAudioRadioButton.setChecked(False)

        self.OnlyAudioRadioButton = QtWidgets.QCheckBox(Downloader)
        self.OnlyAudioRadioButton.setGeometry(QtCore.QRect(160, 90, 82, 17))
        self.OnlyAudioRadioButton.setObjectName("OnlyAudioRadioButton")
        self.OnlyAudioRadioButton.setChecked(False)

        self.TextUnderVideoRadioBatton = QtWidgets.QCheckBox(Downloader)
        self.TextUnderVideoRadioBatton.setGeometry(QtCore.QRect(160, 150, 111, 17))
        self.TextUnderVideoRadioBatton.setObjectName("TextUnderVideoRadioBatton")
        self.TextUnderVideoRadioBatton.setChecked(False)

        self.ExitButton = QtWidgets.QPushButton(Downloader)
        self.ExitButton.setGeometry(QtCore.QRect(404, 152, 91, 31))
        self.ExitButton.setObjectName("ExitButton")

        self.retranslateUi(Downloader)
        QtCore.QMetaObject.connectSlotsByName(Downloader)

        self.add_function() # метод для добавления событий при нажатии на кнопки


    def retranslateUi(self, Downloader):
        _translate = QtCore.QCoreApplication.translate
        Downloader.setWindowTitle(_translate("Downloader", "YouTube Downloader"))
        self.UrlField.setText(_translate("Downloader", ''))
        self.DownloadButton.setText(_translate("Downloader", "DownLoad"))

        self.AddSingleURL.setText(_translate("Downloader", "Single Url"))
        self.AddSingleURL.method = 'SingleUrlTest'

        self.AddPlaylist.setText(_translate("Downloader", "PlayList"))
        self.AddPlaylist.method = 'PlaylistTest'

        self.AddChanel.setText(_translate("Downloader", "Chanel"))
        self.AddChanel.method = 'ChanellistTest'

        self.OnlyVideoRadioButton.setText(_translate("Downloader", "Only Video"))

        self.VideoAudioRadioButton.setText(_translate("Downloader", "Video+Audio"))

        self.OnlyAudioRadioButton.setText(_translate("Downloader", "Only Audio "))
        self.TextUnderVideoRadioBatton.setText(_translate("Downloader", "Txt info"))
        self.ExitButton.setText(_translate("Downloader", "Exit"))
    # def single_download(self):

    def is_checkboxTrue(self):
        self.cond_dict = {}
        if self.OnlyAudioRadioButton.isChecked() == True:
            self.audio = 'audio'
            # print('OnlyAudioTrue')
            self.cond_dict['audio'] = self.audio
        if self.OnlyVideoRadioButton.isChecked() == True:
            # print('OnlyVideoTrue')
            self.video = 'video'
            self.cond_dict['video'] = self.video
        if self.VideoAudioRadioButton.isChecked() == True:
            # print('VideoAudioTrue')
            self.audiovideo = 'audiovideo'
            self.cond_dict['audiovideo'] = 'audiovideo'
        if self.TextUnderVideoRadioBatton.isChecked() == True:
            # print('TextTrue')
            self.text = 'text'
            self.cond_dict['text'] = 'text'

        return self.cond_dict

    def radioButtonText(self):
        text_single = self.AddSingleURL
        text_playlist = self.AddPlaylist
        text_channel = self.AddChanel
        if text_single.isChecked():
            # print('Radio{}'.format(self.AddSingleURL.method))
            self.radioqueuelist.append(self.AddSingleURL.method)
        elif text_playlist.isChecked():
            # print('Radio {}'.format(self.AddPlaylist.method))
            self.radioqueuelist.append(self.AddPlaylist.method)
        elif text_channel.isChecked():
            # print('Radio {}'.format(self.AddChanel.method))
            self.radioqueuelist.append(self.AddChanel.method)
        # print(self.radioqueuelist[0])
        lastelement = self.radioqueuelist
        return str(lastelement[-1])

    def add_function(self):
        self.DownloadButton.clicked.connect(self.download_request)
        self.ExitButton.clicked.connect(app.quit)
        self.AddSingleURL.clicked.connect(self.radioButtonText)
        self.AddPlaylist.clicked.connect(self.radioButtonText)
        self.AddChanel.clicked.connect(self.radioButtonText)

        self.OnlyAudioRadioButton.clicked.connect(self.is_checkboxTrue)
        self.OnlyVideoRadioButton.clicked.connect(self.is_checkboxTrue)
        self.VideoAudioRadioButton.clicked.connect(self.is_checkboxTrue)
        self.TextUnderVideoRadioBatton.clicked.connect(self.is_checkboxTrue)


    def controll_responce(self, url):
        # print(url)
        with requests.Session() as session:
            resp = session.get(url, timeout=20)

            assert resp.status_code == 200, 'Not response'
            return resp.status_code

    def parser_for_queue(self, queue: Queue):
        while queue.qsize() > 0:
            url_from_queue = queue.get()
            print('WORKING ON: ', url_from_queue)
            with requests.Session() as session:
                responce = session.get(
                    url_from_queue,
                    allow_redirects=True,
                    timeout=20
                )
                print(responce.status_code)
                status_code = [508, 404, 500, 503, 507]
                for code in status_code:
                    if responce.status_code == code:
                        print('page not found: ', url_from_queue)
                        # queue.put(url)
                        break
                assert responce.status_code in (200, 301, 302), 'Bad responce'
            print(queue.qsize())
            self.download_content(200, url_from_queue)

    def download_playlist(self, status_code, url):
        if status_code == 200:
            urls = Playlist(url)
            self.queue = Queue()

            for i in urls.video_urls:
                self.queue.put(i)

            work_num = 1

            with ThreadPoolExecutor(max_workers=work_num) as executor:
                for i in range(work_num):
                    executor.submit(self.parser_for_queue, self.queue)

    def download_channel(self, status_code, url):
        if status_code == 200:
            urls = Channel(url)
            self.queue = Queue()

            for i in urls.video_urls:
                self.queue.put(i)

            work_num = 1

            with ThreadPoolExecutor(max_workers=work_num) as executor:
                for i in range(work_num):
                    executor.submit(self.parser_for_queue, self.queue)

    def download_only_text(self):
        print(f'Saving in: C:/DownLoadYouTube as: {self.title}.txt')
        with open(f'C:/DownLoadYouTube/{self.title}.txt', 'w',
        encoding='utf-8') as file:
            for k, v in self.info.items():
                file.write('{}: {}\n'.format(k, v))

    def download_only_audio(self):
        streamaudio = self.yt.streams.get_by_itag(140)
        print(f'Saving in: C:/DownLoadYouTube as {self.title}.txt')
        streamaudio.download(
            'C:/DownLoadYouTube/',
            f'{self.title}.mp3',
        )

    def download_only_video(self):
        stream = self.yt.streams.get_by_itag(137)
        print(f'Saving in: C:/DownLoadYouTube as Vid{self.title}.mp4')
        stream.download('C:/DownLoadYouTube/',
                        f'Vid{self.title}.mp4',
                        )

    def download_video_audio(self):
        stream = self.yt.streams.get_by_itag(22)
        print(f'Saving in: C:/DownLoadYouTube as {self.title}.mp4')
        stream.download('C:/DownLoadYouTube/',
                        f'{self.title}.mp4',
                        )

    def catalog_create(self):
        try:
            os.mkdir('C:/DownLoadYouTube/')
        except (FileExistsError, Exception) as error:
            print('CATALOG EXIST', error)

    def download_content(self, status_code, url):

        if status_code == 200:
            self.yt = YouTube(url, ) # ссылка на видео
            title = re.sub(r'[^\w\s]', '', self.yt.title)
            # title = self.yt.title.replace('.', ' ').replace(':', ' ').strip().split(' ')[:3]
            # self.title = '-'.join(title)
            self.title = title

            self.info = {
                'video_name': self.yt.title,
                'video_description': self.yt.description,
                'video_subtitle': self.yt.captions
            }

            for key, func in self.cond_dict.items():
                # print(key, func)
                print('downloading...', key)
                if key == 'audio':
                    self.download_only_audio()
                print('downloading...', key)
                if key == 'text':
                    self.download_only_text()
                print('downloading...', key)
                if key == 'video':
                    self.download_only_video()
                print('downloading...', key)
                if key == 'audiovideo':
                    self.download_video_audio()
            print('Downloading Finished!!!')

    def download_request(self):
        textboxValue = self.UrlField.text()
        url = textboxValue #'https://www.youtube.com/watch?v=enHWpc77xQk'
        responce = self.controll_responce(url)
        # print(self.is_checkboxTrue())
        self.catalog_create()
        if self.radioButtonText() == self.AddSingleURL.method:
            self.download_content(responce, url)

        elif self.radioButtonText() == self.AddPlaylist.method:
            print(self.AddPlaylist.method)
            self.download_playlist(responce, url)

        elif self.radioButtonText() == self.AddChanel.method:
            print(self.AddChanel.method)
            self.download_channel(responce, url)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Downloader = QtWidgets.QDialog()
    ui = Ui_Downloader()
    ui.setupUi(Downloader)
    Downloader.show()
    sys.exit(app.exec_())
