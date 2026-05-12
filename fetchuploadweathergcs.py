import requests
import json
from datetime import datetime
from google.cloud import storage

# --- Configuration ---
GCS_BUCKET_NAME = "my-weather-bucket-lanzilot"  
GCS_PROJECT_PATH = "raw/"                   
SERVICE_ACCOUNT_JSON_PATH = "D:/angular/my-project-weather-495900-fea21808657b.json"
# Initialize Google Cloud Storage client (using the service account key)
client = storage.Client.from_service_account_json(SERVICE_ACCOUNT_JSON_PATH)

def upload_json_to_gcs(bucket_name, data, destination_blob_name):
    """Uploads a JSON object to a GCS bucket."""
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_string(data, content_type="application/json")
    print(f"Uploaded {destination_blob_name} to {bucket_name}.")

# Fetch current weather from Open-Meteo API
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 52.52,
    "longitude": 13.41,
    "current_weather": True,
    "hourly": "temperature_2m",
    "timezone": "auto"
}
response = requests.get(url, params=params)
data = response.json()

# Add a server-side timestamp for tracking
data["_fetched_at"] = datetime.utcnow().isoformat()

# Convert the data to a JSON string
json_data = json.dumps(data, indent=4)   # indent is optional and makes the file human-readable

# Create a unique file name
timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
destination_path = f"{GCS_PROJECT_PATH}weather_{timestamp}.json"

# Upload the JSON string to GCS
upload_json_to_gcs(GCS_BUCKET_NAME, json_data, destination_path)