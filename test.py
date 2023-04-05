import os
import requests
from bs4 import BeautifulSoup

# URL of the page with the PDF links
url = "https://docs.tanium.com/pdf.html"

# Send a GET request to the URL and get the HTML content
response = requests.get(url)

# Parse the HTML content with Beautiful Soup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the divs with class 'h2-content-default-collapsed'
divs = soup.find_all("div", class_="h2-content-default-collapsed")

# Loop through all the divs and find the last two PDF links in each div
for div in divs:
    # Get the h2 name
    h2_name = div.find_previous("h2").text
    
    # Create the folder path using the h2 name
    folder_path = os.path.join(".", h2_name)
    os.makedirs(folder_path, exist_ok=True)
    
    # Find the last two PDF links in the div
    pdf_links = div.find_all("a", href=lambda href: href is not None and href.endswith(".pdf"))[-2:]

    # Loop through the last two PDF links and download them
    for link in pdf_links:
        # Get the link URL and file name
        pdf_url = link["href"]
        file_name = os.path.basename(pdf_url)
        
        # Download the PDF file and save it in the folder
        response = requests.get(pdf_url)
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "wb") as f:
            f.write(response.content)
