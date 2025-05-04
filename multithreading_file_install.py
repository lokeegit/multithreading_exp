import requests
import threading
import time

urls = [
    "https://petsworld.in/cdn/shop/articles/How-To-Make-Your-Puppy-Gain-Weight.jpg?v=1730980733",
    "https://www.pedigree.in/files/styles/webp/public/2023-09/Puppy-Nutrition-Image-list.png.webp?VersionId=apbK1AhaKBfwIDQpd3.NcdR9egh41zrq&itok=RC0yZp5l",
    "https://d2zp5xs5cp8zlg.cloudfront.net/image-79498-800.jpg"
]

def download_image(url, index):
    response = requests.get(url)
    with open(f"image_{index}.jpg", "wb") as f:
        f.write(response.content)
    print(f"Downloaded image {index}")

# Sequential download
start = time.time()
for i, url in enumerate(urls):
    download_image(url, i)
end = time.time()
print(f"\nSequential download time: {end - start:.2f} seconds")

# Multithreaded download
start = time.time()
threads = []
for i, url in enumerate(urls):
    t = threading.Thread(target=download_image, args=(url, i))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
end = time.time()
print(f"\nMultithreaded download time: {end - start:.2f} seconds")
