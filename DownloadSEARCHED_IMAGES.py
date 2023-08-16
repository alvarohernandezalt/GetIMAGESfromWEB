import requests
import os
from bs4 import BeautifulSoup


def search_google_images(query):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    url = "https://www.google.com/search?q={}".format(query)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    image_results = soup.find_all("img", class_="t0fcAb")
    image_urls = [image["src"] for image in image_results if "src" in image.attrs]

    return image_urls


def download_images(image_urls, output_directory):
    if not os.path.exists(output_directory):
        os.mkdir(output_directory)

    num_images = 3
    for i, image_url in enumerate(image_urls):
        if i == num_images:
            break

        image_name = image_url.split("/")[-1]
        image_path = os.path.join(output_directory, image_name)

        response = requests.get(image_url)
        with open(image_path, "wb") as f:
            f.write(response.content)


def main():
    query = input("Enter the query: ")
    output_directory = query.replace(" ", "_")

    image_urls = search_google_images(query)
    download_images(image_urls, output_directory)


if __name__ == "__main__":
    main()
