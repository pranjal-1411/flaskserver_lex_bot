
import json
import os
import time
from flask import jsonify
import boto3
from python_files.attachment_processor.attachment_helper import \
    processAttachment

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

def sendSlotValuesToLex( slotValue,intentName , sender_id ):
    
    client = boto3.client('lex-runtime')

    get_session_response = { 'recentIntentSummaryView':[] }
    try:
        get_session_response = client.get_session(
        botName= botName ,
        botAlias= botAlias ,
        userId= sender_id 
        )
        logging.error(get_session_response)
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
        botName= botName ,
        botAlias= botAlias ,
        userId= sender_id ,
        sessionAttributes={"HI":"By"},
        dialogAction={
            'type': 'Delegate',
            'intentName': intentName ,
            'slots': slotValue
        },
        recentIntentSummaryView= get_session_response.get('recentIntentSummaryView') 
    ) 
    logging.info(response)
    
    return response


initEnvironment(None)
sendSlotValuesToLex({'leave_type':'Travel'},"ApplyLeave",'500f568b-966c-47c9-8bdf-f699e0db3a48')   