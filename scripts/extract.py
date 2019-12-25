import requests
import pandas as pd

# Example API: Replace with a real API or file for your use case
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
data = response.json()

# Convert to DataFrame
df = pd.DataFrame(data)
df.to_csv("data/raw_data.csv", index=False)

print("Data extracted and saved to raw_data.csv")
