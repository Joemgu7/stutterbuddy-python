from stutterbuddy import Stutterbuddy
import os
import dotenv

# Load the .env file
dotenv.load_dotenv()

# Get the API key from the .env file
key = os.getenv("API_KEY")

print(f"API key: {key}")

# Create a Stutterbuddy object
sb = Stutterbuddy(key)
# get all jobs of the user
jobs = sb.get_all_jobs()

for job in jobs:
    print(job)

# get all assets of the user
assets = sb.get_all_assets()

for asset in assets:
    print(asset)

# Upload a file
file_path = os.getenv("FILE_PATH")
asset_id = sb.upload_file(file_path, verbose=2)

print(f"Asset ID: {asset_id}")

# Submit a job
job = sb.submit_job(asset_id, verbose=2)

print(f"Job: {job}")