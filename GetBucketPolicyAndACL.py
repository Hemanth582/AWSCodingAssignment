##################################################################################
##This Script will Get the all S3 buckets and it's ACL Rules and Bucket Policy's
###################################################################################

import boto3
import botocore


#This Method will fetch the all buckets and return Buckets List
def ListAllS3Buckets(client):

    response = client.list_buckets()

    bucketList = []
    for resp in response['Buckets']:
        bucketName = resp['Name']
        bucketList.append(bucketName)
    
    return bucketList


#This method can get the Bucket ACL& Policy Details based on Bucket name
def GetBucketACLANDPolicy(s3BucketList,client):

    for bucketName in s3BucketList:

        print("Bucket Name:: ",bucketName)
        response = client.get_bucket_acl(
            Bucket=bucketName,
        )
        for resp in response['Grants']:
            acl = resp['Permission']
            print("Bucket ACL:: ",acl)

        try:

            response = client.get_bucket_policy(
                Bucket=bucketName,
            )
            policy = response['Policy']
            print("Bucket Policy:: ",policy)

        except botocore.exceptions.ClientError as e:
            print("This Bucket doesn't have Policy")


###############
#Main Method 
###############
def Main():

    client = boto3.client('s3')
    s3BucketList = []
    s3BucketList = ListAllS3Buckets(client)
    GetBucketACLANDPolicy(s3BucketList,client)


if __name__ == "__main__":
    Main()