import boto3

bucket = 'useastonebucketaws'
key = 'test.html'
s3 = boto3.resource('s3')
versions = s3.Bucket(bucket).object_versions.filter(Prefix=key)

for version in versions:
    obj = version.get()
    print(obj.get('VersionId'), obj.get('ContentLength'), obj.get('LastModified'))
