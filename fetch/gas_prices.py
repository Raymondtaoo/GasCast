import requests

csv_url = 'https://ontario.ca/v1/files/fuel-prices/fueltypesall.csv'

response = requests.get(csv_url)

if response.status_code == 200:
    # Save the file locally
    with open('data/fuel_prices_ontario.csv', 'wb') as file:
        file.write(response.content)
    print("CSV file downloaded and saved successfully.")
else:
    print(f"Failed to download the file. Status code: {response.status_code}")