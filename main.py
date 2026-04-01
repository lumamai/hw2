import requests
import json
import csv

url = "https://api.github.com/users/octocat/repos"

response = requests.get(url)
data = response.json()

# JSON
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

# CSV
with open("data.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["id", "name", "full_name", "private"])

    for item in data[:10]:
        writer.writerow([
            item["id"],
            item["name"],
            item["full_name"],
            item["private"]
        ])

print("done")