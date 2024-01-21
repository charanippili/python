import multiprocessing
import requests

def download(url, name):
    print(f"starting downloading {name}")
    response = requests.get(url)
    open(f"C:/Users/chara/Desktop/tutorial/file{name}.jpg", "wb").write(response.content)
    print(f"finished downloading{name}")

if __name__ == "__main__":
    url = "https://picsum.photos/2000/3000"

    pros = []
    for i in range(5):
        download(url, i)
        p = multiprocessing.Process(target = download, args = [url, i])
        p.start()
        pros.append(p)

    for p in pros:
        p.join()
