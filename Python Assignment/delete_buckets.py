#!/usr/bin/env python3
import sys
import boto3
import subprocess
s3 = boto3.resource('s3')

def delbuck():

    try:
        subprocess.call(['python3','list_buckets.py'])
        bucketname = input('Please enter name of bucket to kill: ')
        bucket = s3.Bucket(bucketname)

        for key in bucket.objects.all():
            try:
                response = key.delete()
                print ('Contents Deleted')
            except Exception as error:
                print ('No Contents to Delete')
        response = bucket.delete(bucketname)
        print ('Bucket Deleted')
    except Exception:
        print ('No Buckets')

def main():
    delbuck()

if __name__ == '__main__':
    main()
