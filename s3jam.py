import boto3
from botocore.client import Config
import io

def uploadObject(bucket, object_name, data):
    bucket.upload_fileobj(data, object_name)

def getBucket(s3, bucket_name):
    return s3.Bucket(bucket_name)

def getBuckets(s3):
    return s3.buckets.all()

def main():
    endpoint = 'https://s3.example.com'
    s3 = boto3.resource('s3',
                        aws_access_key_id='',
                        aws_secret_access_key='',
                        config=Config(
                            signature_version='s3'
                        ),
                        endpoint_url=endpoint)

    data = bytearray([0 for x in range(1024*1024*1024)])
    bytesIo = io.BytesIO(data)
    uploadObject(getBucket(s3, 'hoge'), '1024Mbyteobj', bytesIo)



if __name__ == '__main__':
    main()