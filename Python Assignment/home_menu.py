#!/usr/bin/python3

# Text menu in Python
# Using the subprocess module to execute a command http://www.sharats.me/posts/the-ever-useful-and-neat-subprocess-module/
#
import os
import subprocess

# Menu deisgn
def print_menu():
    print ('')
    print (10 * "-", "Menu" , 29 * "-")
    print ("|")
    print ("|",4 * "-", "Instance Options" , 4 * "-")
    print ("|1. Create a New Instance  |")
    print ("|2. List Instances         |")
    print ("|3. Terminate Instance     |")
    print ("|                          |")
    print ("|",5 * "-", "Bucket options", 5*"-")
    print ("|4. Create a New Bucket")
    print ("|5. List Buckets")
    print ("|6. Delete Bucket")
    print ("|7. Put Bucket")
    print ("|8. Put a file from a Bucket to an Instance")
    print ("|0. Exit")
    print (45 * "-")

loop = True

# While loop continues until loop = False
while loop:
    # Displays the menu above
    print_menu()
    choice = input("Please select an option: ")

    if choice == "1":
        subprocess.call(['python3', 'create_instance.py'])
        print (2 * '\n')
    elif choice == "2":
        subprocess.call(['python3', 'list_instances.py'])
        print (2 * '\n')
    elif choice == "3":
        subprocess.call(['python3', 'terminate_instances.py'])
        print (2 * '\n')
    elif choice == "4":
        subprocess.call(['python3', 'create_bucket.py'])
        print (2 * '\n')
    elif choice == "5":
        subprocess.call(['python3', 'list_buckets.py'])
        print (2 * '\n')
    elif choice == "6":
        subprocess.call(['python3', 'delete_buckets.py'])
        print (2 * '\n')
    elif choice == "7":
        subprocess.call(['python3', 'put_bucket.py'])
        print (2 * '\n')
    elif choice == "8":
        subprocess.call(['python3', 'add_file.py'])
        print (2 * '\n')
    elif choice == "0":
        # loop set to False, exits menu
        print("Exiting menu")
        loop = False
    else:
        # Clears the screen and prints an error message for invalid input
        os.system('clear')
        print('Please enter a valid option')
