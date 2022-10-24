from googletrans import Translator
import pdfplumber
from gtts import gTTS # конвертация текста в аудио
from pathlib import Path

path = 'D:/My/OGVZ Alfa/AkceptGD.pdf'

def pdf_to_txt(path, language='en'):
    if Path(path).is_file() and Path(path).suffix == '.pdf':
        print('File exist')

        with pdfplumber.PDF(open(file=path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        text = ''.join(pages)
        text = text.replace('\n', '')
        # print(text)
        # with open('file.txt', 'w', encoding='utf-8') as file:
        #     file.writelines(text)
        # with open('file.txt', 'r', encoding='utf-8') as file:
        #     text = file.read()[0:3000]
        transl = Translator()
        translation = transl.translate(text=text[100:300], src='auto',
                                       dest='en')

        # перевод текста в аудио, предварительно конвертнув с pdf
        my_audio = gTTS(text=text, lang='uk', slow=False)
        file_name = Path(path).stem
        my_audio.save(f'{file_name}.mp3')
        return f'{translation.text} in audio records success!!!'
    else:
        return 'File does not exist'

def text_translator(text='Громадянин України', scr='auto', dest='en'):
    print(text)
    try:
        transl = Translator()
        translation = transl.translate(text=text, src=scr, dest=dest)
        return translation.text
    except Exception as err:
        return err

def main():
    print(text_translator())
    print(pdf_to_txt(path))
if __name__ == '__main__':
    main()

