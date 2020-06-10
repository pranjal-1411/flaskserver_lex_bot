import os
import boto3
from dotenv import load_dotenv


def initEnvironment( rootDir ):
    rootDir='/mnt/f/python3resolve'
    load_dotenv(os.path.join(rootDir, '.env'))
    # os.environ['AWS_ACCESS_KEY_ID'] =  os.getenv('AWS_ACCESS_KEY_ID_PG')
    # os.environ['AWS_SECRET_ACCESS_KEY']= os.getenv('AWS_SECRET_ACCESS_KEY_PG')
    #os.environ['AWS_DEFAULT_REGION'] =  os.getenv('AWS_REGION')

def publish_message_from_slack_to_sns( message,rootDir):
    
    initEnvironment(rootDir)
    TopicArn = os.getenv('AWS_SNS_TOPICARN_SLACK_TO_AWS')
    client = boto3.client('sns')
    response = client.publish(
            TopicArn = TopicArn,
            Message = message
        )

def publish_message_to_ms( message,rootDir):
    
    #initEnvironment(rootDir)
    TopicArn = os.getenv('AWS_SNS_TOPICARN_SERVER_TO_MS')
    client = boto3.client('sns', aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID_PG'),
        aws_secret_access_key= os.getenv('AWS_SECRET_ACCESS_KEY_PG') )
    response = client.publish(
            TopicArn = TopicArn,
            Message = message
        )    
    
    