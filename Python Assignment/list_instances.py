#!/usr/bin/env python3
# Richard Frizby Moodle Notes 
import boto3
ec2 = boto3.resource('ec2')
import time
#Lists all instances
for instance in ec2.instances.all():
  for tag in instance.tags:
      print ('')
      print (' ID:',instance.id, '\n Name:', tag['Value'],'\n State: ',instance.state['Name'],'\n I.P',instance.public_ip_address)
      print ('')
      time.sleep(.2)
      


