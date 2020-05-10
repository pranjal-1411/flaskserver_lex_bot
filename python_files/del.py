
import json
import os
import time
from flask import jsonify
import boto3
import logging
botName = None
botAlias = None
from dotenv import load_dotenv
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


def sendSlotValuesToLex( sender_id,intentName,slotValue ):
    initEnvironment('/mnt/f/python3resolve')
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
    logging.error(response)
    
    return response


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
    logging.error( f'Response from lex is {response}' )
    return response


if __name__ == "__main__":
    initEnvironment('/mnt/f/python3resolve')
    
    intentName= 'addExpense'
    sender_id = '12345'
    slotValue = {'amount':'12345dgsvsv'}
    sendSlotValuesToLex(sender_id,intentName,slotValue)
    #sendTextToLex('hii',sender_id,)