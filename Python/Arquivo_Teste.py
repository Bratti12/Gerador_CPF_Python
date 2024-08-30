import threading
import time
import random
from abc import ABC, abstractmethod


class AbstractFile(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def download(self):
        pass

    @abstractmethod
    def process(self):
        pass


class ImageFile(AbstractFile):
    def download(self):
        print(f"[Download]: Baixando imagem '{self.name}'...")
        time.sleep(random.uniform(0.5, 2)) 
        print(f"[Download]: Imagem '{self.name}' baixada com sucesso.")

    def process(self):
        print(f"[Processamento]: Processando a imagem '{self.name}'...")


class VideoFile(AbstractFile):
    def download(self):
        print(f"[Download]: Baixando vídeo '{self.name}'...")
        time.sleep(random.uniform(1, 3))  
        print(f"[Download]: Vídeo '{self.name}' baixado com sucesso.")

    def process(self):
        print(f"[Processamento]: Processando o vídeo '{self.name}'...")


def download_and_process(file_obj):
    file_obj.download()
    file_obj.process()


files = [
    ImageFile("foto1.jpg"),
    VideoFile("video1.mp4"),
    ImageFile("foto2.jpg"),
    VideoFile("video2.mp4")
]


threads = []


for file in files:
    thread = threading.Thread(target=download_and_process, args=(file,))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()

print("Todos os arquivos foram baixados e processados.")
