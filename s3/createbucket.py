import boto3

client = boto3.client('s3')
client.create_bucket(Bucket='mybotoawsbucket')


if __name__ == '__main__':
    print(create_topic)
