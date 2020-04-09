import os
import boto3
from dotenv import load_dotenv


def initEnvironment( rootDir ):
    load_dotenv(os.path.join(rootDir, '.env'))
    os.environ['AWS_ACCESS_KEY_ID'] =  os.getenv('AWS_ACCESS_KEY_ID')
    os.environ['AWS_SECRET_ACCESS_KEY']= os.getenv('AWS_SECRET_ACCESS_KEY')
    os.environ['AWS_DEFAULT_REGION'] =  os.getenv('AWS_REGION')

def publish_message_from_slack_to_sns( message,rootDir):
    
    initEnvironment(rootDir)
    TopicArn = os.getenv('AWS_SNS_TOPICARN_SLACK_TO_AWS')
    client = boto3.client('sns')
    response = client.publish(
            TopicArn = TopicArn,
            Message = message
        )
    
    
    