import os
import csv
import requests

# Fetch data from API
response = requests.get("https://api.covidtracking.com/v1/us/daily.json")
data = response.json()

# Define your exact target path
output_folder = os.path.expanduser("~/Documents/IA_Bootcamp/2_proyectos/covid-datathon")
output_path = os.path.join(output_folder, "covid_data.csv")

# Create directory if it doesn't exit
os.makedirs(output_folder, exist_ok=True)

# Write to CSV
with open('covid_data.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
    writer.writeheader()  # Write column headers
    writer.writerows(data)  # Write all rows

print(f"✅ Data successfully saved to:\n{output_path}")