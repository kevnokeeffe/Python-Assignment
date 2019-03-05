#!/usr/bin/env python3

import boto3
import subprocess
import time
from subprocess import *
s3 = boto3.resource('s3')
ec2 = boto3.resource('ec2')

def add_file():
    subprocess.call(['python3','list_buckets.py'])

    try:
        bucket = input('\nPlease type in the name of the bucket you wish to choose a file from: ')
        url = input('\nPlease type in the name of the file you wish to copy to the Index page: ')
        file_url = "https://s3-eu-west-1.amazonaws.com/" + bucket + "/" + url
        index = open("index.html", "w")
        img_tag = "<img src='{}'>".format(file_url)
        index.write(img_tag)
        index.close()
        for instance in ec2.instances.all():
          for tag in instance.tags:
            print (' ID:',instance.id, '\n Name:', tag['Value'],'\n State: ',instance.state['Name'],'\n I.P',instance.public_ip_address)
            print ('')
            time.sleep(.2)
    except Exception:
            print('Enter Valid Details!')

    try:
        ip = input('\nPlease type in the I.P. of the instance you wish to upload to: ')
        touch_index = 'ssh -i assignment_key.pem ec2-user@'+ip+' sudo touch /var/www/html/index.html'
        change_permissions = 'ssh -i assignment_key.pem ec2-user@'+ip+' sudo chmod 777 /var/www/html/index.html'
        scp_index = 'scp -i assignment_key.pem index.html ec2-user@'+ip+':/var/www/html/'

        run(touch_index, check=True, shell=True)
        run(change_permissions, check=True, shell=True)
        run(scp_index, check=True, shell=True)

    except Exception:
            print('Enter Valid Details!')
 

# Define a main() function
def main():
    add_file()

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()


