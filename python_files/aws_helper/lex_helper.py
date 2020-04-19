
import json
import os
import time
from flask import jsonify
import boto3
from python_files.attachment_processor.attachment_helper import \
    processAttachment

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
    
    #json format of message to be followed 
    ''' {
            {
            "sender":{
                "id": "4"
                "name":"Pranjal"
            }
            "message":{
                "text":"Hi"
                "attachment":{
                    type: "image/file"
                    path: // for downlaoding    
                }
            }
        }
    } 
    '''
    logging.info( f'Message Json received in generate response is {message}' )
    sender_id = message['sender']['id']
    response = None
    if message['message'].get('attachment'):
        filePath = message['message']['attachment']['path']
        fileType = message['message']['attachment']['type']
        data = processAttachment( filePath , fileType , rootDir )
        response = sendSlotValuesToLex( data , sender_id  ) 
    
    elif message['message'].get('text'):
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
    #response syntax from lex   
    '''      {
                'intentName': 'string',
                'slots': {
                    'string': 'string'
                },
                'sessionAttributes': {
                    'string': 'string'
                },
                'message': 'string',
                'sentimentResponse': {
                    'sentimentLabel': 'string',
                    'sentimentScore': 'string'
                },
                'messageFormat': 'PlainText'|'CustomPayload'|'SSML'|'Composite',
                'dialogState': 'ElicitIntent'|'ConfirmIntent'|'ElicitSlot'|'Fulfilled'|'ReadyForFulfillment'|'Failed',
                'slotToElicit': 'string',
                'responseCard': {
                    'version': 'string',
                    'contentType': 'application/vnd.amazonaws.card.generic',
                    'genericAttachments': [
                        {
                            'title': 'string',
                            'subTitle': 'string',
                            'attachmentLinkUrl': 'string',
                            'imageUrl': 'string',
                            'buttons': [
                                {
                                    'text': 'string',
                                    'value': 'string'
                                },
                            ]
                        },
                    ]
                },
                'sessionId': 'string'
            }
    '''   
        
def sendTextToLex( message , sender_id  ):
    
    #request syntax
    '''  {
            # response = client.post_text(
            #     botName='string',
            #     botAlias='string',
            #     userId='string',
            #     sessionAttributes={
            #         'string': 'string'
            #     },
            #     requestAttributes={
            #         'string': 'string'
            #     },
            #     inputText='string'
            # )
        }
    '''
    
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

def sendSlotValuesToLex( data , sender_id ):
    
    slotValue = { 'receipt':'success' }
    if data.get('unit'): slotValue['unit']=data['unit']
    if data.get('amount'): slotValue['amount']=data['amount']
    if data.get('category'): slotValue['category'] = data['category']
    if data.get('date') : slotValue['date'] = data['date']
    
    client = boto3.client('lex-runtime')
    
    get_session_response = { 'recentIntentSummaryView':[] }
    try:
        get_session_response = client.get_session(
        botName= botName ,
        botAlias= botAlias ,
        userId= sender_id 
        )
        temp = []
        for recentIntent in get_session_response['recentIntentSummaryView']:
            if recentIntent['intentName']!=intentName: 
                temp.append(recentIntent)
            else:
                for key,value in recentIntent['slots'].items():
                    if value is not None:  slotValue[key] = value
                
        get_session_response['recentIntentSummaryView'] = temp     
    except Exception as e:
        logging.info('Session does not exist. Starting new session')
         
    client = boto3.client('lex-runtime')
    response = client.put_session(
        botName=botName,
        botAlias=botAlias,
        userId= sender_id ,
        sessionAttributes={},
        dialogAction={
            'type': 'Delegate',
            'intentName': intentName ,
            'slots': slotValue
        },
        recentIntentSummaryView= get_session_response.get('recentIntentSummaryView') 
    ) 
    #print(response)
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
    #sendSlotValuesToLex({'category':'Food'},'1234567')   
    message =   {
        'sender': {
            'id': '1234'
        }, 
        'message': {
          'text': 'Hi', 
          'attachment': 
            {'name': 'file.pdf', 'type': 'file'}
        }
    }
    generateResponse( message )
 