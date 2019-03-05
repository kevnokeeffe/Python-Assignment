#!/usr/bin/env python3

import sys
import boto3
import os
import time

s3 = boto3.resource("s3")

def put_bucket():
    for bucket in s3.buckets.all():
        print ('\nList of buckets:')
        print (bucket.name)

    bucket = input('\nEnter the name of the bucket you want to upload to: ')
    file = input('\nEnter the file name you wish to upload to ' + bucket + ': ')
    try:
        time.sleep(3)
        response = s3.Object(bucket, file).put(ACL='public-read', ContentType='image/jpeg',Body=open(file, 'rb'))
        print ("\nFile has been uploaded successfully")
        time.sleep(3)
    except Exception as error:
        print (error)

def main():
    put_bucket()

#Call the main() function.
if __name__ == '__main__':
    main()
