import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('mybotoawsbucket')
bucket.upload_file('/root/g1.jpg','g1.jpg')
