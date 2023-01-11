import requests

class Dannye:

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }

    response = requests.get('https://jsonplaceholder.typicode.com/posts',
                            headers = headers)




    def __init__(self, json_resp, response):
        self.json_resp = json_resp

    def vyvod(self):
        for i in self.json_resp:
            print(f"Stroka: {i}\n")


data = Dannye("https://jsonplaceholder.typicode.com/posts")
print(data.vyvod())