import requests
import csv
import os
import time
import yaml
from dotenv import find_dotenv, load_dotenv

# Finds and instantiates the .env file
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# Load the YAML configuration file
def load_config(config_file='config.yaml'):
    with open(config_file, 'r') as file:
        return yaml.safe_load(file)

# Variables needed to make the Mockaroo API request string
api_key = os.getenv("API_KEY")  # Passes the value of "API_KEY" from the .env file into the variable "api_key"
base_url = "https://api.mockaroo.com/api/"

# Load the configuration from the YAML file
config = load_config()

# File destination base (can be modified in the config yaml file)
base_file_destination = config["file_destination"]["file_location"]

# Debugging: Print out the loaded config to see its structure
print("Loaded config:", config)

# Extract values from YAML config
schemas = config.get("schema_info", [])
num_of_rows = config.get("script_params", {}).get("num_of_rows")
file_amount = config.get("script_params", {}).get("file_amount")

# Debugging: Print out the 'schemas' variable to verify its structure
print("Schemas:", schemas)

# Function to download and save data to a CSV
def download_data(schema_name, schema_id, num_of_rows, api_key, file_amount):
    # Create a subfolder for the schema within the base file destination
    file_destination = os.path.join(base_file_destination, schema_name)
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
            print(f"\nData download was successful for {schema_name} (file {i + 1})!\nResponse code: {response.status_code}\n")

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
            print(f"Data could not be downloaded from the API for {schema_name} (file {i + 1}). See response status code: {response.status_code}\n")

# Loop through the schemas defined in the YAML file and call the download_data function for each
for schema in schemas:
    # Debugging: Print each schema
    print("Processing schema:", schema)

    schema_name = schema.get("schema_name")
    schema_id = schema.get("schema_id")

    # Ensure both schema_name and schema_id are present before processing
    if schema_name and schema_id:
        print(f"Processing schema: {schema_name} ({schema_id})")
        download_data(schema_name, schema_id, num_of_rows, api_key, file_amount)
    else:
        print(f"Skipping invalid schema: {schema}")
