import re
import requests
import os

with open("okcubid.txt", 'r', encoding='utf-8') as file:
    string = file.read()
subStr = re.findall(r'background-image: url\(&quot;(.+?)&quot', string)


def download_image(url, folder, counter):
    print(str(counter)+". image is downloading..")
    # Create the 'images' folder if it doesn't exist
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Extract the filename from the URL
    filename = url.split('/')[-1]
    filepath = os.path.join(folder, filename)

    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Save the image to the specified filepath
            with open(filepath, 'wb') as file:
                file.write(response.content)
            print(f"Image downloaded successfully: {filepath}")
        else:
            print("Failed to download image.")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")

for x in range(subStr.__len__()):
  download_image(subStr[x],"images",x)