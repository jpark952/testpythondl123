import requests

# URL of the file to download
url = "https://files.pythonhosted.org/packages/8d/59/dfafae6747926ac8200e303cd45bcf1c152ee569dfad64accb12ab7276e0/tiktoken-0.3.0.tar.gz"

# Send a GET request to the URL and get the response
response = requests.get(url)

# Get the file name from the URL
file_name = url.split("/")[-1]

# Save the downloaded file
with open(file_name, "wb") as f:
    f.write(response.content)

print(f"{file_name} downloaded successfully.")
