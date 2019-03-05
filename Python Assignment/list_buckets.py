#!/usr/bin/env python3
import boto3
s3 = boto3.resource('s3')

try:
    for bucket in s3.buckets.all():
     print (bucket.name)
     print ("---")
    for item in bucket.objects.all():
     print ("\t%s" % item.key)

except Exception:
    print('No Buckets to Display')
