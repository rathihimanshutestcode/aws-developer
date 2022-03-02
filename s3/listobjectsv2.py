client = boto3.client('s3')

response = client.list_objects_v2(
    Bucket='examplebucket',
    MaxKeys='2',
)

print(response)


#need of pagination 

s3_client = boto3.client("s3")

result = s3_client.list_objects(Bucket="my-bucket")
for obj in result["Contents"]:
    do_something(obj)
    
    
    
#pagination 

s3_client = boto3.client("s3")

paginator = s3_client.get_paginator("list_objects")
pages = paginator.paginate(Bucket="my-bucket")
for page in pages:
    for obj in page["Contents"]:
        do_something(obj)
