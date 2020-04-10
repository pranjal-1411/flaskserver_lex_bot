import os
from slackclient import SlackClient
import requests 
from python_files.aws_helper.lex_helper import createMessageDict,generateResponse
from flask import Response
import json
import logging
import csv

def get_auth_token( temp_response_code ):
    
    slack_client = SlackClient(os.getenv("SLACK_TOKEN"))
    auth_response = slack_client.api_call("oauth.v2.access",
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
    

def check_event( event ):
    if event['channel_type'] != 'im':
        return False
        
    if event.get('subtype') and event['subtype'] =='bot_message':
        return False
    
    return True

def _main_process_slack_event(event,rootDir):
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
        lexResponse =  generateResponse(message,rootDir)
    
    if event['type'] == 'message' and event.get('blocks') :
        text = event['blocks'][0]['elements'][0]['elements'][0]['text']
        if event['blocks'][0]['elements'][0]['elements'][0]['type']=='text':
            logging.info( f'Text received from slack is {text}' )
            #slack.send_message( channelId,'Bot received '+ text )
            message = createMessageDict(channelId,text)
        lexResponse =  generateResponse(message,rootDir)
    team_id = event["team"]
    access_token = find_access_token(team_id)
    if lexResponse:
        for message in lexResponse['messages']:
            send_message_to_slack( channelId, message['text'],access_token )

def find_access_token( team_id ):
    os.environ['ROOT_PATH'] = "/mnt/f/python3resolve" 
    path_to_oauth_file = os.path.join(os.getenv('ROOT_PATH'),"python_files","slack","slack_oauth.csv")
    with open(path_to_oauth_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[0] == team_id:
                logging.error(row[1])
                return row[1]
        
    return None 

def send_message_to_slack(channel_id, message,access_token=None):
    
    if access_token is None:
        access_token = os.getenv("SLACK_TOKEN")
    slack_client = SlackClient(access_token)

    response = slack_client.api_call(
        "chat.postMessage",
        channel=channel_id,
        text=message,
        username='Asanifybot',
        icon_emoji=':robot_face:'
    )

    logging.error( f'Response from slack.post api is {response } '  )
    

def downloadFile( fileName , fileUrl , extension ,  downloadPath):
    print(fileUrl)
    
    r = requests.get(fileUrl, headers={'Authorization': 'Bearer %s' % SLACK_TOKEN}) 
 
    
    if r.status_code != 200:
        logging.error('File Download Error ') 
        return 
    
    with open(downloadPath,'wb') as f: 
        f.write(r.content) 


if __name__ == '__main__':
    #send_message_to_slack("D011M87PWG3","just keep trying")
    slack_client = SlackClient(token= "xoxb-1045423027863-1055279789379-m1DsGB0mO0dzboVxgntMm1Du")
    #slack_client.api_call("auth_test", json = {})
    # params = {'channel':channel_id,
    #     'text':message,
    #     'username':'Asanifybot',
    #     'icon_emoji':':robot_face:' }
    # res =requests.post( url='https://slack.com/api/chat.postMessage',data=params,headers={'Authorization': f'Bearer {SLACK_TOKEN}'} )
    # print(res.json)
    #logging.error( f' res is {res} ' )
    response = slack_client.api_call(
        method = "users.info",
        user="U011L9L5T4J"
    )

    logging.error( f'Response from slack.post api is {response } '  )

# pRANJAL ALTER IN SACHIN WORK "U011CEW3XTR"
# PRANJAL IN SACHIN WORK "U011L9L5T4J"
#xoxp-1045423027863-1054326197154-1046494602007-f91b2e3ef505a9bf9221ae647398e7dd
#D011L9L6Q58