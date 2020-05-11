import os
from slack import WebClient
import requests 
from python_files.aws_helper.lex_helper import createMessageDict,generateResponse
from flask import Response
import json
import logging
import csv

import hmac
import hashlib
import base64
import time
import binascii


def get_auth_token( temp_response_code ):
    
    slack_client = WebClient(os.getenv("SLACK_TOKEN"))
    auth_response = slack_client.oauth_v2_access(
                client_id=os.getenv("CLIENT_ID"),
                client_secret=os.getenv("CLIENT_SECRET"),
                code=temp_response_code)
    logging.info(auth_response)
    
    if auth_response["ok"] is False:
        logging.error(f'Error during authentication: {auth_response}')
        return False
    logging.info(f'Auth successful {auth_response}' )
    access_token = auth_response['access_token']
    team_id = auth_response["team"]["id"]
    path_to_oauth_file = os.path.join(os.getenv('ROOT_PATH'),"python_files","slack","slack_oauth.csv")
    
    with open(path_to_oauth_file, "a") as auth_csv:
        auth_csv.write(f'{team_id},{access_token}')
        
    return True    
   
def verify_slack_request( request ):
    key = os.getenv('SLACK_SIGNING_SECRET')
    byte_key = binascii.unhexlify(key)
    timestamp = request.headers['X-Slack-Request-Timestamp']
    if abs(time.time()-int(timestamp)) > 60*5 :
        return False 
    req = str.encode('v0:' + str(timestamp) + ':') + request.get_data()
    my_signature = 'v0=' + hmac.new(
        str.encode(key),
        req, hashlib.sha256
    ).hexdigest()
    
    slack_signature = request.headers['X-Slack-Signature']
    return hmac.compare_digest( my_signature,slack_signature )
     

def check_event( event ):
    if event.get('channel_type') and event['channel_type'] != 'im':
        return False
        
    if event.get('subtype') and event['subtype'] =='bot_message':
        return False
    
    return True

def _main_process_slack_event(query,rootDir):
    event = query['event']
    team_id = query["team_id"]
    access_token = find_access_token(team_id)
        
    message = None 
    lexResponse = None
    
    if check_event(event) is False:
        return 
    
    channelId = event['channel']
    if event.get('subtype') and event['subtype'] =='file_share':
        
        for File in event['files']:
            downloadPath = os.path.join(rootDir,'processedAttachment', File['name'])
            downloadFile(File['name'],File['url_private'],File['filetype'],downloadPath) ; 
            #slack.send_message('Bot received '+ File['name'],channelId )
            message = createMessageDict(channelId,None,has_attachment=True,attach_path=downloadPath,attach_type=File['filetype'])   
        lexResponse =  generateResponse(message,rootDir,query,"slack")
    
    if event['type'] == 'message' and event.get('blocks') :
        text = event['blocks'][0]['elements'][0]['elements'][0]['text']
        if event['blocks'][0]['elements'][0]['elements'][0]['type']=='text':
            logging.info( f'Text received from slack is {text}' )
            #slack.send_message( channelId,'Bot received '+ text )
            message = createMessageDict(channelId,text)
        lexResponse =  generateResponse(message,rootDir,query,"slack")
    
    if lexResponse:
        for message in lexResponse['messages']:
            send_message_to_slack( channelId, text= message['text'],access_token=access_token )

def find_access_token( team_id ):
    
    return None 

def update_slack_message(channel_id,ts, text=None,blocks=None,access_token=None):
    if access_token is None:
        access_token = os.getenv("SLACK_TOKEN")
    slack_client = WebClient(access_token)
    
    response = slack_client.chat_update(
        as_user=True,
        ok= True,
    channel= channel_id,
    ts=ts,
    text= text,
    blocks=blocks,  
    )
    logging.info(f'Response on slack update message is {response}')   
    

def send_message_to_slack(channel_id, text=None,blocks = None,access_token=None):
    
    if access_token is None:
        access_token = os.getenv("SLACK_TOKEN")
    slack_client = WebClient(access_token)

    response = slack_client.chat_postMessage(
        channel=channel_id,
        text= text,
        blocks= blocks
    )

    logging.info( f'Response from slack.post api is {response }' )
    
def get_user_info( user_id, workspace_id ):
    access_token = find_access_token(workspace_id)
    if access_token is None:
        access_token = os.getenv("SLACK_TOKEN")
    slack_client = WebClient(token= access_token)
    response = slack_client.users_info(
        user=user_id
    )

    if not response['ok']:
        logging.error( "Unable to retrieve user info" )
        logging.error(response)
        return None   
    
    return response['user']

def downloadFile( fileName , fileUrl , extension ,  downloadPath , access_token=None):
    
    logging.info(fileUrl)
    if access_token is None:
        access_token = os.getenv('SLACK_TOKEN')
    r = requests.get(fileUrl, headers={'Authorization': 'Bearer %s' % access_token}) 
 
    
    if r.status_code != 200:
        logging.error('File Download Error ') 
        return 
    
    with open(downloadPath,'wb') as f: 
        f.write(r.content) 


if __name__ == '__main__':
    pass
