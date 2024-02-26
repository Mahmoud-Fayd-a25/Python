# Automating cloud infrastructure tasks on AWS using the Boto3 library, the official AWS SDK for Python
# Install Boto3 (pip install boto3) and configured with appropriate AWS credentials (either through environment variables, shared credential file, or IAM roles).
# Replace placeholder values such as 'ami-12345678', 'my-unique-bucket-name', 'local_file.txt', etc., with actual values specific to your AWS environment.


import boto3

# Example 1: Creating an EC2 instance


def create_ec2_instance():
    ec2 = boto3.client('ec2')
    response = ec2.run_instances(
        ImageId='ami-12345678',
        InstanceType='t3.smale',
        MinCount=1,
        MaxCount=1
    )
    instance_id = response['Instances'][0]['InstanceId']
    print(f"EC2 instance created with ID: {instance_id}")

# Example 2: Creating an S3 bucket


def create_s3_bucket():
    s3 = boto3.client('s3')
    bucket_name = 'my-unique-bucket-name'
    s3.create_bucket(Bucket=bucket_name)
    print(f"S3 bucket '{bucket_name}' created")

# Example 3: Uploading a file to S3 bucket


def upload_file_to_s3():
    s3 = boto3.client('s3')
    bucket_name = 'my-unique-bucket-name'
    file_path = '/path/to/local/file.txt'
    object_name = 'file.txt'
    s3.upload_file(file_path, bucket_name, object_name)
    print(f"File '{object_name}' uploaded to S3 bucket '{bucket_name}'")

# Example 4: Creating an RDS instance


def create_rds_instance():
    rds = boto3.client('rds')
    rds.create_db_instance(
        DBInstanceIdentifier='mydbinstance',
        Engine='mysql',
        DBInstanceClass='db.t2.micro',
        AllocatedStorage=20,
        MasterUsername='admin',
        MasterUserPassword='password',
        DBName='mydatabase'
    )
    print("RDS instance created")

# Example 5: Creating a Lambda function


def create_lambda_function():
    lambda_client = boto3.client('lambda')
    with open('lambda_function.zip', 'rb') as f:
        zipped_code = f.read()
    response = lambda_client.create_function(
        FunctionName='my_lambda_function',
        Runtime='python3.8',
        Role='arn:aws:iam::123456789012:role/lambda-role',
        Handler='lambda_function.handler',
        Code={'ZipFile': zipped_code},
        Description='My Lambda function',
        Timeout=30,
        MemorySize=128
    )
    print(f"Lambda function created with ARN: {response['FunctionArn']}")

# Example 6: Creating an SQS queue


def create_sqs_queue():
    sqs = boto3.client('sqs')
    response = sqs.create_queue(QueueName='my_queue')
    print(f"SQS queue created with URL: {response['QueueUrl']}")

# Example 7: Creating an IAM user


def create_iam_user():
    iam = boto3.client('iam')
    iam.create_user(UserName='myuser')
    print("IAM user created")

# Example 8: Creating an SNS topic


def create_sns_topic():
    sns = boto3.client('sns')
    response = sns.create_topic(Name='my_topic')
    print(f"SNS topic created with ARN: {response['TopicArn']}")

# Example 9: Creating a DynamoDB table


def create_dynamodb_table():
    dynamodb = boto3.client('dynamodb')
    dynamodb.create_table(
        TableName='my_table',
        KeySchema=[
            {'AttributeName': 'id', 'KeyType': 'HASH'}
        ],
        AttributeDefinitions=[
            {'AttributeName': 'id', 'AttributeType': 'S'}
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    print("DynamoDB table created")

# Example 10: Creating a CloudFormation stack


def create_cloudformation_stack():
    cloudformation = boto3.client('cloudformation')
    with open('template.yaml', 'r') as f:
        template_body = f.read()
    response = cloudformation.create_stack(
        StackName='my-stack',
        TemplateBody=template_body,
        Parameters=[
            {'ParameterKey': 'InstanceType', 'ParameterValue': 't2.micro'}
        ],
        Capabilities=['CAPABILITY_NAMED_IAM']
    )
    print(
        f"CloudFormation stack creation initiated with Stack ID: {response['StackId']}")

# Execute all examples


def main():
    print("Example 1:")
    create_ec2_instance()
    print()

    print("Example 2:")
    create_s3_bucket()
    print()

    print("Example 3:")
    upload_file_to_s3()
    print()

    print("Example 4:")
    create_rds_instance()
    print()

    print("Example 5:")
    create_lambda_function()
    print()

    print("Example 6:")
    create_sqs_queue()
    print()

    print("Example 7:")
    create_iam_user()
    print()

    print("Example 8:")
    create_sns_topic()
    print()

    print("Example 9:")
    create_dynamodb_table()
    print()

    print("Example 10:")
    create_cloudformation_stack()
    print()


if __name__ == "__main__":
    main()
