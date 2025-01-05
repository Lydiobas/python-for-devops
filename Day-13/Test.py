# import boto3

# client = boto3.client('s3')
# response = client.create_bucket(
#     Bucket='taniform-bucket1',
# )
# print(response)	
# # This code will create a bucket



# import boto3

# client = boto3.client('s3')

# # Create a bucket
# client.create_bucket(
#     Bucket='taniform-bucket1',
# )

# # List buckets
# response = client.list_buckets()

# # Print bucket names
# for bucket in response['Buckets']:
#     print(bucket['Name'])
    
# #This code will list the buckets in your account and print out the bucket names
import boto3

client = boto3.client('s3')

buckets_to_delete = ['taniform-bucket', 'taniform-bucket1', ]

for bucket_name in buckets_to_delete:
    try:
        # Delete all objects in the bucket before deleting the bucket itself
        response = client.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            for obj in response['Contents']:
                client.delete_object(Bucket=bucket_name, Key=obj['Key'])
        
        # Delete the bucket
        client.delete_bucket(Bucket=bucket_name)
        print(f"Deleted bucket: {bucket_name}")
    except Exception as e:
        print(f"Error deleting bucket {bucket_name}: {e}")
