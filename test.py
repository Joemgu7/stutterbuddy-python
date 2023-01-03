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

# get all assets of the user
assets = sb.get_all_assets()

for asset in assets:
    print(asset)
    print(asset.to_dict())
    print(asset.to_xml())

# get all jobs of the user
jobs = sb.get_all_jobs()

for job in jobs:
    print(job)
    print(job.to_dict())
    print(job.to_xml())

# Upload a file
file_path = os.getenv("FILE_PATH")
asset_id = sb.upload_file(file_path)

print(f"Asset ID: {asset_id}")

# Submit a job
job = sb.submit_job(asset_id)

print(f"Job: {job}")