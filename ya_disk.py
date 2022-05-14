import requests

class YandexDisk:
    url = 'https://cloud-api.yandex.net'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def check(self, folder):
        folder_url = self.url + '/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': folder}
        req = requests.get(folder_url, headers=headers, params=params)
        return req.status_code

    def create_folder(self, folder):
        folder_url = self.url + '/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': folder}
        req = requests.put(folder_url, headers=headers, params=params)
        return req.status_code

    def delete_folder(self, folder):
        folder_url = self.url + '/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': folder}
        req = requests.delete(folder_url, headers=headers, params=params)
        return req.status_code
