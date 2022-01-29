##########################################################################
#This Script will get the S3 Bucket encryption and Logging Information
##########################################################################

from pydoc import cli
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


#This method check the Bucket encryption and log details
def GetBucketEncryptionStatus(client,s3BucketList):

    for buckets in s3BucketList:
        response = client.get_bucket_encryption(
            Bucket=buckets,
        )
        
        for resp in response['ServerSideEncryptionConfiguration']['Rules']:
            print(resp)
            for key, value in resp.items():
                print(key, '->', value)

        response = client.get_bucket_logging(
            Bucket=buckets,
        )
        

###############
#Main Method 
###############
def Main():

    client = boto3.client('s3')
    s3BucketList = []
    s3BucketList = ListAllS3Buckets(client)

    GetBucketEncryptionStatus(client,s3BucketList)


if __name__ == "__main__":
    Main()