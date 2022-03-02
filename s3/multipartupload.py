import boto3
import os

s3client = boto3.client('s3')

#print(s3client.list_object_versions(Bucket='marchonebucket-hereawsdev-1'))


s3_resource = boto3.resource('s3')
from boto3.s3.transfer import TransferConfig
config = TransferConfig(multipart_threshold=1024 * 20,
                        max_concurrency=10,
                        multipart_chunksize=1024 * 20,
                        use_threads=True)

bucket_name = 'marchonebucket-hereawsdev-2'
def multipart_upload_boto3():

    file_path = '/Users/himanshurathi/Desktop/largepdf.pdf'
    key = 'largepdf.pdf'

    s3_resource.Object(bucket_name, key).upload_file(file_path,
                            ExtraArgs={'ContentType': 'text/pdf'},
                            Config=config
                            )

print(multipart_upload_boto3())
