#!/usr/bin/env python3
import sys
import boto3
import time
ec2 = boto3.resource('ec2')

def kill():
    try:
      instancename = input('Please enter I.D. of instance to kill: ')
      instance = ec2.Instance(instancename)
      responce = instance.terminate()
      time.sleep(2)
      print ("Instance Terminated")
      time.sleep(3)

    except Exception:
      print('Please enter a valid I.D.')
      time.sleep(3)

def main():
    kill()

if __name__ == '__main__':
    main()
