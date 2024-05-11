import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
with open('archivo.txt', 'rb') as data:
    s3.Bucket('almacenamento').put_object(key='archivo.txt', Body=data)
