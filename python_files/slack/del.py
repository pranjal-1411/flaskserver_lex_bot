
import json
import os
import time
from flask import jsonify
import boto3
import logging
from dotenv import load_dotenv
botName = 'AsanifyBot'
botAlias = 'dev'
intentName = None

#import asyncio


def initEnvironment( rootDir ):
    global botName,botAlias,intentName
    load_dotenv(os.path.join(rootDir, '.env'))
    #botName = os.getenv('BOT_NAME')
    #botAlias = os.getenv('BOT_ALIAS')
    #intentName = os.getenv('INTENT_NAME')
    os.environ['AWS_ACCESS_KEY_ID'] =  os.getenv('AWS_ACCESS_KEY_ID')
    os.environ['AWS_SECRET_ACCESS_KEY']= os.getenv('AWS_SECRET_ACCESS_KEY')
    os.environ['AWS_DEFAULT_REGION'] =  os.getenv('AWS_REGION')



async def sendSlotValuesToLex( data=None , intentName='ApplyLeave', sender_id='12344' , useOldValue = False ):
    data = {'type':'123455'}
    slotValue =  data

    client = boto3.client('lex-runtime')
    

    try:
        get_session_response = client.get_session(botName= botName ,botAlias= botAlias ,userId= sender_id )
        for recentIntent in get_session_response['recentIntentSummaryView']:
            if recentIntent['intentName']==intentName:
                [ slotValue.update([item]) for item in recentIntent['slots'].items() if item[1] is not None and (useOldValue or slotValue.get(item[0]) is None)  ] 
                                
    except Exception as e:
        logging.error('---------------Session does not exist. Starting new session')
        
    client =  boto3.client('lex-runtime')
    response = client.put_session(
        botName=botName,
        botAlias=botAlias,
        userId= sender_id ,
        sessionAttributes={},
        dialogAction={
            'type': 'Delegate',
            'intentName': intentName ,
            'slots': slotValue
        }
        #recentIntentSummaryView= get_session_response.get('recentIntentSummaryView') 
    ) 
    logging.error(response)
    #print(response)
    return response


import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def main():
    task1 = loop.create_task(sendSlotValuesToLex())
    task2 = loop.create_task(count())
    
    await asyncio.wait([task1,task2])
    
    

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    # import time
    # s = time.perf_counter()
    # asyncio.run(main())
   
    # elapsed = time.perf_counter() - s
    # print(f"{__file__} executed in {elapsed:0.2f} seconds.")
    

# if __name__ == "__main__":
#     #initEnvironment( '/mnt/f/python3resolve' )
#     data = {'type':'123455'}
#     sender_id='123456'
#     intentName= 'ApplyLeave' #'ApplyLeave'
#     #asyncio.run(sendSlotValuesToLex(data,intentName,sender_id),debug=True)
#     #response = sendSlotValuesToLex(data,intentName,sender_id)
#     asyncio.run(temp())
#     print("hiiiiiiiiii")
#     #logging.error(response)

 