import requests
import io
import os

from bs4 import BeautifulSoup


def search_google_images(query):
    url = "https://www.google.com/search?q={}".format(query)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    image_results = soup.find_all("img", class_="rg_i")
    image_urls = [image["src"] for image in image_results]

    return image_urls


def download_images(image_urls, output_directory):
    if not os.path.exists(output_directory):
        os.mkdir(output_directory)

    for image_url in image_urls:
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
