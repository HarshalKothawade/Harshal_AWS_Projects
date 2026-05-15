import boto3
import os
import botocore

bucket_name = "project05-bucket"  # ⚠️ must be globally unique
region = "ap-south-1"

s3 = boto3.client("s3", region_name=region)

# 1. Create bucket (safe)
try:
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': region
        }
    )
    print("Bucket created")
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
        print("Bucket already exists, continuing...")
    else:
        raise

# 2. Upload files
folder_path = "./website"

print("Starting upload...")

for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)

        # keep folder structure
        s3_key = os.path.relpath(file_path, folder_path)

        try:
            s3.upload_file(file_path, bucket_name, s3_key)
            print(f"Uploaded: {s3_key}")
        except Exception as e:
            print(f"Error uploading {file}: {e}")

print("Files uploaded successfully")