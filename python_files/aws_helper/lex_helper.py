
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
    if rootDir is None:
        rootDir='/mnt/f/python3resolve'
    global botName,botAlias,intentName
    load_dotenv(os.path.join(rootDir, '.env'))
    botName = os.getenv('BOT_NAME')
    botAlias = os.getenv('BOT_ALIAS')
    #intentName = os.getenv('INTENT_NAME')
    # os.environ['AWS_ACCESS_KEY_ID'] =  os.getenv('AWS_ACCESS_KEY_ID')
    # os.environ['AWS_SECRET_ACCESS_KEY']= os.getenv('AWS_SECRET_ACCESS_KEY')
    # os.environ['AWS_DEFAULT_REGION'] =  os.getenv('AWS_REGION')


def generateResponse( message ,rootDir=None ,query = None ,  source = None,turn_context = None ):
     
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
        response = sendSlotValuesToLex( data ,  'addExpense'  , sender_id,useOldValue=True  ) 
    
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
    
    server_response = _main_map_lex_intent(response , query=query , source=source ,turn_context=turn_context ) 
    
    if source == 'ms' and server_response.get("ignoreLex") and server_response.get("intent"):
        return { "messages":[],"intent":server_response['intent']  }
    
    if server_response.get("ignoreLex") and server_response["ignoreLex"] is True:
        response = server_response
    elif server_response.get("editMessage") and server_response["editMessage"] is True:
        lex_message = response['message']
        for i in range(server_response['variables']):
                pass
        response['message'] = lex_message
        
    if response.get('message') and  response['message'][0] == '{':
        response_json = json.loads(response['message'])
        for message in response_json['messages']:
            messageArray.append( message['value'] )
    elif response.get('message')  :
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

def sendSlotValuesToLex( slotValue,intentName , sender_id,session_attributes={} ):
    
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
                    if slotValue.get(key) is None and value is not None:  slotValue[key] = value
                
        get_session_response['recentIntentSummaryView'] = temp  
        if session_attributes == {}:
            session_attributes = get_session_response['sessionAttributes']  
    except Exception as e:
        logging.error('Session does not exist. Starting new session')
         
    client = boto3.client('lex-runtime')
    response = client.put_session(
        botName=botName,
        botAlias=botAlias,
        userId= sender_id ,
        sessionAttributes=session_attributes,
        dialogAction={
            'type': 'Delegate',
            'intentName': intentName ,
            'slots': slotValue
        }
        #recentIntentSummaryView= get_session_response.get('recentIntentSummaryView') 
    ) 
    
    
    return response


def getSlotValuesFromLex( intentName,sender_id,session_attributes=False ):
    client = boto3.client('lex-runtime')
    try:
        get_session_response = client.get_session(botName= botName ,botAlias= botAlias ,userId= sender_id )
        #logging.error(get_session_response)
        for recentIntent in get_session_response['recentIntentSummaryView']:
            if recentIntent['intentName']==intentName:
                if session_attributes :
                    return {
                            'session_attributes':get_session_response['sessionAttributes'],
                            'slots':recentIntent['slots']
                        }
                else:   return recentIntent['slots'] 
                        
                
                                
    except Exception as e:
        return {}
    
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
    sendSlotValuesToLex({'leave_type':'Travel'},"ApplyLeave",'pranjalguptacse@gmail.com')   
    # message =   {
    #     'sender': {
    #         'id': '1234'
    #     }, 
    #     'message': {
    #       'text': 'Hi', 
    #       'attachment': 
    #         {'name': 'file.pdf', 'type': 'file'}
    #     }
    # }
    # generateResponse( message )
 