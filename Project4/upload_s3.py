import boto3

# Initialize S3 client
s3 = boto3.client('s3')

bucket_name = "project04-bucket04"  # same as previous step
file_name = "text.txt"
object_name = "uploaded/test.txt"  # path inside S3

# Upload file
s3.upload_file(file_name, bucket_name, object_name)

print("File uploaded successfully!")