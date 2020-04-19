
import json
import os
import time
from flask import jsonify
import boto3


from python_files.aws_helper.lex_intent_mapper import _main_map_lex_intent

from dotenv import load_dotenv
import logging 
botName = None
botAlias = None
intentName = None

def initEnvironment( rootDir ):
    global botName,botAlias,intentName
    load_dotenv(os.path.join(rootDir, '.env'))
    botName = os.getenv('BOT_NAME')
    botAlias = os.getenv('BOT_ALIAS')
    #intentName = os.getenv('INTENT_NAME')
    os.environ['AWS_ACCESS_KEY_ID'] =  os.getenv('AWS_ACCESS_KEY_ID')
    os.environ['AWS_SECRET_ACCESS_KEY']= os.getenv('AWS_SECRET_ACCESS_KEY')
    os.environ['AWS_DEFAULT_REGION'] =  os.getenv('AWS_REGION')


def generateResponse( message ,rootDir ,query = None ,  source = None ):
     
    initEnvironment( rootDir )
    
    logging.info( f'Message Json received in generate response is {message}' )
    sender_id = message['sender']['id']
    response = None
     
    if message['message'].get('text'):
        response = sendTextToLex( message['message']['text'],sender_id )
    
    messageArray = [] 
    if response is None : 
        temp_dic = {
            "by":"server",
            "text":message,
            "time":time.time()
        }
        messageArray.append('Some error occured. Please try again')
        return  {"messages":messageArray}
    
    logging.info(f'Response from lex is {response}')
    server_response = _main_map_lex_intent( response , query , source  )
    
    if server_response.get("ignoreLex"):
        response = server_response
    elif server_response.get("editMessage") and server_response["editMessage"] is True:
        lex_message = response['message']
        for i in range(server_response['variables']):
                pass
        response['message'] = lex_message
        
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
    logging.info( f'Response from lex is {response}' )
    return response

def createMessageDict(senderId , text , has_attachment=False, attach_path=None,attach_type=None   ):
    
    message = {} 
    message[ 'sender' ] = { 'id': senderId  } 
    message[ 'message'] = {
        'text' : text
    }
    
    if has_attachment:
       message['message']['attachment'] = {}
       message['message']['attachment']['path'] = attach_path
       message['message']['attachment']['type'] = attach_type

    return message
  
    
     
if __name__ == "__main__":
    pass