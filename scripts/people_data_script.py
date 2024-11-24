import requests
import csv
import os
import time 
from dotenv import find_dotenv, load_dotenv

# Finds and instantiates the .env file 

dotenv_path = find_dotenv()

load_dotenv(dotenv_path)

# Variables needed to make the Mockaroo API request string

schema_id = "9f46f370"
schema_name = "people_data"
num_of_rows = 5000
api_key = os.getenv("API_KEY") # passes the value of "API_KEY" from the .env file into the variable "api_key"
base_url = "https://api.mockaroo.com/api/"
file_destination = f"C:\\Users\\lyon2\\Desktop\\raw_data\\{schema_name}"

# Ask the user how many files they want to generate (controls how many files are made)
file_amount = int(input("How many files do you want to create? Enter a whole number: "))

# Function to download and save data to a CSV
def download_data(schema_id, num_of_rows, api_key, file_amount):

    # Ensure the directory exists
    if not os.path.exists(file_destination):
        os.makedirs(file_destination)

    for i in range(file_amount):

        # Get a timestamp for unique file naming
        timestamp = time.strftime("%Y%m%d_%H%M%S")

        # Create a unique file name using the timestamp and iteration number
        file_name = f"{schema_name}_{timestamp}.csv"
        file_path = os.path.join(file_destination, file_name)

        # Construct the API URL
        url = f"{base_url}{schema_id}?count={num_of_rows}&key={api_key}"

        # Make the request to the Mockaroo API
        response = requests.get(url)

        print(f"Response content type: {response.headers.get('Content-Type')}")

        if response.status_code == 200:
            print(f"\nData download was successful for file {i + 1}!\nResponse code: {response.status_code}\n")

            # Parse the returned data into CSV format
            data = response.text
            lines = data.splitlines()
            reader = csv.reader(lines)

            # Save the data to a CSV file
            with open(file_path, "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(reader)

            print(f"Data was saved as a CSV in {file_path}.\n")

        else:
            print(f"Data could not be downloaded from the API for file {i + 1}. See response status code: {response.status_code}\n")

# Call the function to download and save the data
download_data(schema_id, num_of_rows, api_key, file_amount)
