client = boto3.client('s3')

response = client.list_objects_v2(
    Bucket='examplebucket',
    MaxKeys='2',
)

print(response)
