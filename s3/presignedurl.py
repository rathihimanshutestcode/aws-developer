import boto3
s3client = boto3.client('s3')
#url = s3client.generate_presigned_url('list_buckets', Params = {'Bucket': 'mybotoawsbucket', 'Key': 'g1.jpg'}, ExpiresIn = 120)
url = s3client.generate_presigned_url('get_object', Params = {'Bucket': 'mybotoawsbucket', 'Key': 'g1.jpg'}, ExpiresIn = 120)
print(url)
