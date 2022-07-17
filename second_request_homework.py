from pprint import pprint

import requests

TOKEN = ""

class YandexDisk:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json','Authorization': 'OAuth {}'.format(self.token)}

    def get_yaDisk_link(self, path_to_file):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': path_to_file, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload(self, path_to_file,filename):
        url = self.get_yaDisk_link(path_to_file=path_to_file).get("href", "")
        response = requests.put(url, data=open(filename, 'rb'))


if __name__ == "__main__":
    ya = YandexDisk(token=TOKEN)
    ya.upload(path_to_file = r'C:/Users/Yupal/Documents/6.Работа с библиотекой requests, http запросы', filename='test1.txt')
