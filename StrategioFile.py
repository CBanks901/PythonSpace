import logging

import boto3

from botocore.exceptions import ClientError

logging.basicConfig(level=logging.INFO)

"""
logger = logging.getLogger('iamusers_list')

#Process for listing out all users of my aws console
#create iam client
iam = boto3.client('iam')

#creating starts instance function
def list_iamusers():
    try:
        response = iam.list_users()
        paginator = iam.get_paginator('list_users')
        for response in paginator.paginate():
            for user in response['Users']:
                print(f"Usersname: {user['UserName']}")
        logger.info("listing iam users %s.")
    except ClientError:
        logger.exception("couldn't list i am users %s.")
        raise
    else:
        return response

response = list_iamusers()
"""

"""
#Begin process for creating a new user
logger = logging.getLogger('iamuser')

#create iam client
iam = boto3.client('iam')

username = input('Please enter a name:\n')

def create_user(username):
    try:
        #Take input from screen

        response = iam.create_user(UserName=username)
        logger.info('Created a user %s.', username)
    except ClientError:
        logger.exception("Couldn't create a user %s.", username)
    else:
        return response

response = create_user(username)
#End process for creating a new user
"""

"""
#Being process for granting iam to a user [

logger = logging.getLogger('iamuser')
#Create iam client
iam = boto3.client('iam')

#Take input from screen
username = input('Please enter a name:\n')

def create_iamuser_accesskey(username):
    try:
        response = iam.create_access_key(UserName=username)
        logger.info('Created a user access key %s.', username)
    except ClientError:
        logger.exception("Couldn't create a user access key %s.", username)
    else:
        return response

response = create_iamuser_accesskey(username)
print(response)
#End process for granting a user iam access ]
"""

"""
#Begin process for creating aws console access

logger = logging.getLogger('iamuser_loginprofile')

#Create iam client
iam = boto3.client('iam')

#Take input from screen
username = input('Please enter a name:\n')
password = input('Please enter an 8 letter word/number combo that has at least one uppercase letter and at at least one symbol:\n')

def create_iamuser_loginprofile(username):
    try:
        response = iam.create_login_profile(UserName=username, Password = password)
        logger.info('Created login profile for %s.', username)
    except ClientError:
        logger.exception("Couldn't login profile for %s.", username)
    else:
        return response

def main():
    response = create_iamuser_loginprofile(username)
    print(response)

if __name__ == '__main__':
    main()

#End process for creating aws console access
"""