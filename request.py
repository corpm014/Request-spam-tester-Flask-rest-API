import requests
import threading

url = "http://192.168.0.15:8080/login"

data = {"email": "test", "password" :"test"}


def request():
    while True:
        response = requests.get(url)

threads = []

for i in range(1000):
    d = threading.Thread(target=request)
    d.daemon = True
    threads.append(d)

for i in range(1000):
    threads[i].start()

for i in range(1000):
    threads[i].join()
