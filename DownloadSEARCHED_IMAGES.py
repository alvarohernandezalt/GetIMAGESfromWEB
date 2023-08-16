import os
import requests

API_KEY = "YOUR_GOOGLE_API_KEY"
SEARCH_ENGINE_ID = "YOUR_SEARCH_ENGINE_ID"


def search_google_images(query):
    url = f"https://www.googleapis.com/customsearch/v1"
    params = {"key": API_KEY, "cx": SEARCH_ENGINE_ID, "q": query, "searchType": "image"}
    response = requests.get(url, params=params)
    data = response.json()

    image_urls = [item["link"] for item in data.get("items", [])]
    return image_urls


def download_images(image_urls, output_directory):
    if not os.path.exists(output_directory):
        os.mkdir(output_directory)

    num_images = 3
    for i, image_url in enumerate(image_urls):
        if i == num_images:
            break

        image_name = os.path.basename(image_url)
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
