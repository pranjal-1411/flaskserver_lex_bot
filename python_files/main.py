
import json
import os
import time
from flask import jsonify
import boto3


from dotenv import load_dotenv

botName = None
botAlias = None
intentName = None

def initEnvironment( rootDir ):
    global botName,botAlias,intentName
    load_dotenv(os.path.join(rootDir, '.env'))
    botName = os.getenv('BOT_NAME')
    botAlias = os.getenv('BOT_ALIAS')
    intentName = os.getenv('INTENT_NAME')
    os.environ['AWS_ACCESS_KEY_ID'] =  os.getenv('AWS_ACCESS_KEY_ID')
    os.environ['AWS_SECRET_ACCESS_KEY']= os.getenv('AWS_SECRET_ACCESS_KEY')
    os.environ['AWS_DEFAULT_REGION'] =  os.getenv('AWS_REGION','ap-southeast-2')


def generateResponse( message ,rootDir):
     
    initEnvironment( rootDir )
    
    sender_id = message['sender']['id']
    response = None
    if message['message'].get('attachment'):
        text = 'Spent Rs 58 on food today'
        response = sendTextToLex( text,sender_id )
    
    elif message['message'].get('text'):
        response = sendTextToLex( message['message']['text'],sender_id )
    
    messageArray = [] 
    
    if response is None : 
        messageArray.append('Some error occured. Please try again')
        return messageArray
    
    if response['message'][0] == '{':
        response_json = json.loads(response['message'])
        for message in response_json['messages']:
            messageArray.append( message['value'] )
    else :
        messageArray.append( response['message'] )    
    
  
    finalMessageArray = []
    unix_timestamp = time.time()
    
    for message in messageArray:
        temp_dic = {
            "by":"server",
            "text":message,
            "time":unix_timestamp
        }
        finalMessageArray.append(temp_dic)
    response = { "messages": finalMessageArray }
    return  response
 
def sendTextToLex( message , sender_id  ):
    
    client = boto3.client('lex-runtime')
    response = client.post_text(
        botName= botName ,
        botAlias= botAlias,
        userId=sender_id,
        sessionAttributes={},
        requestAttributes={},
        inputText=message
    )
    return response


     
if __name__ == "__main__":
   
    message =   {
        'sender': {
            'id': '1234'
        }, 
        'message': {
          'text': 'Hi'
        }
    }
    generateResponse( message )
