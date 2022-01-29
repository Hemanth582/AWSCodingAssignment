##################################################################################
##This Script will Get the all S3 buckets policies and ACL
###################################################################################
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


#This method Get the all S3 buckets policies and ACL
def GetAllBucketPolicyAndACL(client,s3BucketList):

    for bucketName in s3BucketList:

        try:

            print("Bucket Name:: ",bucketName)
            response = client.get_bucket_policy_status(Bucket=bucketName,)
            #print(response)
            status = response['PolicyStatus']['IsPublic']
            print(status)
            if(status == 'True'):
                print("this bucket is public")
            else:
                print("this bucket is private")

        except botocore.exceptions.ClientError as e:
            print("This Bucket doesn't have Policy....")

        try:

            response = client.get_public_access_block(Bucket=bucketName)
            #print(response)
            acl = response['PublicAccessBlockConfiguration']['BlockPublicAcls']
            blockPublicPolicy =response['PublicAccessBlockConfiguration']['BlockPublicPolicy']
            restrictPublicBuckets = response['PublicAccessBlockConfiguration']['RestrictPublicBuckets']
            ignorePublicacl = response['PublicAccessBlockConfiguration']['IgnorePublicAcls']

            print("ACL Rule :: block public access control lists ::" ,acl)
            print("Block Public Policy:: ",blockPublicPolicy)
            print("RestrictPublicBuckets is:: ",restrictPublicBuckets)
            print("ignore public ACLs for this bucket:: ",ignorePublicacl)
            

        except botocore.exceptions.ClientError as e:
            print("This Bucket doesn't have Policy")


###############
#Main Method 
###############
def Main():

    client = boto3.client('s3')
    s3BucketList = []
    s3BucketList = ListAllS3Buckets(client)
    GetAllBucketPolicyAndACL(client,s3BucketList)



if __name__ == "__main__":
    Main()
